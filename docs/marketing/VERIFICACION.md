# Método de verificación

## Niveles separados

1. **Revisión estática editorial:** entradas, pasos de decisión, contratos, ejemplos, casos límite, permisos y atribución. Leer no demuestra comportamiento de un modelo.
2. **Ejecución determinista offline:** `python3 -m unittest discover -s tests -v`. Comprueba contenido y fixtures, cálculos acotados, enlaces, copia aislada, colisiones y rollback. Python 3.10+; sin paquetes externos.
3. **Casos sintéticos de aceptación:** cada `references/casos-limite.md` expresa lo que debería contestar un agente. **No se ejecutan con LLM** en esta suite. Ni los fixtures ni los oráculos numéricos son resultados de clientes.
4. **Integración real del runtime:** fuera de esta verificación. Cargar una skill en Hermes/Claude, ejecutar campañas o medir impacto requiere autorización y prueba separadas.

## Cobertura

- Identidades exactas del [manifiesto](../../marketing-manifest.json): 25 incorporadas, sin colisiones con cuatro preexistentes.
- Seis recursos portables por skill: instrucciones, contrato, ejemplo, casos límite, procedencia y licencia; fixture de prueba fuera de la carpeta instalable.
- Encabezados, campos obligatorios, filas/IDs, referencias y Estado final coinciden entre contrato, ejemplo y fixture.
- Casos sustantivos: negación y límites de un corte; parámetros previos de experimento; duración de entrevista; saltos de encuesta y salida sin respuesta; carga de calendario por rol; métrica de comprensión separada de finalización; evento del denominador; deduplicación, orden temporal, ventana y huérfanos; puntos porcentuales frente a cambio relativo.
- Instalador: dry-run sin escritura, selección repetida rechazada antes de crear destino, colisiones sin sobrescritura, copia de las 25 con comparación byte a byte, fallos inyectados en staging y commit, lock y rutas/enlaces no admitidos.
- Licencias: MIT local, aviso Single Grain en cinco adaptaciones y hash del texto de licencia pública fijado por la fuente.
- Privacidad: patrones básicos de secretos/identidades/rutas internas sobre el corpus nuevo. No es un certificado de anonimato ni una revisión legal.

## Reproducción

```bash
python3 -m unittest discover -s tests -v
```

Los tests crean sandboxes con `tempfile.TemporaryDirectory()` y los limpian al terminar. Puedes fijar `TMPDIR` a un directorio de trabajo existente y aislado. Nunca seleccionan una carpeta activa de skills.

Para validar también los comandos de usuario, sigue el dry-run y la instalación aislada del [README](../../README.md). Volver a instalar sobre el mismo destino debe fallar, no sobrescribir. Prueba el conjunto sin APIs, credenciales ni gastos.

La integración dispone de workflow CI en Python 3.10 y 3.13. Su resultado depende del SHA: consultar los checks del commit exacto, no asumir que este documento demuestra CI verde.

## Límites conocidos

- Los asserts de texto sirven como regresión, no como evaluación semántica completa. Ejemplos útiles todavía requieren lectura humana.
- El instalador revierte errores capturados, pero no ofrece atomicidad frente a apagado, terminación forzada o escritores maliciosos. Un lock abandonado necesita inspección humana; no borrarlo automáticamente.
- La suite no ejecuta ni modifica las cuatro skills históricas y no valida sus scripts, conectores o afirmaciones de compatibilidad.
- Los hashes de recursos anteriores no públicos se conservan como trazabilidad declarada. No se afirma haber recuperado esos originales.
