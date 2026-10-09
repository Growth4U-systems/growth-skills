#!/usr/bin/env python3
"""Copy reviewed marketing skills locally. No network, shell or profile edits.

Preflight rejects duplicate selections before any write. All copies are staged
before reserving targets; caught failures remove only directories created by this
invocation. This is rollback on ordinary errors, not crash-atomic multi-directory
commit. An interrupted process may require manual inspection of its lock/staging.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def _no_symlinks(path):
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError('No se permiten enlaces simbólicos en el destino.')


def install(destination, names, apply=False):
    names = list(names)
    if not names:
        raise ValueError('Selecciona al menos una skill.')
    if len(names) != len(set(names)):
        raise ValueError('Selección duplicada; no se ha escrito ningún archivo.')
    destination = Path(destination).expanduser().absolute()
    _no_symlinks(destination)
    destination = destination.resolve()
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError('El destino debe estar fuera del repositorio.')
    if destination.exists() and not destination.is_dir():
        raise ValueError('El destino debe ser un directorio.')
    allowed = {x['name'] for x in json.loads((ROOT / 'marketing-manifest.json').read_text())['skills']}
    sources = []
    for name in names:
        if not re.fullmatch(r'g4u-[a-z0-9]+(?:-[a-z0-9]+)*', name) or name not in allowed:
            raise ValueError('Skill de marketing no permitida: ' + name)
        source = ROOT / 'skills' / name
        if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError('No se copian enlaces simbólicos.')
        if not (source / 'SKILL.md').is_file() or not (source / 'LICENSE').is_file():
            raise ValueError('Skill o licencia incompleta: ' + name)
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError('No se sobrescribe una skill existente: ' + name)
        sources.append(source)
    if not apply:
        return names

    # Require the caller to create the parent explicitly: no hidden mkdir chain.
    if not destination.parent.is_dir():
        raise ValueError('Crea explícitamente el directorio padre del destino.')
    created_destination = not destination.exists()
    destination.mkdir(exist_ok=True)
    lock = destination / '.growth-skills-install.lock'
    locked = False
    stage = None
    reserved = []
    try:
        fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        os.close(fd)
        locked = True
        stage = Path(tempfile.mkdtemp(prefix='.growth-skills-stage-', dir=destination))
        for source in sources:
            shutil.copytree(source, stage / source.name)
        # mkdir is exclusive even if an uncooperative writer races the preflight.
        for source in sources:
            target = destination / source.name
            target.mkdir()
            reserved.append(target)
        for target in reserved:
            for child in (stage / target.name).iterdir():
                child.rename(target / child.name)
        return names
    except BaseException:
        for target in reversed(reserved):
            shutil.rmtree(target)
        raise
    finally:
        if stage is not None:
            shutil.rmtree(stage)
        if locked:
            lock.unlink()
        if created_destination and not any(destination.iterdir()):
            destination.rmdir()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destination', required=True)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--all-marketing', '--all', dest='all_marketing', action='store_true', help='Solo las 25 skills del manifiesto; no activa las cuatro preexistentes')
    group.add_argument('--skill', action='append')
    p.add_argument('--apply', action='store_true', help='Sin esta opción no escribe nada')
    args = p.parse_args()
    names = sorted(x['name'] for x in json.loads((ROOT / 'marketing-manifest.json').read_text())['skills']) if args.all_marketing else args.skill
    try:
        result = install(args.destination, names, args.apply)
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    print(json.dumps({'mode': 'copied' if args.apply else 'dry-run', 'count': len(result), 'skills': result}, ensure_ascii=False))


if __name__ == '__main__':
    main()
