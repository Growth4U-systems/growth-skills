# Ejemplo completo: Calendario editorial por dependencias

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Piezas aprobadas para planificar:** P1: guía breve; P2: correo de ayuda; ambas aprobadas para planificar, no para publicar
- **Ventana de trabajo:** Semana de lunes a viernes, sin fechas reales
- **Capacidad disponible por rol genérico:** Redacción: 4 horas; revisión: 2 horas; publicación: 1 hora; cada rol declara disponibilidad
- **Dependencias:** P1: redactar 2h → revisar 1h → publicar 0,5h. P2: redactar 2h → revisar 1h → publicar 0,5h; P2 depende de aprobación P1
- **Criterio de aprobación:** Revisión funcional y editorial explícita por pieza antes de publicación

Opcionales:
- **Frecuencia máxima por canal:** no aportado
- **Restricciones de disponibilidad:** no aportado

## Evidencia y alcance
- **C1:** Capacidad aportada: redacción 4h, revisión 2h, publicación 1h; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **D1:** Dependencias y estimaciones aportadas por pieza; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **A1:** Aprobación de contenido todavía pendiente, distinta de permiso para planificar; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Pieza | Secuencia relativa | Redacción h | Revisión h | Publicación h | Fuente | Gate |
|---|---|---|---|---|---|---|---|
| P1 | Guía breve | Lun redactar → mar revisar → mié publicar si aprobada | 2 | 1 | 0.5 | C1; D1 | A1 pendiente |
| P2 | Correo ayuda | Mié redactar tras aprobación P1 → jue revisar → vie publicar si aprobado | 2 | 1 | 0.5 | C1; D1 | A1 pendiente |

## Decisiones y límites
Carga total por rol: 4h, 2h y 1h; igual a capacidad aportada. No hay margen de contingencia. Si P1 no se aprueba, P2 se desplaza; no se inventa disponibilidad de revisión ni fecha segura.

## Validación humana
- Pendiente: Sumas por rol no exceden capacidad
- Pendiente: P2 nunca precede aprobación P1
- Pendiente: Revisar contingencia y aprobación antes de comprometer fechas

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
