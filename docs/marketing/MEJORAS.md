# Mejoras trazables a la auditoría

Fuente fijada: `4d54e83f25e37b2ee467f6cd216ec70211d1e228`. El informe privado permanece fuera del repositorio; esta matriz conserva solo hallazgos técnicos del material público y sus correcciones. No es una evaluación LLM.

## Correcciones comunes

- Contratos y ejemplos conservan seis apartados, incluido Estado final.
- Entradas requeridas resueltas explícitamente; no decisiones rellenadas por defecto.
- Métodos específicos, fuentes con ID y casos incompletos/conflictivos por skill.
- Copia aislada con preflight de duplicados, staging y rollback de errores capturados.
- Licencia y procedencia portables; límites de atribución y privacidad explícitos.

## Por skill

### 01 · g4u-plan-cortes-video

**Hallazgo de partida:** El paso de revisar el vídeo original queda dentro del procedimiento aunque las entradas obligatorias solo exigen transcripción. La muestra declara que no hay vídeo y entrega un corte con revisión pendiente: es razonable para preproducción, pero la frontera entre paso ejecutable y comprobación humana no está inequívocamente expresada.

**Criterio de mejora:** Convertir ese paso en gate externo de aprobación; entregar explícitamente estado Borrador y nunca afirmar que se revisó audio o imagen. Añadir muestra con marcas faltantes y cortes que perderían una negación.

