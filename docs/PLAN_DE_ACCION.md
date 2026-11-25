# PLAN DE ACCIÓN Y GUÍA OPERATIVA PARA LA MATERIALIZACIÓN DE LA TESIS DE GRADO (UPDS)

**Postulante:** Britney Aracelly Arratia Gonzales  
**Carrera:** Ingeniería en Redes y Telecomunicaciones  
**Tutor:** Ing. Gonzalo Tarifa Rodríguez  
**Institución:** Universidad Privada Domingo Savio (UPDS), Sede Tarija  
**Título del Proyecto:** *Evaluación experimental de un prototipo de detección de anomalías de red con Zeek e Isolation Forest y respuesta automatizada en un entorno emulado de la UPDS - Tarija*  
**Período de Ejecución:** Modalidad de Grado II (7 de diciembre de 2026 – 5 de marzo de 2027)

---

## 1. DIAGNÓSTICO METODOLÓGICO Y MATRIZ DE TRANSICIÓN (PERFIL ➔ TESIS FINAL)

El perfil aprobado cuenta con una delimitación clara, rigor experimental y respaldo institucional firmado (Anexo B). Sin embargo, el paso del perfil al borrador final de la **Tesis de Licenciatura** según la Guía Oficial UPDS exige expandir la estructura, pasar de verbos en futuro a pasado/presente reflexivo, e incorporar los capítulos de desarrollo empírico y resultados.

### 1.1 Matriz de Alineación Estructural (Perfil vs. Tesis Final)

| Componente en Perfil (Aprobado) | Ubicación en Tesis Final (Guía UPDS 2026) | Requerimiento de Transformación / Expansión |
| :--- | :--- | :--- |
| **Páginas preliminares** | Portada, Dedicatoria, Agradecimientos, Resumen | Redactar Resumen estructurado (200 a 250 palabras en 1 sola página) sin viñetas de capítulos, con palabras clave (Keywords). |
| **Cap. I: Introducción y Delimitación** | **Capítulo I: Introducción** | Mantener antecedentes, delimitaciones (sustantiva, temporal, espacial), árbol de problemas/objetivos, preguntas, justificaciones. Ajustar el límite temporal al período de ejecución experimental real. |
| **Cap. II: Marco Teórico y Normativo** | **Capítulo II: Marco Teórico** | Expandir la revisión teórica y conceptual (Zeek, Isolation Forest, IEEE 802.11, WIDS, NIST SP 800-61r3, Scikit-Learn). Ordenar subapartados obligatorios: Marco Conceptual, Marco Contextual (UPDS), Marco Histórico y Marco Normativo (Pirámide de Kelsen boliviana). |
| **Cap. III: Diseño Metodológico** | **Capítulo III: Diseño Metodológico** | Describir enfoque cuantitativo, alcance explicativo-evaluativo, diseño experimental de laboratorio, operacionalización de variables y protocolo de recolección/análisis estadístico. |
| *No desarrollado en perfil* | **Capítulo IV: Diagnóstico y Caracterización del Entorno Experimental** *(Opcional/Aplicable según guía)* | **Crucial en Ingeniería:** Caracterización detallada del hardware, firmware del AP, interfaces en modo monitor, máquinas virtuales (Proxmox/GNS3), segmentación de red y topología del banco de pruebas aislado. |
| *No desarrollado en perfil* | **Capítulo V: Análisis e Interpretación de Datos / Desarrollo del Prototipo y Experimentación** | Despliegue de scripts Zeek, pipeline de extracción de features en Python, entrenamiento del modelo Isolation Forest, ejecución de las 600 corridas (20 escenarios x 30 repeticiones) y evaluación estadística (Wilcoxon, matrices de confusión, tiempos de respuesta). |
| *No desarrollado en perfil* | **Capítulo VI: Conclusiones y Recomendaciones** | Contrastación directa de hipótesis H1 y H2; conclusiones alineadas 1 a 1 con los 6 objetivos específicos; recomendaciones técnicas e institucionales. |
| **Bibliografía y Anexos** | **Bibliografía y Anexos** | Mínimo 30 fuentes bajo norma APA 7.ª edición con DOI/URL activo. Anexar scripts versionados de Git, logs crudos de muestra, fichas de laboratorio y carta de autorización de TI. |

