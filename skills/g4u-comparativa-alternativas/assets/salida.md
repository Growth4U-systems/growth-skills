# Contrato: Comparativa de alternativas con evidencia

## Entradas y ausencias
Lista cada entrada obligatoria por su nombre, valor y estado recibido/ausente/contradictorio. Enumera las opcionales con valor o «no aportado». No trates un permiso pendiente como autorización.

## Evidencia y alcance
Mapa de IDs de fuente → extracto/ubicación, fecha o «no aportado», alcance y limitación. No usar el ejemplo como evidencia del caso real.

## Resultado
Entrega al menos una fila si las entradas lo permiten; cero filas y razón explícita si Bloqueado. Mantén exactamente estas columnas, sin celdas vacías:

| Campo | Tipo y regla |
|---|---|
| ID | texto único estable dentro de la entrega |
| Criterio | texto explícito; no vacío |
| A | texto explícito; no vacío |
| B | texto explícito; no vacío |
| Fuente | uno o más IDs existentes en Evidencia y alcance; no referencias inventadas |
| Decisión limitada | texto explícito; no vacío |

Los IDs de salida no se repiten. Las fuentes citadas existen en el mapa. Una condición pendiente no se convierte en hecho aprobado.

## Decisiones y límites
Explica selección, alternativa descartada, razón y qué información cambiaría la decisión. Distingue hechos, hipótesis y propuestas. En bloqueo, no des una recomendación dependiente del dato ausente.

## Validación humana
- Cada celda diferencia no aportado y no disponible
- Fuentes comparables en fecha y tarea
- Recomendación reversible ante nueva evidencia

## Estado final
- Estado: exactamente «Borrador para revisión humana» o «Bloqueado».
- Datos ausentes: lista explícita o «ninguno obligatorio; opcionales detalladas arriba».
- Incertidumbres: límites de evidencia y permisos; no «ninguna» si hay hipótesis.
- Validación pendiente: tarea, rol genérico responsable y condición para avanzar.
- Acción ejecutada: «ninguna acción externa»; una propuesta no es ejecución.
