# Ejemplo completo: Secuencia de bienvenida con reglas de salida

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Finalidad y consentimiento declarado:** Entregar ayuda solicitada voluntariamente; declaración sintética, no permiso real verificado
- **Audiencia genérica:** Personas que pidieron guía de la plantilla
- **Recurso solicitado:** Guía de uso manual
- **Objetivo de la secuencia:** Acceder a la guía y resolver una duda inicial
- **Información aprobada:** P1: plantilla semanal manual, sin garantía de terminar
- **Regla de frecuencia y salida:** Máximo dos mensajes, al menos tres días entre ellos; salida inmediata por baja, recurso innecesario o ayuda completada

Opcionales:
- **Preferencias de contenido:** no aportado
- **Destino autorizado de la acción:** no aportado

## Evidencia y alcance
- **P1:** Capacidad manual aprobada; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **C1:** Solicitud declarada y límites de frecuencia; enviar requiere validación real; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Cuándo / condición | Asunto | Cuerpo | Acción | Salida prioritaria |
|---|---|---|---|---|---|
| B1 | Solicitud válida y sin baja | Tu guía de planificación manual | Aquí tienes la guía que solicitaste. La plantilla organiza una vista semanal, pero tú decides la distribución. No predice resultados. Usa el destino autorizado para consultarla. | Consultar guía | Baja o solicitud retirada: no enviar |
| B2 | ≥3 días tras B1; ayuda no completada; sin respuesta pendiente | ¿Necesitas aclarar algún paso? | Si te queda una duda sobre la distribución manual, puedes consultarla por el canal que autorizaste. Si ya terminaste, no necesitas hacer nada más. | Pedir aclaración si hace falta | Baja, objetivo cumplido o frecuencia agotada: no enviar |

## Decisiones y límites
Secuencia de dos borradores no enviados. Una baja entre B1 y B2 cancela B2 aunque estuviera planificado. La ausencia de señal no demuestra que la persona no haya aprendido; no automatizar sin regla aprobada.

## Validación humana
- Pendiente: Salida revaluada inmediatamente antes de envío
- Pendiente: No reentrada automática tras baja
- Pendiente: No seguimiento de apertura inventado

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