---

## 2. PLAN DE ACCIÓN CRONOLÓGICO POR FASES E HITOS (CALENDARIO DE GRADO II)

| Fase | Fechas Clave | Actividades Técnicas y Metodológicas | Entregable / Hito UPDS |
| :--- | :--- | :--- | :--- |
| **Fase 1: Preparación del Banco y Protocolos** | 07 al 18 Dic 2026 | - Configuración física/virtual del entorno aislado (AP, switch, sensor con modo monitor, Zeek en interfaz de red dedicada).<br>- Definición exacta del formato de la ficha experimental (logging de timestamps de inicio/fin de ataques).<br>- Redacción preliminar de la estructura del Cap. IV. | **Hito 1:** Taller de análisis e interpretación de datos (12 dic). |
| **Fase 2: Despliegue del Prototipo y Pipeline** | 19 Dic 2026 al 08 Ene 2027 | - Implementación de scripts Zeek para extracción de flujos de red.<br>- Implementación de script Python/Scapy/Tshark para captura de tramas de gestión 802.11.<br>- Pipeline de fusión de características en ventanas de 60 segundos.<br>- Scripts de respuesta automatizada (iptables/eBTables/ACL API). | **Hito 2:** 1.er Informe de Control (08 ene 2027). Cap. I y II consolidados + arquitectura técnica. |
| **Fase 3: Captura de Línea Base Normal** | 21 Dic 2026 al 19 Ene 2027 | - Recolección ininterrumpida de tráfico normal (30 días) en el entorno de pruebas emulado.<br>- Verificación de estabilidad y almacenamiento seguro de logs/pcaps. *(Se corre en paralelo con Fases 2 y 4)*. | Dataset de tráfico normal propio (Línea Base). |
| **Fase 4: Entrenamiento, Calibración y Piloto** | 11 al 29 Ene 2027 | - Limpieza y preprocesamiento de la línea base.<br>- Entrenamiento inicial de Isolation Forest (`n_estimators`, `contamination`, `max_samples`).<br>- Calibración de umbrales para la línea base de reglas estáticas.<br>- Ejecución de la prueba piloto (Escenarios 1, 4 y 17) para validar el pipeline. | **Hito 3:** 2.º Informe de Control (29 ene 2027). Cap. III y IV cerrados + prueba piloto validada. |
| **Fase 5: Batería Experimental Masiva (600 Corridas)** | 01 al 12 Feb 2027 | - Ejecución automatizada/secuencial de los 20 escenarios de ataque x 30 repeticiones.<br>- Registro sincronizado de timestamps de lanzamiento, detección y bloqueo.<br>- Almacenamiento de matrices de confusión por corrida. | Base de datos consolidada de resultados experimentales. |
| **Fase 6: Procesamiento Estadístico y Redacción Final** | 13 Feb al 05 Mar 2027 | - Tabulación de Recall, Precision, F1-Score, FPR y tiempos de respuesta.<br>- Cálculo de intervalos de confianza de Wilson (95%) y prueba no paramétrica de Wilcoxon ($p < 0.05$).<br>- Redacción de los Capítulos V y VI.<br>- Revisión de formato general APA 7.ª ed. | **Hito 4:** 3.er Informe de Control (19 feb 2027) y **Presentación Oficial de Tesis Final (05 mar 2027)**. |

---

## 3. ESQUEMA DE CONTENIDO Y ESTRUCTURA CAPITULAR DE LA TESIS FINAL

La estudiante debe estructurar su documento en Word o LaTeX bajo este índice detallado:

