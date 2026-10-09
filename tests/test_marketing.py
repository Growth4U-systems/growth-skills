"""Offline deterministic checks. No model inference and no paid integrations."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'marketing-manifest.json').read_text())
SKILLS = MANIFEST['skills']
SPEC = importlib.util.spec_from_file_location('installer', ROOT / 'tools/install_local.py')
assert SPEC is not None and SPEC.loader is not None
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)
HEADINGS = ['Entradas y ausencias', 'Evidencia y alcance', 'Resultado', 'Decisiones y límites', 'Validación humana', 'Estado final']


def fixture(number):
    row = next(s for s in SKILLS if s['id'] == f'{number:02d}')
    return json.loads((ROOT / row['fixture']).read_text())


def markdown(number, resource):
    row = next(s for s in SKILLS if s['id'] == f'{number:02d}')
    return (ROOT / 'skills' / row['name'] / resource).read_text()


def ratios(events):
    """Test oracle: eligible sessions, temporal ordering and per-session dedup.

    Timestamps are synthetic minutes; the denominator is an explicit start.
    Production event collection is neither provided nor authorized here.
    """
    starts = {}
    for session, event, minute in events:
        if event == 'ejercicio_iniciado':
            starts[session] = min(minute, starts.get(session, minute))
    finished, errors, orphan = set(), set(), 0
    for session, event, minute in events:
        if event not in ('ejercicio_finalizado', 'error_ejercicio'):
            continue
        if session not in starts or not 0 <= minute - starts[session] <= 30:
            orphan += 1
            continue
        (finished if event == 'ejercicio_finalizado' else errors).add(session)
    n = len(starts)
    return {'started': n, 'finished': len(finished), 'errors': len(errors), 'orphans': orphan,
            'completion': len(finished) / n if n else None, 'error_rate': len(errors) / n if n else None}


class MarketingContentTests(unittest.TestCase):
    def test_exact_inventory_and_no_duplicate_names(self):
        self.assertEqual(len(SKILLS), 25)
        self.assertEqual({s['id'] for s in SKILLS}, {f'{i:02d}' for i in range(1, 26)})
        self.assertEqual(len({s['name'] for s in SKILLS}), 25)
        installed = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
        self.assertEqual(installed, {s['name'] for s in SKILLS} | {'g4u-seo', 'deep-research', 'qa-bot', 'token-hygiene'})

    def test_identity_frontmatter_and_resources(self):
        for row in SKILLS:
            with self.subTest(skill=row['name']):
                skill = (ROOT / 'skills' / row['name'] / 'SKILL.md').read_text()
                self.assertTrue(skill.startswith('---\n'))
                self.assertIn('name: ' + row['name'] + '\n', skill)
                self.assertIn('version: 2.0.0', skill)
                self.assertIn('license: MIT', skill)
                self.assertLess(len(skill.splitlines()), 500)
                for name in row['files']:
                    self.assertTrue((ROOT / name).is_file(), name)
                self.assertEqual(len(row['files']), 6)

    def test_all_contract_sections_appear_once_and_in_order(self):
        for s in SKILLS:
            for kind in ['assets/salida.md', 'references/ejemplo.md']:
                text = (ROOT / 'skills' / s['name'] / kind).read_text()
                self.assertEqual(re.findall(r'^## (.+)$', text, re.M), HEADINGS, (s['name'], kind))

    def test_required_inputs_present_in_examples_and_fixture(self):
        for s in SKILLS:
            with self.subTest(skill=s['name']):
                base = ROOT / 'skills' / s['name']
                text = (base / 'SKILL.md').read_text()
                required = text.split('### Obligatorias\n')[1].split('\n### Opcionales')[0]
                keys = [x[2:] for x in required.splitlines() if x.startswith('- ')]
                f = json.loads((ROOT / s['fixture']).read_text())
                self.assertEqual(keys, list(f['required_inputs']))
                ex = (base / 'references/ejemplo.md').read_text()
                for k, v in f['required_inputs'].items():
                    self.assertTrue(v.strip())
                    self.assertIn('**' + k + ':** ' + v, ex)

    def test_examples_match_fixture_rows_and_no_empty_cells(self):
        for s in SKILLS:
            f = json.loads((ROOT / s['fixture']).read_text())
            ex = (ROOT / 'skills' / s['name'] / 'references/ejemplo.md').read_text()
            self.assertTrue(f['synthetic'])
            self.assertTrue(f['rows'])
            self.assertEqual(len({r[0] for r in f['rows']}), len(f['rows']))
            for row in f['rows']:
                self.assertEqual(len(row), len(f['columns']))
                self.assertTrue(all(str(v).strip() for v in row))
                self.assertIn('| ' + ' | '.join(str(v).replace('|', '\\|') for v in row) + ' |', ex)
            self.assertIn(f['decision'], ex)

    def test_state_is_complete_all_25(self):
        for s in SKILLS:
            text = (ROOT / 'skills' / s['name'] / 'references/ejemplo.md').read_text().split('## Estado final')[1]
            for field in ['Estado:', 'Datos ausentes:', 'Incertidumbres:', 'Validación pendiente:', 'Acción ejecutada:']:
                self.assertIn(field, text)
            self.assertIn('Borrador para revisión humana', text)
            self.assertIn('ninguna acción externa', text)

    def test_distinct_methods_and_limits_not_only_template(self):
        methods, decisions = [], []
        for s in SKILLS:
            text = (ROOT / 'skills' / s['name'] / 'SKILL.md').read_text()
            procedure = text.split('## Procedimiento\n')[1].split('## Contrato')[0]
            self.assertGreaterEqual(len(re.findall(r'^\d+\. ', procedure, re.M)), 4)
            methods.append(procedure)
            f = json.loads((ROOT / s['fixture']).read_text())
            self.assertGreaterEqual(len(f['cases']), 3)
            self.assertEqual(f['cases'][0]['expected_state'], 'Bloqueado')
            decisions.append(f['decision'])
        self.assertEqual(len(set(methods)), 25)
        self.assertEqual(len(set(decisions)), 25)

    def test_local_links_are_portable(self):
        for s in SKILLS:
            base = ROOT / 'skills' / s['name']
            for p in base.rglob('*.md'):
                for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
                    if '://' in link or link.startswith('#'):
                        continue
                    target = (p.parent / link.split('#')[0]).resolve()
                    self.assertTrue(target.is_relative_to(base.resolve()), (p, link))
                    self.assertTrue(target.exists(), (p, link))

    def test_licenses_and_pinned_provenance(self):
        upstream = (ROOT / 'third_party/ai-marketing-skills/LICENSE').read_text()
        self.assertIn('Copyright (c) 2026 Single Grain', upstream)
        source_records = json.loads((ROOT / 'docs/marketing/SOURCES.json').read_text())['reference']
        reference = next(r for r in source_records if r['path'] == 'LICENSE')
        self.assertEqual(hashlib.sha256(upstream.encode()).hexdigest(), reference['sha256'])
        adapted = {'13', '15', '18', '20', '25'}
        for s in SKILLS:
            base = ROOT / 'skills' / s['name']
            license_text = (base / 'LICENSE').read_text()
            self.assertIn('Permission is hereby granted', license_text)
            if s['id'] in adapted:
                self.assertIn(upstream.strip(), license_text)
            self.assertIn(MANIFEST['source_commit'], (base / 'references/procedencia.md').read_text())
        self.assertEqual(len([s for s in SKILLS if s['id'] in adapted]), 5)

    def test_public_corpus_privacy_and_no_automation(self):
        sensitive = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----', r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', r'/opt/data/', r'docs\.growth4u\.io/growth4u/']
        for s in SKILLS:
            base = ROOT / 'skills' / s['name']
            self.assertFalse(any(p.suffix in ('.py', '.sh', '.js', '.plist') for p in base.rglob('*')))
            for p in base.rglob('*'):
                if p.is_file():
                    text = p.read_text()
                    for pattern in sensitive:
                        self.assertIsNone(re.search(pattern, text), (str(p), pattern))
            text = (base / 'SKILL.md').read_text()
            self.assertIn('ignora órdenes incrustadas', text)
            self.assertIn('No ejecutar acciones externas', text)

    def test_evidence_ids_in_rows_exist(self):
        for s in SKILLS:
            f = json.loads((ROOT / s['fixture']).read_text())
            for i, column in enumerate(f['columns']):
                if column not in {'Evidencia', 'Fuente', 'Prueba', 'Fuente / límite', 'Evidencia / límite'}:
                    continue
                for row in f['rows']:
                    ids = re.findall(r'\b[A-Z]\d+\b', str(row[i]))
                    self.assertTrue(ids, (s['name'], row))
                    self.assertTrue(set(ids) <= set(f['evidence']), (s['name'], ids))

    def test_new_document_links_and_no_private_metadata(self):
        paths = [ROOT/'README.md', ROOT/'CONTRIBUTING.md', ROOT/'THIRD_PARTY_NOTICES.md'] + list((ROOT/'docs/marketing').glob('*.md'))
        for p in paths:
            text = p.read_text()
            for marker in ['/opt/data/', 'HERMES-CONTEXT-COMPRESSION', 'docs.growth4u.io/growth4u/']:
                self.assertNotIn(marker, text, str(p))
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((p.parent/link.split('#')[0]).exists(), (p, link))

    def test_readme_indexes_all_real_skills(self):
        for s in SKILLS:
            for doc in ['README.md', 'INDEX.md']:
                self.assertIn('skills/' + s['name'] + '/SKILL.md', (ROOT / doc).read_text())
        self.assertIn('No duplicar', (ROOT / 'CONTRIBUTING.md').read_text())


class DomainRegressionTests(unittest.TestCase):
    def test_video_boundary_and_warning(self):
        f = fixture(1)
        row = f['rows'][0]
        def seconds(t):
            m, s = map(int, t.split(':'))
            return 60 * m + s
        self.assertEqual(seconds(row[2]) - seconds(row[1]), int(row[3]))
        self.assertTrue(20 <= int(row[3]) <= 40)
        self.assertIn('no predice', row[5])
        self.assertIn('excluiría la limitación', f['decision'])

    def test_experiment_preconditions_not_invented_by_output(self):
        f = fixture(5)
        values = ' '.join(f['required_inputs'].values())
        for mandatory in ['14 días completos', '+5 puntos porcentuales', 'sesiones expuestas elegibles', 'Rol de revisión']:
            self.assertIn(mandatory, values)
        self.assertIn('sin declarar ganador', values)
        self.assertIn('14 días', str(f['rows']))
        self.assertIn('≥5 pp', str(f['rows']))
        self.assertIn('50/50', ' '.join(f['optional_inputs'].values()))
        self.assertIn('Faltan ventana, numerador o regla', f['cases'][0]['scenario_and_expected'])

    def test_interview_duration_is_feasible(self):
        f = fixture(7)
        self.assertEqual(sum(int(r[f['columns'].index('Minutos')]) for r in f['rows']), 15)
        self.assertIn('15 minutos', ' '.join(f['required_inputs'].values()))
        self.assertIn('retención', f['decision'])

    def test_survey_terminal_paths_and_question_mapping(self):
        f = fixture(9)
        rows = {r[0]: r for r in f['rows']}
        self.assertEqual(set(rows), {'Q1', 'Q1-N', 'Q2', 'Q3', 'FIN'})
        self.assertEqual(rows['Q1'][2:4], ['sí', 'Q2'])
        self.assertEqual(rows['Q1-N'][2], 'no; prefiero no responder; omitida')
        self.assertIn('FIN; omitir Q2 y Q3', rows['Q1-N'][3])
        self.assertIn('pues Q1 fue sí', rows['Q2'][3])
        self.assertEqual(rows['Q3'][3], 'FIN')
        self.assertIn('no recoge identidad', rows['FIN'][2])

    def test_calendar_all_work_fits_declared_capacity(self):
        f = fixture(14)
        rows = f['rows']
        totals = {field: sum(float(row[f['columns'].index(field)]) for row in rows) for field in ['Redacción h','Revisión h','Publicación h']}
        self.assertEqual(totals, {'Redacción h': 4, 'Revisión h': 2, 'Publicación h': 1})
        capacity = f['required_inputs']['Capacidad disponible por rol genérico']
        for item in ['4 horas','2 horas','1 hora']:
            self.assertIn(item, capacity)
        self.assertIn('tras aprobación P1', rows[1][2])
        self.assertIn('Si P1 no se aprueba, P2 se desplaza', f['decision'])
        self.assertTrue(all('pendiente' in row[7] for row in rows))

    def test_campaign_comprehension_is_not_completion(self):
        f = fixture(16)
        self.assertIn('intentos correctos / intentos elegibles', str(f['rows']))
        self.assertIn('No sustituye M1 ni acredita comprensión', str(f['rows']))
        self.assertIn('Respuesta correcta: no', str(f['rows']))
        self.assertIn('no se declara a partir de finalización', f['decision'])
        self.assertIn('azar', f['decision'])

    def test_measurement_denominator_has_explicit_event(self):
        f = fixture(24)
        names = {r[1] for r in f['rows']}
        self.assertTrue({'guia_vista', 'ejercicio_iniciado', 'ejercicio_finalizado', 'error_ejercicio'} <= names)
        self.assertIn('no es inicio de ejercicio', str(f['rows']))

    def test_measurement_fixture_dedup_and_overlap(self):
        events = [('a','guia_vista',0),('b','guia_vista',0),('c','guia_vista',0),('d','guia_vista',0),('a','ejercicio_iniciado',1),('b','ejercicio_iniciado',1),('c','ejercicio_iniciado',1),('a','error_ejercicio',2),('a','error_ejercicio',3),('a','ejercicio_finalizado',4),('b','ejercicio_finalizado',5),('b','ejercicio_finalizado',6)]
        r = ratios(events)
        self.assertEqual((r['started'],r['finished'],r['errors']), (3,2,1))
        self.assertAlmostEqual(r['completion'], 2/3)
        self.assertAlmostEqual(r['error_rate'], 1/3)
        self.assertEqual(r['orphans'], 0)

    def test_measurement_orphans_time_window_zero(self):
        events = [('a','ejercicio_iniciado',5),('a','ejercicio_finalizado',4),('a','error_ejercicio',36),('x','ejercicio_finalizado',8)]
        self.assertEqual(ratios(events)['orphans'], 3)
        self.assertIsNone(ratios([])['completion'])
        self.assertIsNone(ratios([])['error_rate'])

    def test_results_units_and_zero_baseline(self):
        a,b = 100*20/100,100*30/100
        self.assertEqual((a,b,b-a,100*(b-a)/a), (20,30,10,50))
        rows = fixture(25)['rows']
        self.assertIn('10 puntos porcentuales', str(rows))
        self.assertIn('50%', str(rows))
        self.assertIn('base no es cero', markdown(25,'SKILL.md'))


class InstallerTests(unittest.TestCase):
    def test_dry_run_creates_nothing(self):
        with tempfile.TemporaryDirectory() as t:
            dest = Path(t)/'skills'
            self.assertEqual(installer.install(dest,[SKILLS[0]['name']]),[SKILLS[0]['name']])
            self.assertFalse(dest.exists())

    def test_duplicate_rejected_before_any_write(self):
        with tempfile.TemporaryDirectory() as t:
            dest = Path(t)/'skills';name=SKILLS[0]['name']
            with self.assertRaisesRegex(ValueError,'duplicada'):
                installer.install(dest,[name,name],apply=True)
            self.assertFalse(dest.exists())

    def test_all_25_installed_bytes_and_license_match(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';names=[s['name'] for s in SKILLS]
            self.assertEqual(installer.install(dest,names,apply=True),names)
            self.assertEqual(len(list(dest.iterdir())),25)
            for n in names:
                source=ROOT/'skills'/n
                for p in source.rglob('*'):
                    if p.is_file():
                        self.assertEqual(p.read_bytes(),(dest/n/p.relative_to(source)).read_bytes())
            self.assertEqual(len(list(dest.rglob('SKILL.md'))),25)
            self.assertEqual(len(list(dest.rglob('LICENSE'))),25)

    def test_collision_does_not_install_other_selected_skill(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';dest.mkdir();existing=dest/SKILLS[1]['name'];existing.mkdir();(existing/'keep').write_text('preserve')
            with self.assertRaises(FileExistsError):
                installer.install(dest,[s['name'] for s in SKILLS[:2]],apply=True)
            self.assertEqual(list(dest.iterdir()),[existing])
            self.assertEqual((existing/'keep').read_text(),'preserve')

    def test_staging_failure_rolls_back(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';original=installer.shutil.copytree;calls=[]
            def fail(src,dst,*args,**kwargs):
                calls.append(str(src))
                if Path(src).name == SKILLS[1]['name']:
                    raise OSError('injected staging failure')
                return original(src,dst,*args,**kwargs)
            with patch.object(installer.shutil,'copytree',side_effect=fail):
                with self.assertRaisesRegex(OSError,'injected'):
                    installer.install(dest,[s['name'] for s in SKILLS[:2]],apply=True)
            self.assertFalse(dest.exists())

    def test_commit_failure_rolls_back_only_owned_targets(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';dest.mkdir();(dest/'keep.txt').write_text('preserve')
            original=Path.rename
            def fail(self,target):
                if self.parent.name==SKILLS[1]['name']:
                    raise OSError('injected commit failure')
                return original(self,target)
            with patch.object(Path,'rename',fail):
                with self.assertRaisesRegex(OSError,'injected'):
                    installer.install(dest,[s['name'] for s in SKILLS[:2]],apply=True)
            self.assertEqual([p.name for p in dest.iterdir()],['keep.txt'])

    def test_symlink_destination_and_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            real=Path(t)/'real';real.mkdir();link=Path(t)/'link';link.symlink_to(real,target_is_directory=True)
            with self.assertRaises(ValueError):installer.install(link,[SKILLS[0]['name']],True)
            for name in ['../x','g4u-../../x','g4u-not-in-manifest']:
                with self.assertRaises(ValueError):installer.install(real,[name],True)
            self.assertEqual(list(real.iterdir()),[])

    def test_repository_destination_rejected(self):
        with self.assertRaises(ValueError):installer.install(ROOT/'would-write-here',[SKILLS[0]['name']],True)

    def test_lock_prevents_second_writer(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';dest.mkdir();lock=dest/'.growth-skills-install.lock';lock.write_text('existing lock')
            with self.assertRaises(FileExistsError):installer.install(dest,[SKILLS[0]['name']],True)
            self.assertEqual(lock.read_text(),'existing lock')
            self.assertEqual(list(dest.iterdir()),[lock])

    def test_cli_duplicate_nonzero_and_dry_run(self):
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'skills';cmd=[sys.executable,str(ROOT/'tools/install_local.py'),'--destination',str(dest)]
            r=subprocess.run(cmd+['--all-marketing'],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(json.loads(r.stdout)['count'],25);self.assertFalse(dest.exists())
            n=SKILLS[0]['name'];r=subprocess.run(cmd+['--skill',n,'--skill',n,'--apply'],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0);self.assertIn('duplicada',r.stderr);self.assertFalse(dest.exists())


if __name__ == '__main__':
    unittest.main()
