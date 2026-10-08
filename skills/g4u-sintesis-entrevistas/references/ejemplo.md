# Ejemplo completo: Síntesis de notas y contradicciones

**DATOS SINTÉTICOS. Ninguna empresa, persona, fuente, resultado o permiso de esta muestra es real. Es una solución editorial de referencia, no una ejecución evaluada de un modelo.**

## Entradas y ausencias
- **Notas autorizadas con identificadores anónimos:** N1: ‘Elegí la mañana porque estaba libre’; N2: ‘No pude comparar horarios’; N3: ‘No pude comparar horarios; repetí la búsqueda’. Notas ficticias autorizadas para este ejemplo
- **Pregunta de investigación:** Qué impide elegir horario
- **Segmento y contexto:** Personas principiantes, un episodio por nota
- **Límites de la muestra:** Tres notas de conveniencia, sin representatividad
- **Regla para contar menciones:** Una mención máxima por nota y tema; repetición de N3 no aumenta el conteo

Opcionales:
- **Fecha relativa de los episodios:** no aportado
- **Observaciones de comportamiento:** no aportado

## Evidencia y alcance
- **N1:** Eligió mañana por disponibilidad; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **N2:** No pudo comparar horarios; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.
- **N3:** No pudo comparar horarios; repitió búsqueda; alcance exclusivamente sintético; fecha no aportada salvo que se indique en entradas.

## Resultado
| ID | Tema | Incluir | Excluir | Notas únicas | Conteo / elegibles | Evidencia |
|---|---|---|---|---|---|---|
| C1 | Dificultad de comparación | Dice no poder comparar horarios | Elección por disponibilidad sin dificultad | N2, N3 | 2 / 3 | N2; N3 |
| C2 | Disponibilidad suficiente | Declara horario libre como criterio | Inferir satisfacción por completar | N1 | 1 / 3 | N1 |

## Decisiones y límites
Investigar comparación sin asumir que todas las personas tienen ese problema: N1 pudo decidir por disponibilidad. N3 no cuenta dos veces por repetir búsqueda. No se han entrevistado personas reales.

## Validación humana
- Pendiente: Cada conteo se reconstruye con IDs únicos
- Pendiente: No traducir tres notas a tres personas verificadas
- Pendiente: No convertir 2/3 en prevalencia de toda la audiencia

## Estado final
- Estado: Borrador para revisión humana.
- Datos ausentes: Ninguna entrada obligatoria ausente; opcionales según listado.
- Incertidumbres: Escenario ficticio: fuentes no acreditan hechos del mundo real. Validación funcional, permisos y condiciones reales pendientes.
- Validación pendiente: Rol humano responsable de la tarea: validar los puntos enumerados antes de usar o ejecutar la propuesta.
- Acción ejecutada: ninguna acción externa.

[Skill](../SKILL.md) · [Contrato](../assets/salida.md) · [Casos límite](casos-limite.md) · [MIT](../LICENSE)