```text
PORTADA (Formato oficial UPDS)
PÁGINAS DE APROBACIÓN DEL TRIBUNAL Y TUTOR
DEDICATORIA Y AGRADECIMIENTOS
RESUMEN ANALÍTICO / ABSTRACT (Con Palabras Clave / Keywords)
ÍNDICE GENERAL
ÍNDICE DE TABLAS
ÍNDICE DE FIGURAS / GRÁFICOS
ÍNDICE DE ACRÓNIMOS Y SIGLAS

CAPÍTULO I: INTRODUCCIÓN Y CONTEXTUALIZACIÓN
  1.1. Antecedentes (Teórico, Metodológico y Contextual)
  1.2. Delimitación
       1.2.1. Límite Sustantivo (Temático)
       1.2.2. Límite Temporal
       1.2.3. Límite Geográfico y Espacial
  1.3. Planteamiento del Problema
       1.3.1. Contextualización del problema en redes Wi-Fi académicas
       1.3.2. Diagnóstico preliminar de la infraestructura institucional
       1.3.3. Árbol de problemas (Causas y Efectos)
  1.4. Formulación del Problema (Pregunta de investigación)
  1.5. Sistematización del Problema y Abordaje de Solución (Árbol de objetivos)
  1.6. Objetivos
       1.6.1. Objetivo General
       1.6.2. Objetivos Específicos
  1.7. Justificaciones
       1.7.1. Justificación Científica
       1.7.2. Justificación Social
       1.7.3. Justificación Económica
       1.7.4. Justificación Metodológica
       1.7.5. Viabilidad Técnica, Operativa y Ética

CAPÍTULO II: MARCO TEÓRICO, CONCEPTUAL Y NORMATIVO
  2.1. Marco Teórico
       2.1.1. Fundamentos de seguridad en redes inalámbricas IEEE 802.11
       2.1.2. Clasificación de Sistemas de Detección de Intrusiones (NIDS, WIDS, HIDS)
       2.1.3. Aprendizaje automático no supervisado en ciberseguridad
       2.1.4. Algoritmo Isolation Forest: fundamentos matemáticos y complejidad
       2.1.5. Arquitectura del analizador pasivo Zeek (Event Engine y Policy Framework)
       2.1.6. Frameworks de respuesta a incidentes (NIST SP 800-61r3 y CSF 2.0)
  2.2. Marco Conceptual (Definición de variables y glosario técnico formal)
  2.3. Marco Contextual (Infraestructura de red de referencia UPDS Sede Tarija)
  2.4. Marco Histórico (Evolución del monitoreo y la detección de anomalías)
  2.5. Marco Normativo (Pirámide de Kelsen boliviana: CPE, Ley 164, DS 1793, DS 2514, Políticas UPDS)

CAPÍTULO III: DISEÑO METODOLÓGICO
  3.1. Enfoque de la Investigación (Cuantitativo y Diseño de Ciencia del Diseño)
  3.2. Tipo y Alcance del Estudio (Explicativo - Evaluativo, Experimental)
  3.3. Hipótesis y Sistema de Variables
       3.3.1. Formulación de Hipótesis de Investigación (H1, H2) y Nulas (H0_1, H0_2)
       3.3.2. Identificación de Variables (Independiente, Dependiente e Intervinientes)
       3.3.3. Operacionalización de Variables (Matriz completa con dimensiones e indicadores)
  3.4. Población, Muestra y Unidad de Observación
       3.4.1. Población de referencia y muestra experimental
       3.4.2. Muestreo de escenarios de ataque (20 escenarios x 30 repeticiones)
       3.4.3. Unidad de análisis: Ventana temporal de 60 segundos
  3.5. Métodos, Técnicas e Instrumentos de Recolección de Datos
       3.5.1. Métodos de investigación (Empírico-experimental, analítico-estadístico)
       3.5.2. Técnicas e instrumentos (Fichas experimentales, adaptadores en modo monitor, Zeek)
       3.5.3. Consideraciones éticas, anonimización y seguridad del laboratorio

CAPÍTULO IV: ARQUITECTURA Y CARACTERIZACIÓN DEL ENTORNO EXPERIMENTAL
  4.1. Topología del Entorno Wi-Fi Aislado y Segmentación de Red
  4.2. Especificaciones de Hardware y Software (Punto de Acceso, Switch, Host de Captura)
  4.3. Configuración del Sensor Inalámbrico y Modo Monitor (Canal, Banda y Cobertura)
  4.4. Pipeline de Ingesta y Procesamiento de Tráfico (Zeek Logs + 802.11 Frames)
  4.5. Diseño del Módulo de Respuesta Automatizada y Reglas de Excepción (Fail-safe)
  4.6. Definición Operativa de la Línea Base de Reglas Estáticas (Línea de contraste)

CAPÍTULO V: ANÁLISIS, INTERPRETACIÓN DE RESULTADOS Y CONTRASTACIÓN DE HIPÓTESIS
  5.1. Caracterización de la Línea Base de Tráfico Normal (30 días de captura)
  5.2. Desempeño del Prototipo en la Batería Experimental (Resultados por escenario)
  5.3. Análisis Comparativo: Prototipo (Isolation Forest) vs. Línea Base de Reglas
       5.3.1. Evaluación de Detección: Exhaustividad (Recall), Precisión y F1-Score
       5.3.2. Evaluación de Calidad de Alerta: Tasa de Falsos Positivos (FPR)
       5.3.3. Evaluación de Eficiencia Operativa: Tiempo de Respuesta (Latencia de contención)
       5.3.4. Consumo de recursos de cómputo (CPU, memoria RAM)
  5.4. Pruebas de Significancia Estadística y Contrastación de Hipótesis
       5.4.1. Verificación de normalidad (Shapiro-Wilk)
       5.4.2. Prueba de rangos con signo de Wilcoxon
       5.4.3. Decisión estadística sobre H1 y H2
  5.5. Discusión de Resultados y Validación con Datasets Públicos (AWID3 / CICIDS2017)

CAPÍTULO VI: CONCLUSIONES Y RECOMENDACIONES
  6.1. Conclusiones (Alineadas estrictamente con los 6 Objetivos Específicos y la Hipótesis)
  6.2. Recomendaciones (Técnicas, operativas, de escalabilidad a producción y líneas futuras)

BIBLIOGRAFÍA (Norma APA 7.ª edición, mínimo 30 fuentes primarias/secundarias)
ANEXOS:
  Anexo A: Constancia de búsqueda bibliográfica en repositorio UPDS
  Anexo B: Guía de entrevista y acta firmada con Jefatura de Sistemas UPDS
  Anexo C: Carta de solicitud y autorización técnica de uso del laboratorio
  Anexo D: Ficha técnica de registro experimental (Formato estándar)
  Anexo E: Repositorio de código fuente y scripts de automatización (Git log / hashes)
  Anexo F: Tablas completas de métricas estadísticas de las 600 corridas
```

