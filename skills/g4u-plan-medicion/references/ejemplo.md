# Ejemplo completo: Plan de medición con diccionario de métricas

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Pregunta de decisión:** Detectar dónde se atasca una demostración, sin afirmar comprensión
- **Acción objetivo y población elegible:** Finalizar ejercicio; sesiones consentidas que lo inician
- **Pasos del recorrido:** Ver guía → iniciar ejercicio → finalizar o error
- **Ventana y unidad de análisis:** Una sesión de demostración, máximo 30 minutos; unidad sesión efímera
- **Restricciones de datos:** Sin identidad, texto libre ni URL completa; agregación y retención pendientes de aprobación
- **Datos disponibles o ausentes:** No hay datos reales; solo eventos y fixture sintético para validar fórmulas

Opcionales:
- **Métricas de daño o calidad:** no aportado
- **Comparación temporal autorizada:** no aportado

## Evidencia y alcance
- **D1:** Recorrido y población sintéticos aprobados para diseño; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **P1:** Restricciones de privacidad; no implementación autorizada; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Evento / métrica | Disparo o fórmula | Deduplicación / elegibilidad | Fuente |
|---|---|---|---|---|
| E1 | guia_vista | Al mostrarse la guía en sesión consentida | Una por sesión; no es inicio de ejercicio | D1 |
| E2 | ejercicio_iniciado | Al iniciar efectivamente el ejercicio | Una por sesión; establece denominador | D1 |
| E3 | ejercicio_finalizado | Tras completar tarea, posterior a E2 | Una por sesión; excluir huérfanos y registrar incidencia | D1 |
| E4 | error_ejercicio | Error durante ejercicio iniciado | Una sesión con ≥1 error cuenta una vez en tasa | D1 |
| M1 | Finalización | 100 × sesiones iniciadas con finalización posterior / sesiones iniciadas | Misma sesión, máximo 30 minutos | D1 |
| M2 | Sesiones con error | 100 × sesiones iniciadas con ≥1 error posterior / sesiones iniciadas | Mismo denominador; múltiples errores no duplican sesión | D1 |

## Decisiones y límites
Fixture sintético: 4 sesiones ven guía; 3 inician; 2 finalizan; 1 de las iniciadas tiene dos errores y finalmente termina. Finalización = 2/3; sesiones con error = 1/3, no 2/3 ni 1/4. Ambas métricas pueden solaparse. No hay instrumentación real.

## Validación humana
- Pendiente: Cada denominador tiene evento y disparo
- Pendiente: Orden, deduplicación y huérfanos se prueban con fixture
- Pendiente: Denominador cero devuelve no calculable; permisos antes de recopilar

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
