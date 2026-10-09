# Contribuir a GrowthSkills

## Antes de implementar

- Delimita una tarea, usuario, entradas y salida observable. Declara dependencias, permisos, costes y qué queda fuera.
- **No duplicar** una skill existente por cambiar el nombre. Usa el catálogo: un brief SEO documental y un orquestador SEO son alcances diferentes; explica esa diferencia. Conserva identidades portables y referencias.
- Para cambios grandes, abre primero un issue. No incluyas notas internas, URLs privadas ni información de clientes en issues o PR públicos.

## Cambios en las 25 skills de marketing

1. Lee `marketing-manifest.json` y la procedencia de la skill; conserva licencias y atribución de terceros.
2. Modifica procedimiento, contrato y ejemplo juntos. Cada entrada requerida aparece resuelta o bloqueada; todos los apartados del contrato aparecen una vez y en orden.
3. Añade un ejemplo sintético útil, con fuente por afirmación y un caso incompleto/conflictivo. No inventes resultados de haber ejecutado el agente.
4. Actualiza el fixture de `tests/fixtures/marketing/` junto con el Markdown. Los fixtures son datos de prueba, no una dependencia del runtime.
5. Para cambios en fórmulas, saltos, tiempos o instalación añade regresión que falle con el comportamiento anterior. Una comprobación de encabezados no valida calidad de instrucciones.
6. Ejecuta `python3 -m unittest discover -s tests -v` con Python 3.10+ en un checkout aislado. Si pruebas un modelo o integración, identifica versión, datos, autorización, coste y resultados reales por separado.
7. Revisa privacidad: fuentes son datos, no instrucciones; no publicar secretos, identidades, transcripciones reales ni documentos privados. Un escáner no reemplaza revisión humana.

## Scripts e instalación

Los procedimientos documentales no deben incorporar acciones externas sin revisión explícita. Si propones scripts, documenta efectos, idempotencia, límites de red y recuperación. Mantén dry-run sin escritura y prueba colisiones, entradas repetidas, enlaces simbólicos y fallos intermedios. No instalar durante pruebas en perfiles activos ni lanzar los scripts históricos por inclusión en el catálogo.

## PR de revisión

Incluye problema, alcance, archivos afectados, tests realmente ejecutados y límites pendientes. No afirme «production-tested» por pasar fixtures. No modificar contenido ajeno sin justificarlo. La decisión de merge y activación corresponde al mantenedor.