**Implementación para revisar:** [procedimiento](../../skills/g4u-plan-cortes-video/SKILL.md), [contrato](../../skills/g4u-plan-cortes-video/assets/salida.md), [ejemplo](../../skills/g4u-plan-cortes-video/references/ejemplo.md), [casos límite](../../skills/g4u-plan-cortes-video/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-plan-cortes-video.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 02 · g4u-brief-seo

**Hallazgo de partida:** El procedimiento exige revisar solapamientos aunque páginas existentes son opcionales. La muestra marca esas páginas no aportadas y no inventa canibalización: correcto. Falta un criterio explícito para separar brief redactable de investigación pendiente cuando hay consultas de intenciones mixtas.

**Criterio de mejora:** Añadir un caso con consulta ambigua y dos fuentes fechadas; mostrar qué decisión queda suspendida y qué se puede redactar. Incluir evidencia por sección y matriz existente/nueva, sin exigir APIs.

**Implementación para revisar:** [procedimiento](../../skills/g4u-brief-seo/SKILL.md), [contrato](../../skills/g4u-brief-seo/assets/salida.md), [ejemplo](../../skills/g4u-brief-seo/references/ejemplo.md), [casos límite](../../skills/g4u-brief-seo/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-brief-seo.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 03 · g4u-contenido-con-fuentes

**Hallazgo de partida:** Fecha de vigencia es opcional, mientras el procedimiento pide comprobar fecha. Esto permite redactar con hechos potencialmente caducados si no se deja una suspensión explícita para afirmaciones sensibles al tiempo. El ejemplo funcional simple no prueba el caso de fuentes contradictorias que la skill menciona.

**Criterio de mejora:** Incluir tabla fuente/fecha/alcance/afirmación y un ejemplo conflictivo: conservar ambas versiones o excluir la afirmación, sin decidir verdad por orden de aparición. Completar el Estado final común.

**Implementación para revisar:** [procedimiento](../../skills/g4u-contenido-con-fuentes/SKILL.md), [contrato](../../skills/g4u-contenido-con-fuentes/assets/salida.md), [ejemplo](../../skills/g4u-contenido-con-fuentes/references/ejemplo.md), [casos límite](../../skills/g4u-contenido-con-fuentes/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-contenido-con-fuentes.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 04 · g4u-email-revision-humana

**Hallazgo de partida:** La muestra resuelve un correo de ayuda y deja permiso/canal bloqueados correctamente. No hay fallo sustantivo adicional verificado; la regla de legitimidad es general y no debe venderse como validación legal o de consentimiento.

**Criterio de mejora:** Añadir casos de finalidad incompatible y permiso retirado, distinguir condiciones para redactar de condiciones para usar el texto, y definir longitud o variantes cuando se aporten.

**Implementación para revisar:** [procedimiento](../../skills/g4u-email-revision-humana/SKILL.md), [contrato](../../skills/g4u-email-revision-humana/assets/salida.md), [ejemplo](../../skills/g4u-email-revision-humana/references/ejemplo.md), [casos límite](../../skills/g4u-email-revision-humana/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-email-revision-humana.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 05 · g4u-ficha-experimento

**Hallazgo de partida:** Contradicción concreta: métrica con numerador/denominador, ventana, instrumentación y regla de decisión son entradas obligatorias, y se ordena detenerse si faltan. Las entradas de la muestra no las proporcionan; el resultado introduce una ventana de 14 días, umbral de 5 puntos, eventos y asignación. Están etiquetados como propuestas sintéticas, por lo que no son resultados falsos, pero la muestra no cumple el bloqueo que enseña la skill.

**Criterio de mejora:** Elegir una política consistente: aportar esos parámetros en Entradas resueltas y mantener el bloqueo, o hacerlos campos a proponer pendientes de aprobación. Añadir ejemplo negativo con datos ausentes. No convertir el umbral de 5 puntos en recomendación universal.

**Implementación para revisar:** [procedimiento](../../skills/g4u-ficha-experimento/SKILL.md), [contrato](../../skills/g4u-ficha-experimento/assets/salida.md), [ejemplo](../../skills/g4u-ficha-experimento/references/ejemplo.md), [casos límite](../../skills/g4u-ficha-experimento/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-ficha-experimento.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 06 · g4u-plan-investigacion

**Hallazgo de partida:** El ejemplo cierra al tener una observación y una explicación por sesión; ese criterio indica completitud de la recogida, no que haya evidencia suficiente para elegir entre guías. La distinción existe parcialmente mediante no generalizar, pero se puede explicitar un resultado inconcluso aun completando ambas sesiones.

**Criterio de mejora:** Separar cierre logístico, suficiencia para decisión y regla de continuación cuando las observaciones discrepan. Añadir ejemplo de dos sesiones que apuntan en sentidos distintos.

**Implementación para revisar:** [procedimiento](../../skills/g4u-plan-investigacion/SKILL.md), [contrato](../../skills/g4u-plan-investigacion/assets/salida.md), [ejemplo](../../skills/g4u-plan-investigacion/references/ejemplo.md), [casos límite](../../skills/g4u-plan-investigacion/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-plan-investigacion.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 07 · g4u-guion-entrevista

**Hallazgo de partida:** No se observa pregunta inductiva importante en la muestra. El cierre permite pedir que no se conserven respuestas, pero un registro sin identidad necesita un mecanismo para localizar la contribución a retirar; ese mecanismo no está desarrollado.

**Criterio de mejora:** Definir retirada durante la sesión o código aleatorio entregado al participante y plazo de retención; no solicitar identidad innecesaria. Añadir reparto orientativo de los 15 minutos y pregunta de recuperación.

**Implementación para revisar:** [procedimiento](../../skills/g4u-guion-entrevista/SKILL.md), [contrato](../../skills/g4u-guion-entrevista/assets/salida.md), [ejemplo](../../skills/g4u-guion-entrevista/references/ejemplo.md), [casos límite](../../skills/g4u-guion-entrevista/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-guion-entrevista.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 08 · g4u-sintesis-entrevistas

**Hallazgo de partida:** N1 describe que alguien agrupó, no que agrupar le ayudara. La formulación del resultado «ayuda a estructurar el relato» es una interpretación ligera que conviene etiquetar, ya que la skill exige separar observación literal e interpretación. No se afirma productividad ni una mejora causal.

**Criterio de mejora:** Sustituir por «N1 relata que agrupó antes de priorizar» y dejar utilidad como hipótesis. Añadir varias notas de una misma persona para ejercitar deduplicación.

**Implementación para revisar:** [procedimiento](../../skills/g4u-sintesis-entrevistas/SKILL.md), [contrato](../../skills/g4u-sintesis-entrevistas/assets/salida.md), [ejemplo](../../skills/g4u-sintesis-entrevistas/references/ejemplo.md), [casos límite](../../skills/g4u-sintesis-entrevistas/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-sintesis-entrevistas.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 09 · g4u-encuesta-diagnostico

**Hallazgo de partida:** Q3 pregunta por «ese momento» a todas las personas, aunque Q1 permita no haber organizado tareas. Solo se explicita omitir Q2 al responder no; tampoco se define recorrido de prefiero no responder. Puede producir una respuesta sin episodio de referencia.

**Criterio de mejora:** Especificar árbol: sí → Q2/Q3; no o prefiero no responder → cierre o pregunta alternativa no presupuesta. Declarar selección única en Q2 y permitir empates si no se puede elegir una sola dificultad.

**Implementación para revisar:** [procedimiento](../../skills/g4u-encuesta-diagnostico/SKILL.md), [contrato](../../skills/g4u-encuesta-diagnostico/assets/salida.md), [ejemplo](../../skills/g4u-encuesta-diagnostico/references/ejemplo.md), [casos límite](../../skills/g4u-encuesta-diagnostico/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-encuesta-diagnostico.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 10 · g4u-comparativa-alternativas

**Hallazgo de partida:** La muestra trata correctamente la lista manual y el esfuerzo desconocido. No se encuentra defecto sustantivo adicional; falta mostrar qué hacer con fichas de fechas distintas o criterios no comparables.

**Criterio de mejora:** Añadir fuente/fecha por celda y ejemplo de comparación suspendida por unidades o planes diferentes. Mantener costes desconocidos visibles.

**Implementación para revisar:** [procedimiento](../../skills/g4u-comparativa-alternativas/SKILL.md), [contrato](../../skills/g4u-comparativa-alternativas/assets/salida.md), [ejemplo](../../skills/g4u-comparativa-alternativas/references/ejemplo.md), [casos límite](../../skills/g4u-comparativa-alternativas/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-comparativa-alternativas.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 11 · g4u-posicionamiento

**Hallazgo de partida:** No hay defecto específico demostrado: la necesidad se etiqueta hipotética y se invita a comprobar si la alternativa actual basta. La muestra no tensiona el método con segmentos de necesidades incompatibles.

**Criterio de mejora:** Añadir segmento excluido con necesidad incompatible y una tabla diferencia/prueba/valor supuesto/condición de rechazo. No convertir beneficios plausibles en posicionamiento validado.

**Implementación para revisar:** [procedimiento](../../skills/g4u-posicionamiento/SKILL.md), [contrato](../../skills/g4u-posicionamiento/assets/salida.md), [ejemplo](../../skills/g4u-posicionamiento/references/ejemplo.md), [casos límite](../../skills/g4u-posicionamiento/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-posicionamiento.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 12 · g4u-matriz-mensajes

**Hallazgo de partida:** El procedimiento dice que cada respuesta termina con una acción proporcionada. La segunda respuesta de la matriz solo niega predicción/decisión y no incluye acción; la acción global posterior no cumple literalmente la condición por respuesta.

**Criterio de mejora:** Añadir columna de siguiente acción por fila o cambiar la instrucción a una acción global. Para necesidad incompatible, permitir recomendar no continuar en vez de forzar CTA.

**Implementación para revisar:** [procedimiento](../../skills/g4u-matriz-mensajes/SKILL.md), [contrato](../../skills/g4u-matriz-mensajes/assets/salida.md), [ejemplo](../../skills/g4u-matriz-mensajes/references/ejemplo.md), [casos límite](../../skills/g4u-matriz-mensajes/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-matriz-mensajes.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 13 · g4u-mapa-contenidos

**Hallazgo de partida:** La ficha B remite a una sección de prioridad manual que no se explicita en la descripción de guía A. Puede ser una sección prevista, no un enlace roto comprobado; conviene que las dependencias señalen pieza y sección concretas antes de aprobar el mapa.

**Criterio de mejora:** Dar IDs a piezas y secciones, marcar destino propuesto/no creado y comprobar que la cobertura prometida existe. Mantener Q2 explícitamente pendiente.

**Implementación para revisar:** [procedimiento](../../skills/g4u-mapa-contenidos/SKILL.md), [contrato](../../skills/g4u-mapa-contenidos/assets/salida.md), [ejemplo](../../skills/g4u-mapa-contenidos/references/ejemplo.md), [casos límite](../../skills/g4u-mapa-contenidos/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-mapa-contenidos.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 14 · g4u-calendario-editorial

**Hallazgo de partida:** Capacidad por rol es obligatoria. La entrada de la muestra solo define redacción y revisión, mientras la salida asigna decisión al rol Aprobación el día 5 sin declarar su disponibilidad. La frase de autocomprobación de todas las entradas no resuelve ese vacío.

**Criterio de mejora:** Añadir capacidad y disponibilidad del aprobador en la entrada o dejar la decisión con fecha pendiente. Incorporar caso con revisión rechazada que retorna a redacción y consume capacidad.

**Implementación para revisar:** [procedimiento](../../skills/g4u-calendario-editorial/SKILL.md), [contrato](../../skills/g4u-calendario-editorial/assets/salida.md), [ejemplo](../../skills/g4u-calendario-editorial/references/ejemplo.md), [casos límite](../../skills/g4u-calendario-editorial/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-calendario-editorial.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 15 · g4u-reutilizacion-activo

**Hallazgo de partida:** La ficha se vincula a A1 y el checklist a A1/A2, y se conserva la limitación manual. No hay fallo específico demostrado. El ejemplo deja derechos reales sin acreditar porque es sintético; esto no es una licencia para reutilizar un activo real sin permiso.

**Criterio de mejora:** Separar permiso para analizar, transformar y distribuir; añadir estado por derivado y un ejemplo descartado por perder contexto. No exigir permisos reales para usar la muestra sintética del propio kit.

**Implementación para revisar:** [procedimiento](../../skills/g4u-reutilizacion-activo/SKILL.md), [contrato](../../skills/g4u-reutilizacion-activo/assets/salida.md), [ejemplo](../../skills/g4u-reutilizacion-activo/references/ejemplo.md), [casos límite](../../skills/g4u-reutilizacion-activo/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-reutilizacion-activo.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 16 · g4u-brief-campana

**Hallazgo de partida:** El ejemplo busca que lectores comprendan grupos pero mide completar una guía. La finalización es un proxy de avance, no evidencia de comprensión; no se explicita esa limitación en la sección de medición.

**Criterio de mejora:** Etiquetar finalización como proxy e incluir tarea de comprensión observable, o cambiar objetivo a finalización. Especificar ventana/denominador para la comprobación de comprensión sin identificar lectores.

**Implementación para revisar:** [procedimiento](../../skills/g4u-brief-campana/SKILL.md), [contrato](../../skills/g4u-brief-campana/assets/salida.md), [ejemplo](../../skills/g4u-brief-campana/references/ejemplo.md), [casos límite](../../skills/g4u-brief-campana/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-brief-campana.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 17 · g4u-estructura-landing

**Hallazgo de partida:** La muestra conserva límites y no finge destino real. No hay fallo específico confirmado; accesibilidad está como opcional y no se convierte en criterios concretos de estructura textual.

**Criterio de mejora:** Añadir jerarquía H1/H2 sugerida, texto de enlace comprensible aislado y checklist de condiciones de oferta. Mantener renderizado, contraste y navegación como verificaciones posteriores.

**Implementación para revisar:** [procedimiento](../../skills/g4u-estructura-landing/SKILL.md), [contrato](../../skills/g4u-estructura-landing/assets/salida.md), [ejemplo](../../skills/g4u-estructura-landing/references/ejemplo.md), [casos límite](../../skills/g4u-estructura-landing/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-estructura-landing.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 18 · g4u-revision-conversion

**Hallazgo de partida:** La muestra demuestra correctamente tres cambios textuales y excluye contraste/responsive/velocidad. No se confirma un defecto sustantivo; el plan de validación no incluye prioridad por riesgo o dependencia entre cambios.

**Criterio de mejora:** Añadir orden cualitativo: primero afirmación engañosa, después claridad de CTA, después preferencia editorial. No convertir este orden en scoring o promesa de uplift.

**Implementación para revisar:** [procedimiento](../../skills/g4u-revision-conversion/SKILL.md), [contrato](../../skills/g4u-revision-conversion/assets/salida.md), [ejemplo](../../skills/g4u-revision-conversion/references/ejemplo.md), [casos límite](../../skills/g4u-revision-conversion/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-revision-conversion.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 19 · g4u-edicion-texto

**Hallazgo de partida:** El ejemplo retira productividad no demostrada y aclara manualidad de forma correcta. No hay defecto adicional confirmado. Si dos hechos autorizados se contradicen, el caso límite pide no inventar pero no muestra cómo devolver una edición parcial.

**Criterio de mejora:** Añadir muestra con un término obligatorio y fuentes incompatibles; mantener texto no afectado, señalar bloqueo factual en la oración afectada y registrar cambios completos.

**Implementación para revisar:** [procedimiento](../../skills/g4u-edicion-texto/SKILL.md), [contrato](../../skills/g4u-edicion-texto/assets/salida.md), [ejemplo](../../skills/g4u-edicion-texto/references/ejemplo.md), [casos límite](../../skills/g4u-edicion-texto/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-edicion-texto.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 20 · g4u-brief-recurso-descargable

**Hallazgo de partida:** La muestra propone un ejercicio y no convierte respuestas sintéticas en testimonios: correcto. No demuestra efectividad ni desarrolla criterios de accesibilidad o comprensión para formatos distintos del texto.

**Criterio de mejora:** Precisar qué observar, qué errores implican revisar instrucciones y qué evidencia mínima aceptar para distribución. Añadir caso con necesidad no sustentada que debe bloquearse.

**Implementación para revisar:** [procedimiento](../../skills/g4u-brief-recurso-descargable/SKILL.md), [contrato](../../skills/g4u-brief-recurso-descargable/assets/salida.md), [ejemplo](../../skills/g4u-brief-recurso-descargable/references/ejemplo.md), [casos límite](../../skills/g4u-brief-recurso-descargable/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-brief-recurso-descargable.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 21 · g4u-secuencia-bienvenida

**Hallazgo de partida:** El segundo mensaje depende de no haber completado la ayuda, pero la entrada no especifica una señal autorizada para conocerlo. El ejemplo no afirma haberlo medido; queda un vacío de operacionalización, no un seguimiento oculto ejecutado.

**Criterio de mejora:** Definir señal voluntaria mínima o estado desconocido que bloquee automatización; no convertir falta de dato en no completado. Mantener máximo dos contactos y validación separada de permisos.

**Implementación para revisar:** [procedimiento](../../skills/g4u-secuencia-bienvenida/SKILL.md), [contrato](../../skills/g4u-secuencia-bienvenida/assets/salida.md), [ejemplo](../../skills/g4u-secuencia-bienvenida/references/ejemplo.md), [casos límite](../../skills/g4u-secuencia-bienvenida/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-secuencia-bienvenida.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 22 · g4u-secuencia-educativa

**Hallazgo de partida:** El procedimiento del caso límite pide una prueba de comprensión por paso. El ejemplo solo propone comparar conceptos y elegir procedimiento: acciones educativas, no un criterio explícito para comprobar comprensión. Además D1/D2 no resueltas requieren una señal que aquí no se aporta.

**Criterio de mejora:** Añadir tarea de clasificación o explicación voluntaria con criterio de corrección; definir desconocido como tal y evitar inferencias por apertura de email. No convertir medición en seguimiento invisible.

**Implementación para revisar:** [procedimiento](../../skills/g4u-secuencia-educativa/SKILL.md), [contrato](../../skills/g4u-secuencia-educativa/assets/salida.md), [ejemplo](../../skills/g4u-secuencia-educativa/references/ejemplo.md), [casos límite](../../skills/g4u-secuencia-educativa/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-secuencia-educativa.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 23 · g4u-onboarding-primer-valor

**Hallazgo de partida:** La muestra añade ayuda para quien no sabe agrupar pero no una ruta concreta para un fallo al crear grupo o guardar prioridad; el procedimiento sí pide recuperación cuando hay bloqueo. No es prueba de que el producto falle, sino cobertura incompleta del flujo propuesto.

**Criterio de mejora:** Añadir estado de error, acción de reintento/ayuda y preservación del trabajo para un fallo sintético. Mantener requisitos de seguridad aunque se aplace configuración.

**Implementación para revisar:** [procedimiento](../../skills/g4u-onboarding-primer-valor/SKILL.md), [contrato](../../skills/g4u-onboarding-primer-valor/assets/salida.md), [ejemplo](../../skills/g4u-onboarding-primer-valor/references/ejemplo.md), [casos límite](../../skills/g4u-onboarding-primer-valor/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-onboarding-primer-valor.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 24 · g4u-plan-medicion

**Hallazgo de partida:** La tasa de error usa sesiones que inician ejercicio como denominador, pero los eventos propuestos solo son guia_iniciada, ejercicio_completado y ejercicio_error. No se declara un evento de inicio de ejercicio ni una regla que lo equipare a inicio de guía; el denominador no es derivable inequívocamente de lo propuesto.

**Criterio de mejora:** Añadir ejercicio_iniciado con orden y elegibilidad, o redefinir tasa de error sobre quienes inician guía y renombrar la métrica. Añadir ejemplo de evento faltante, denominador cero y duplicados.

**Implementación para revisar:** [procedimiento](../../skills/g4u-plan-medicion/SKILL.md), [contrato](../../skills/g4u-plan-medicion/assets/salida.md), [ejemplo](../../skills/g4u-plan-medicion/references/ejemplo.md), [casos límite](../../skills/g4u-plan-medicion/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-plan-medicion.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.

### 25 · g4u-informe-resultados

**Hallazgo de partida:** Los cálculos de la muestra son correctos, comprobados con Python. La validación menciona ceros pero no explicita qué hacer con variación relativa cuando la tasa base es cero: queda una condición analítica importante para desarrollar.

**Criterio de mejora:** Añadir muestra A=0 con denominador positivo: diferencia absoluta calculable, variación relativa no definida. Separar denominador cero, dato ausente y numerador cero. No etiquetar significancia sin un diseño adecuado.

**Implementación para revisar:** [procedimiento](../../skills/g4u-informe-resultados/SKILL.md), [contrato](../../skills/g4u-informe-resultados/assets/salida.md), [ejemplo](../../skills/g4u-informe-resultados/references/ejemplo.md), [casos límite](../../skills/g4u-informe-resultados/references/casos-limite.md).

**Evidencia determinista:** [fixture](../../tests/fixtures/marketing/g4u-informe-resultados.json) y suite `tests/test_marketing.py`. Las comprobaciones de coherencia no prueban comportamiento de un modelo.
