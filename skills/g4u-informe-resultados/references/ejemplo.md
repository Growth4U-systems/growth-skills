# Ejemplo completo: Informe de resultados y decisiones limitadas

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Objetivo y pregunta:** Describir cambio de finalización sin atribuirlo a campaña
- **Datos agregados con fuente identificada:** A1: ventana A 20 éxitos / 100 sesiones; A2: ventana B 30 / 100; agregados sintéticos
- **Definiciones de métricas:** Finalización = sesiones elegibles que completan / sesiones elegibles; porcentaje
- **Ventanas comparadas y elegibilidad:** Dos semanas completas; misma elegibilidad y definición; no experimento aleatorio
- **Cambios o incidentes conocidos:** No hay incidentes conocidos según declaración; esto no prueba ausencia de cambios no registrados

Opcionales:
- **Umbral operativo acordado previamente:** no aportado
- **Contexto cualitativo autorizado:** no aportado

## Evidencia y alcance
- **A1:** 100 sesiones elegibles, 20 con finalización; agregado sintético; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **A2:** 100 sesiones elegibles, 30 con finalización; agregado sintético; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **C1:** Ventanas comparables descriptivamente, sin control causal; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Métrica | Cálculo | Resultado | Evidencia | Interpretación |
|---|---|---|---|---|---|
| R1 | Tasa A | 100 × 20 / 100 | 20% | A1 | Descriptiva |
| R2 | Tasa B | 100 × 30 / 100 | 30% | A2 | Descriptiva |
| R3 | Diferencia | 30% − 20% | 10 puntos porcentuales | A1; A2 | No 10% relativo |
| R4 | Cambio relativo | 100 × (30 − 20) / 20 | 50% | A1; A2 | No demuestra efecto causal |

## Decisiones y límites
La finalización observada sube de 20% a 30%. No se sabe por qué. Revisar definiciones y cambios concurrentes antes de decidir; mantener seguimiento descriptivo, no declarar ganadora una campaña.

## Validación humana
- Pendiente: Datos y denominadores válidos por ventana
- Pendiente: Distinguir puntos porcentuales y porcentaje relativo
- Pendiente: Base cero o ventana incompatible impiden variación relativa interpretable

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