---

## 4. PROTOCOLO OPERATIVO EXPERIMENTAL (LA EJECUCIÓN TÉCNICA)

Para que los resultados sean irrebatibles ante el Tribunal de Grado, se debe asegurar la trazabilidad científica de cada uno de los 600 experimentos:

1. **Unidad de Tiempo y Fusión de Datos:**
   - La ventana de observación está fijada en **60 segundos**.
   - En cada ventana, el script fusiona dos vectores:
     - **Vector Capa 2 (Wi-Fi):** Cantidad de tramas `Probe Request`, `Beacon`, `Deauth`, `Disassoc`, `Auth`, anomalías de secuencia y conteo de MACs/SSIDs vistos.
     - **Vector Capa 3/4 (Zeek):** Conexiones por minuto (`conn.log`), consultas DNS anómalas (`dns.log`), solicitudes/arrendamientos DHCP sospechosos, volumen total de bytes y ratios SYN/FIN/RST.
2. **Matriz de Confusión por Ventana:**
   - Si durante la ventana $t$ hubo ataque inyectado en el laboratorio:
     - Alerta emitida por el modelo = **Verdadero Positivo (VP)**.
     - Silencio del modelo = **Falso Negativo (FN)**.
   - Si durante la ventana $t$ solo hubo tráfico normal:
     - Alerta emitida por el modelo = **Falso Positivo (FP)**.
     - Silencio del modelo = **Verdadero Negativo (VN)**.
3. **Métricas de Validación para Hipótesis H1:**
   - $\text{Exhaustividad (Recall)} = \frac{VP}{VP + FN} \ge 0.85$ (85%).
   - $\text{Tasa de Falsos Positivos (FPR)} = \frac{FP}{FP + VN} \le 0.05$ (5%).
4. **Métricas de Validación para Hipótesis H2:**
   - $\text{Tiempo de Respuesta} = t_{\text{bloqueo\_confirmado}} - t_{\text{inicio\_ataque}} \le 60\text{ s}$.

---

## 5. DIRECTRICES Y GUÍA DE TRABAJO CON IA CONVERSACIONAL PARA LA ESTUDIANTE

