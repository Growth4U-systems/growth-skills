# Ejemplo completo: Plan de onboarding hacia una primera tarea

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Producto y capacidad aprobada:** Plantilla semanal manual; no decide prioridades
- **Audiencia inicial:** Principiantes
- **Tarea de primer valor:** Ubicar una tarea ficticia y guardarla en una semana
- **Pasos actuales:** Crear cuenta → completar perfil → elegir semana → añadir tarea → guardar
- **Criterio observable de tarea completada:** Tarea de demostración visible después de guardar y recargar; no retención
- **Restricciones de privacidad:** Propuesta sin cuentas reales ni identidad; medición agregada solo con aprobación

Opcionales:
- **Barreras observadas anonimizadas:** no aportado
- **Funciones que pueden aplazarse:** no aportado

## Evidencia y alcance
- **P1:** Capacidad ficticia de guardar y recuperar una tarea; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **F1:** Flujo actual aportado; perfil no necesario para la tarea didáctica; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Estado / paso | Texto o decisión | Acción siguiente | Fuente |
|---|---|---|---|---|
| O1 | Perfil | Aplazar en demostración, pues no es requisito de F1 | Elegir semana | F1 |
| O2 | Vacío | Aún no hay tareas. Añade una tarea ficticia para ver tu semana | Añadir tarea | P1 |
| O3 | Fallo de guardado | No se ha guardado. Reintenta o vuelve a la tarea sin afirmar éxito | Reintentar guardado; ayuda si persiste | P1 |
| O4 | Éxito | Tarea guardada; comprueba que aparece al recargar | Verificar persistencia | P1 |

## Decisiones y límites
El primer valor exige persistencia, no solo pulsar guardar. No se implementó flujo ni se midió retención; la cuenta solo podría aplazarse en un entorno de demostración que no la requiera.

## Validación humana
- Pendiente: Fallo no conduce a mensaje de éxito
- Pendiente: No quitar requisitos reales por optimizar pasos
- Pendiente: Resultado visible después de recargar, no solo evento de clic

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
