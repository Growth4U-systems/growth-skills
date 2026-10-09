# GrowthSkills

**Procedimientos reutilizables de Growth4U para investigar, decidir y preparar trabajo de marketing con evidencia.** No son un motor de campañas ni una promesa de resultados: una skill guía a tu agente; no garantiza que el modelo siga bien cada instrucción.

El catálogo contiene **29 skills**: cuatro herramientas/orquestadores existentes y **25 procedimientos de marketing** con entradas explícitas, contrato de salida, ejemplo completo, casos límite y licencia portable. Las 25 se integran desde [`marketing-skills-25`](https://github.com/Growth4U-systems/marketing-skills-25/tree/4d54e83f25e37b2ee467f6cd216ec70211d1e228), conservando identidades y atribución; no necesitas instalar ambos catálogos.

[Catálogo y dependencias](INDEX.md) · [Instalación segura](#instalación-segura) · [Cómo usarlas](#cómo-usarlas) · [Pruebas y límites](#pruebas-y-límites) · [Contribuir](CONTRIBUTING.md) · [Procedencia](docs/marketing/PROCEDENCIA.md)

## Qué valor aportan

- **Una decisión, no solo una plantilla:** cada procedimiento explica qué comparar, cuándo bloquear, qué no puede inferirse y qué evidencia cambiaría la recomendación.
- **Entregas revisables:** ejemplos con todos los campos del contrato, fuentes con ID, datos ausentes y un estado final explícito.
- **Especialización útil:** saltos de encuesta, capacidad editorial por rol, denominadores instrumentados, métricas directas frente a proxies y reglas de experimento definidas antes de ver resultados.
- **Sin ejecución oculta en las 25 de marketing:** no contienen scripts, no necesitan claves ni llamadas externas y no envían, publican, reclutan, instrumentan ni gastan. Los orquestadores históricos tienen dependencias distintas: revisa sus fichas antes de usarlos.

## Elige por tarea

### Orquestación y herramientas existentes

Estos cuatro directorios se conservan sin cambios de contenido en la integración. Sus capacidades no se han revalidado con esta suite de marketing.

| Skill | Para qué sirve | Dependencias y límites |
|---|---|---|
| [g4u-seo](skills/g4u-seo/SKILL.md) | Orquestación SEO end-to-end: auditorías, páginas, contenido y handoffs | Coordina otras skills y herramientas; consulta su stack. No equivale al brief documental de abajo. |
| [deep-research](skills/deep-research/SKILL.md) | Investigación multifuente con QA y entrega por entidades | Herramientas de investigación y acceso a fuentes; comprobar disponibilidad y permisos. |
| [qa-bot](skills/qa-bot/SKILL.md) | Revisión crítica con Chain of Verification | La verificación depende de disponer de fuentes y herramientas; no convierte inferencias en hechos. |
| [token-hygiene](skills/token-hygiene/SKILL.md) | Diagnóstico del contexto y consumo de tokens | Incluye shell y automatización local; revisar scripts y entorno antes de instalar/ejecutar. |

### Investigación y estrategia

| Skill | Entrada → salida útil |
|---|---|
| [g4u-plan-investigacion](skills/g4u-plan-investigacion/SKILL.md) | Decisión, incertidumbres y límites → preguntas, métodos, señales y condiciones de parada |
| [g4u-guion-entrevista](skills/g4u-guion-entrevista/SKILL.md) | Objetivo, episodio y condiciones de registro → guion neutral con tiempos y consentimiento pendiente explícito |
| [g4u-sintesis-entrevistas](skills/g4u-sintesis-entrevistas/SKILL.md) | Notas autorizadas con IDs → observaciones, contraejemplos, hipótesis y límites de generalización |
| [g4u-encuesta-diagnostico](skills/g4u-encuesta-diagnostico/SKILL.md) | Decisión, audiencia y privacidad → cuestionario con saltos, omisiones y salida segura |
| [g4u-comparativa-alternativas](skills/g4u-comparativa-alternativas/SKILL.md) | Criterios y fuentes por alternativa → comparación que distingue ausencia de información de ausencia de capacidad |
| [g4u-posicionamiento](skills/g4u-posicionamiento/SKILL.md) | Segmento, problema, alternativa y pruebas → propuesta de posicionamiento y contraste, sin superioridad inventada |
| [g4u-matriz-mensajes](skills/g4u-matriz-mensajes/SKILL.md) | Necesidades, capacidades y pruebas → mensajes por situación con evidencia y límites |

### Contenido y comunicación

| Skill | Entrada → salida útil |
|---|---|
| [g4u-plan-cortes-video](skills/g4u-plan-cortes-video/SKILL.md) | Transcripción marcada → cortes candidatos que conservan contexto y negaciones; no edición de vídeo |
| [g4u-brief-seo](skills/g4u-brief-seo/SKILL.md) | Pregunta, intención y fuentes → brief editorial con huecos; no investigación SERP automática |
| [g4u-contenido-con-fuentes](skills/g4u-contenido-con-fuentes/SKILL.md) | Brief y fuentes autorizadas → texto con trazabilidad de afirmaciones |
| [g4u-email-revision-humana](skills/g4u-email-revision-humana/SKILL.md) | Objetivo, relación permitida y oferta → email completo no enviado con condiciones de revisión |
| [g4u-mapa-contenidos](skills/g4u-mapa-contenidos/SKILL.md) | Necesidades e inventario → mapa de piezas con reutilización, dependencias y señales de solapamiento |
| [g4u-calendario-editorial](skills/g4u-calendario-editorial/SKILL.md) | Piezas, dependencias y capacidad por rol → calendario condicionado a carga y aprobación reales |
| [g4u-reutilizacion-activo](skills/g4u-reutilizacion-activo/SKILL.md) | Activo autorizado y destinos → derivados concretos sin perder advertencias ni ampliar derechos |
| [g4u-edicion-texto](skills/g4u-edicion-texto/SKILL.md) | Texto y hechos aprobados → versión revisada y registro de cambios de significado |
| [g4u-brief-recurso-descargable](skills/g4u-brief-recurso-descargable/SKILL.md) | Necesidades y capacidad → recurso mínimo con fragmento resuelto; no captación implícita |

### Campañas, experiencia y lifecycle

| Skill | Entrada → salida útil |
|---|---|
| [g4u-brief-campana](skills/g4u-brief-campana/SKILL.md) | Objetivo, oferta y restricciones → activos y métricas que no confunden finalización con comprensión |
| [g4u-estructura-landing](skills/g4u-estructura-landing/SKILL.md) | Audiencia, oferta y hechos → orden de secciones, texto y acción; no una página implementada |
| [g4u-revision-conversion](skills/g4u-revision-conversion/SKILL.md) | Material de página disponible → hipótesis de fricción limitadas a lo observable |
| [g4u-secuencia-bienvenida](skills/g4u-secuencia-bienvenida/SKILL.md) | Solicitud, objetivo y salida → mensajes completos con reevaluación de baja antes de cada paso |
| [g4u-secuencia-educativa](skills/g4u-secuencia-educativa/SKILL.md) | Dudas, hechos y frecuencia → explicación progresiva con salida y práctica opcional |
| [g4u-onboarding-primer-valor](skills/g4u-onboarding-primer-valor/SKILL.md) | Tarea y flujo → primer valor observable con estados vacío, error y recuperación |

### Experimentos y medición

| Skill | Entrada → salida útil |
|---|---|
| [g4u-ficha-experimento](skills/g4u-ficha-experimento/SKILL.md) | Hipótesis y parámetros aportados → diseño previo, sin inventar regla, ventana o ganador |
| [g4u-plan-medicion](skills/g4u-plan-medicion/SKILL.md) | Recorrido y pregunta → diccionario con eventos del numerador y denominador, orden y deduplicación |
| [g4u-informe-resultados](skills/g4u-informe-resultados/SKILL.md) | Agregados comparables → tasas, puntos porcentuales, cambio relativo y decisiones no causales |

## Instalación segura

**Python 3.10 o superior**, biblioteca estándar, sin `pip`. Primero revisa el contenido y [`tools/install_local.py`](tools/install_local.py). Instalar aquí significa copiar carpetas; **no prueba la carga ni el comportamiento de un runtime**.

```bash
git clone https://github.com/Growth4U-systems/growth-skills.git
cd growth-skills
python3 -m unittest discover -s tests -v
```

Para reproducir una revisión, usa el SHA de su PR/release en lugar de asumir que `main` sigue igual.

### Prueba aislada, sin tocar tu agente

```bash
# Crea una carpeta nueva; aborta si ya existe.
mkdir ../growthskills-sandbox
# Plan: no escribe nada.
python3 tools/install_local.py --destination ../growthskills-sandbox/skills --all-marketing
# Copia explícita de las 25, manteniendo licencias y referencias.
python3 tools/install_local.py --destination ../growthskills-sandbox/skills --all-marketing --apply
```

`--all-marketing` incluye solo las 25 del manifiesto, **no** los cuatro orquestadores. `--all` es un alias del mismo conjunto. Para una sola skill:

```bash
python3 tools/install_local.py --destination ../growthskills-sandbox/seleccion \
  --skill g4u-plan-medicion --apply
```

El instalador rechaza duplicados, colisiones, rutas internas al repositorio y enlaces simbólicos. Copia primero a staging y revierte los destinos que creó si encuentra un error normal. **No sobrescribe y no es una transacción resistente a corte de energía:** si el proceso se interrumpe abruptamente, inspecciona su lock y staging antes de limpiar o reintentar. No ofrece un modo `--force`.

### Activación en tu runtime: paso separado

- **Claude Code:** tras revisar, elige explícitamente `.claude/skills/` del proyecto o `~/.claude/skills/`. Consulta [documentación oficial](https://code.claude.com/docs/en/skills) para descubrir/verificar skills en tu versión; no se presupone un comando `config list-skills`.
- **Hermes Agent:** consulta [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) para el directorio del perfil o directorios externos. No copies a otro perfil por defecto.
- Los recursos de cada skill de marketing enlazan solo dentro de su carpeta y se pueden copiar por separado. Los cuatro orquestadores históricos requieren revisión propia de referencias, scripts y dependencias.

Ningún test de este repositorio instala en una configuración activa ni confirma compatibilidad funcional de todos los runtimes.

## Cómo usarlas

1. Elige **una tarea concreta**, lee `SKILL.md` y reúne sus entradas obligatorias. Los ejemplos no rellenan los huecos del caso real.
2. Entrega solo fuentes minimizadas y autorizadas. Separa permisos de diseño de permisos de ejecución.
3. Pide explícitamente la skill y una salida conforme a `assets/salida.md`.
4. Revisa fuentes, cálculo, límites y **Estado final**. `Bloqueado` es un resultado válido; no autoriza completar datos por intuición.

Ejemplo de encargo:

> Usa `g4u-plan-medicion`. Te aportaré objetivo, recorrido, población, ventana y restricciones. Define también los eventos del denominador y prueba con datos sintéticos qué pasa con dos errores en una misma sesión. No implementes tracking ni atribuyas comprensión a una finalización.

Encadenamientos posibles, **sin ejecución automática**:

- `plan-investigacion` → `guion-entrevista` → investigación humana autorizada → `sintesis-entrevistas` → `posicionamiento`.
- `brief-seo` → `contenido-con-fuentes` → `edicion-texto` → revisión humana. Para stack o investigación SEO, evalúa primero `g4u-seo`: no le atribuyas esas capacidades al brief.
- `ficha-experimento` → diseño revisado → implementación autorizada aparte → `plan-medicion` → datos reales validados → `informe-resultados`.

## Pruebas y límites

La suite offline cubre inventario **25/25**, contratos y ejemplos, casos escritos, portabilidad, licencias, patrones de privacidad, copia aislada y regresiones de vídeo, experimento, entrevista, encuesta, calendario, campaña y medición. También inyecta fallos de instalación para verificar rollback y preservación de contenido existente.

**Qué no demuestra:** no ejecuta prompts con un modelo, no valida impacto comercial, no prueba consentimiento real y no certifica ausencia absoluta de datos sensibles. Los casos de aceptación son respuestas esperadas; los oráculos numéricos solo verifican cálculos y reglas del ejemplo. No confundirlos con evaluaciones LLM ni resultados de clientes. Consulta [método y pruebas](docs/marketing/VERIFICACION.md) y [trazabilidad de mejoras](docs/marketing/MEJORAS.md).

## Principios y contribución

Conservamos la filosofía del proyecto: **orquestar antes de duplicar**, observar antes de prescribir, entregar handoffs antes de ejecutar cambios y declarar dependencias sin asumir el contexto del cliente. Una skill documental no necesita inventar conectores para ser útil.

Abre un issue o PR siguiendo [CONTRIBUTING.md](CONTRIBUTING.md): caso de uso concreto, evidencia para reglas nuevas, ejemplo completo, caso negativo, pruebas y atribución. No subir secretos, notas de clientes ni capturas privadas. Los scripts o integraciones nuevas necesitan revisión separada de efectos, credenciales y coste.

## Licencia y trabajos relacionados

MIT según [LICENSE](LICENSE). Las 25 skills incluyen licencia portable. Cinco conservan atribución MIT de **Single Grain** por adaptaciones del repositorio de Eric Siu; véanse [avisos de terceros](THIRD_PARTY_NOTICES.md), [procedencia](docs/marketing/PROCEDENCIA.md) y [fuentes fijadas](docs/marketing/SOURCES.json). MIT sobre el procedimiento no concede permisos sobre materiales que un usuario aporte después.

- [Anthropic Skills](https://github.com/anthropics/skills)
- [AY Skills](https://github.com/walidboulanouar/Ay-Skills)
- [AgriciDaniel claude-seo](https://github.com/AgriciDaniel/claude-seo)
- [Corey Haines](https://github.com/coreyhaines/)
- [Eric Siu / ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills)

## Growth4U

Consultoría de growth con base en Madrid, orientada a startups y scale-ups B2B SaaS, fintech e industrias reguladas. [Web](https://growth4u.io) · [Alfonso Sainz de Baranda](https://linkedin.com/in/alfonsosainzdebaranda) · [Más herramientas](https://github.com/Growth4U-systems).
