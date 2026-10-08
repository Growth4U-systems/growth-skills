# Ejemplo completo: Encuesta breve de diagnóstico

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Decisión que informará la encuesta:** Elegir qué tema explicar en la ayuda de horarios
- **Audiencia y criterios de participación:** Principiantes que consideraron un taller; experiencia reciente determina las preguntas
- **Tema acotado:** Elección de horario en los últimos siete días
- **Tiempo de respuesta objetivo:** Dos minutos, pendiente de piloto
- **Reglas de privacidad y consentimiento:** Participación voluntaria, sin identidad, sin campos obligatorios; texto libre sin datos personales

Opcionales:
- **Preguntas anteriores para comparar:** no aportado
- **Canal de distribución autorizado:** no aportado

## Evidencia y alcance
- **D1:** Decisión y periodo sintéticos; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **P1:** Privacidad: se puede omitir cualquier pregunta o abandonar; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Pregunta / condición | Opciones | Destino | Evidencia |
|---|---|---|---|---|
| Q1 | ¿Intentaste elegir horario en los últimos siete días? | sí | Q2 | D1 |
| Q1-N | Respuesta Q1 | no; prefiero no responder; omitida | FIN; omitir Q2 y Q3 | P1 |
| Q2 | ¿Qué fue lo más difícil? | comparar horarios; entender duración; nada; otra; prefiero no responder; omitida | Q3 opcional en todos los casos, pues Q1 fue sí | D1; P1 |
| Q3 | ¿Qué información necesitabas en ese momento? | texto opcional sin datos personales; omitida | FIN | D1; P1 |
| FIN | Gracias; puedes cerrar sin responder más | no recoge identidad | FIN | P1 |

## Decisiones y límites
Introducción: Queremos mejorar la ayuda para elegir horario. Participar es voluntario; puedes omitir preguntas o terminar. No escribas datos personales. Q2 y Q3 solo se muestran a Q1=sí. Cuestionario diseñado, no distribuido y sin respuestas reales.

## Validación humana
- Pendiente: Recorrer sí, no, prefiero no responder y omitida en Q1
- Pendiente: Toda rama termina y nunca obliga texto libre
- Pendiente: Piloto de duración y consentimiento antes de distribución

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