Como tutor, es vital establecer un marco ético, académico y técnico riguroso para que la estudiante aproveche la IA como acelerador cognitivo sin incurrir en plagio ni en alucinaciones teóricas:

### 5.1 Reglas de Oro en el Uso de IA
- **La IA asiste, la tesista ejecuta y redacta:** La IA no debe escribir el texto final sin revisión crítica. La estudiante es la autora responsable y defensora pública ante el tribunal.
- **Cero alucinación en fuentes:** Toda cita o referencia generada por la IA debe ser verificada físicamente en Google Scholar, IEEE Xplore, ACM Digital Library o en la Gaceta Oficial de Bolivia.
- **Transparencia metodológica:** Siguiendo la Guía UPDS 2026 (Anexo 3), si se utiliza soporte conversacional de IA para consultas conceptuales, se cita en el texto como comunicación personal (*p. ej.*, OpenAI/Google, comunicación personal, 2027) sin incluirla en la lista bibliográfica final, o bien se declara en la sección metodológica el uso de herramientas de apoyo en refactorización de código.
- **Validación del código generado:** Cualquier script de Python, Zeek script o regla de iptables producido con asistencia de IA debe probarse estrictamente dentro del laboratorio aislado antes de considerarse funcional.

### 5.2 Estructura de "Mega-Prompts" Recomendados para la Estudiante

La estudiante puede estructurar sus sesiones de trabajo con la IA dividiéndolas por capítulos temáticos:

#### Prompt 1: Desarrollo del Marco Teórico (Capítulo II)
> *"Actúa como experta en ciberseguridad y redes inalámbricas IEEE 802.11. Estoy redactando el Capítulo II de mi tesis de grado en la UPDS. Necesito que me ayudes a estructurar una explicación técnica profunda y formal sobre el funcionamiento matemático de Isolation Forest (Liu et al.) y cómo procesa anomalías en vectores de tráfico multidimensionales frente a detectores de firmas. Utiliza un estilo académico formal y sugiéreme conceptos clave para conectar este algoritmo con los logs estructurados de Zeek (conn.log y dhcp.log)."*

#### Prompt 2: Refactorización de Pipeline de Datos (Capítulo IV / Laboratorio)
> *"Actúa como ingeniera senior de software y analista de datos de red. Tengo dos fuentes de datos en mi laboratorio: un pcap con tramas de gestión Wi-Fi (capturado con modo monitor en Alfa AWUS) y los registros conn.log de Zeek. Ayúdame a escribir un script en Python (utilizando Pandas y Scikit-Learn) que sincronice ambos logs por timestamps y genere una matriz de características agregada por ventanas de 60 segundos para alimentar un modelo IsolationForest."*

#### Prompt 3: Análisis Estadístico y Contrastación (Capítulo V)
> *"Tengo los resultados de 600 ejecuciones experimentales (20 escenarios x 30 repeticiones) comparando mi modelo de Isolation Forest contra una línea base de reglas estáticas. Ayúdame a escribir el script en Python para aplicar la prueba de Wilcoxon de rangos con signo para muestras pareadas, calcular los intervalos de confianza de Wilson al 95% para la exhaustividad y generar gráficos de cajas (Boxplot) para los tiempos de respuesta."*

---

## 6. CHECKLIST DE CONTROL PARA REVISIÓN TUTORIAL

- [ ] **Check 1:** ¿El resumen final cumple con el límite estricto de 200 a 250 palabras y está en una sola página?
- [ ] **Check 2:** ¿Los objetivos específicos se redactaron con verbos en infinitivo según la taxonomía UPDS y hay una conclusión correspondiente para cada uno en el Capítulo VI?
- [ ] **Check 3:** ¿El Marco Normativo está organizado de forma descendente estricta siguiendo la Pirámide de Kelsen boliviana?
- [ ] **Check 4:** ¿Las 600 corridas experimentales están registradas en fichas reproducibles con fecha, hora exacta y parámetros en el Anexo de datos?
- [ ] **Check 5:** ¿Se cuenta con un mínimo de 30 fuentes bibliográficas debidamente citadas en APA 7.ª edición y con respaldo directo en el texto?
- [ ] **Check 6:** ¿El código fuente de extracción, entrenamiento y respuesta automatizada se encuentra preservado en un repositorio Git con commits trazables?
