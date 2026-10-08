# Ejemplo completo: Ficha de experimento

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Problema:** Se desconoce si se entiende el botón de crear grupo
- **hipótesis:** Una etiqueta explícita podría aumentar creación respecto al control
- **población:** Sesiones consentidas de prueba; una exposición elegible por sesión
- **variante y control:** Control: Nuevo grupo; variante: Crear grupo de tareas
- **métrica primaria con numerador y denominador:** Sesiones expuestas con grupo_creado posterior / sesiones expuestas elegibles, porcentaje por brazo
- **ventana de medición:** 14 días completos desde activación; misma sesión para conversión
- **instrumentación prevista:** boton_visto y grupo_creado; asignación aleatoria persistente en sesión, clave efímera; aún no implementado
- **regla de decisión:** Diseño exploratorio aportado: +5 puntos porcentuales solo abre otra prueba; sin declarar ganador ni eficacia estadística
- **responsable humano de revisión:** Rol de revisión de producto designado para aprobar diseño, datos y privacidad

Opcionales:
- **Línea base aportada:** no aportado
- **tamaño de muestra y cálculo externo:** no aportado
- **métricas de seguridad:** no aportado
- **exclusiones:** Excluir QA previamente etiquetado y eventos duplicados
- **plan de aleatorización:** Asignación aleatoria 50/50 persistente por sesión; posible contaminación entre sesiones
- **restricciones legales o de privacidad:** Sin identidad; retención y acceso requieren aprobación

## Evidencia y alcance
- **D1:** Diseño sintético aportado completo; ventana y regla existen ANTES de la salida; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **P1:** No se aporta cálculo de potencia, línea base ni resultados; solo diseño exploratorio; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Elemento | Especificación | Evidencia |
|---|---|---|---|
| X1 | Asignación | 50/50 por sesión elegible, persistente; excluir QA previamente etiquetado | D1 |
| X2 | Métrica | 100 × sesiones con grupo_creado después de boton_visto / sesiones con boton_visto, por brazo | D1 |
| X3 | Ventana y regla | 14 días; diferencia ≥5 pp solo permite considerar otra prueba exploratoria | D1 |
| X4 | Límite | Sin potencia ni resultados: no inferencia confirmatoria ni ganador | P1 |

## Decisiones y límites
La ficha usa parámetros aportados, no los inventa. Privacidad e instrumentación requieren aprobación antes de cualquier ejecución. No se realizó experimento y no hay resultados.

## Validación humana
- Pendiente: Auditar exposición, asignación y orden antes de comparar
- Pendiente: Confirmar regla previa sin cambios oportunistas
- Pendiente: Revisar contaminación entre sesiones y cálculo externo si cambia a confirmatorio

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
