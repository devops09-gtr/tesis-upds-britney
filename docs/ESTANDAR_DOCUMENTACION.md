# ESTÁNDAR DE DOCUMENTACIÓN ACADÉMICA DE TESIS (UPDS)

**Guía Oficial de Redacción y Rigor Científico**  
**Postulante:** Britney Aracelly Arratia Gonzales  
**Tutor:** Ing. Gonzalo Tarifa Rodríguez  
**Normativa Base:** Guía Metodológica de Tesis de Licenciatura UPDS (2026) y APA 7.ª edición

---

## 1. DIRECTRICES DE REDACCIÓN Y ESTILO ACADÉMICO

1. **Voz y Tiempos Verbales:**
   * La tesis final se redacta en **tercera persona** o forma impersonal (*«se implementó»*, *«se evaluaron»*, *«los datos demuestran»*). Evitar el uso de primera persona (*«hice»*, *«evalué»*, *«nuestro modelo»*).
   * Al pasar del perfil a la tesis final:
     * El Capítulo I y II se redactan en presente o pretérito reflexivo.
     * Los Capítulos III, IV y V se redactan en **pasado** (*«se capturaron 30 días de tráfico normal»*, *«el modelo obtuvo un 87.5% de exhaustividad»*).
2. **Resumen Estructurado (Abstract):**
   * Obligatoriamente entre **200 y 250 palabras** en **una sola página**.
   * Debe sintetizar: Problema, Objetivo principal, Metodología (Zeek + Isolation Forest + 20 escenarios), Hallazgos clave (Recall, FPR, tiempos) y Conclusión principal.
   * Sin viñetas de capítulos, sin citas textuales y con 4 a 6 Palabras Clave (*Keywords*).

---

## 2. ESTRUCTURA CAPITULAR OFICIAL Y CHECKLIST POR CAPÍTULO

```text
Portada Oficial UPDS
Aprobaciones y Resumen
CAPÍTULO I: INTRODUCCIÓN Y CONTEXTO
CAPÍTULO II: MARCO TEÓRICO, CONCEPTUAL Y NORMATIVO
CAPÍTULO III: DISEÑO METODOLÓGICO
CAPÍTULO IV: DIAGNÓSTICO Y CARACTERIZACIÓN DEL ENTORNO EXPERIMENTAL
CAPÍTULO V: ANÁLISIS, INTERPRETACIÓN DE DATOS Y CONTRASTACIÓN DE HIPÓTESIS
CAPÍTULO VI: CONCLUSIONES Y RECOMENDACIONES
Bibliografía y Anexos
```

### 2.1 Requisitos Específicos por Capítulo

* **Capítulo I (Introducción):**
  * Incluir árbol de problemas (C1, C2, C3 vs. E1, E2, E3) y árbol de objetivos en diagramas formales.
  * Mantener coherencia estricta entre la pregunta de investigación y el Objetivo General.
* **Capítulo II (Marco Teórico y Normativo):**
  * **Marco Conceptual:** Obligatorio. Definir cada término técnico según al menos un autor de referencia y justificar la postura teórica asumida.
  * **Marco Normativo:** Obligatorio bajo la **Pirámide de Kelsen boliviana** estricta:
    1. Constitución Política del Estado (CPE, 2009 - Arts. 21 y 103).
    2. Ley N.º 164 General de Telecomunicaciones y TIC (Arts. 71 y 72).
    3. D.S. N.º 1793 (Reglamento Ley 164 - Software libre) y D.S. N.º 2514 (AGETIC / CGII).
    4. Resoluciones AGETIC (Planes Institucionales de Seguridad).
    5. Normativa interna y reglamentos de red de la UPDS.
* **Capítulo III (Diseño Metodológico):**
  * Enfoque cuantitativo, alcance explicativo-evaluativo, diseño experimental de laboratorio (Ciencia del Diseño).
  * Matriz completa de operacionalización de variables (con indicadores y escalas de razón/nominal).
* **Capítulo IV (Caracterización del Entorno de Ingeniería):**
  * Describir detalladamente el hardware (AP, antena, Cisco Catalyst 3650, interfaces de red), la topología aislada y los parámetros de captura.
* **Capítulo V (Resultados y Estadística):**
  * Tablas completas con media y desviación estándar de Recall, Precision, F1-Score, FPR y Latencia de respuesta.
  * Test de normalidad (Shapiro-Wilk) y contraste formal de hipótesis mediante la prueba de **Wilcoxon de rangos con signo** ($p < 0.05$).
* **Capítulo VI (Conclusiones y Recomendaciones):**
  * **Regla de oro UPDS:** Debe existir exactamente **una conclusión por cada uno de los 6 objetivos específicos**, cerrando con el veredicto explícito de aceptación o rechazo de las hipótesis $H_1$ y $H_2$.

---

## 3. NORMAS APA 7.ª EDICIÓN (ESTÁNDAR OBLIGATORIO UPDS)

1. **Mínimo de Fuentes:** La UPDS exige un mínimo de **30 fuentes documentales** (artículos científicos indexados, libros especializados, estándares IEEE/NIST y normas legales).
2. **Formato Autor-Fecha:**
   * Cita narrativa: *«Arp et al. (2022) demostraron que...»*
   * Cita parentética: *«...los detectores basados en firmas presentan limitaciones frente a nuevas amenazas (Khraisat et al., 2019).»*
3. **Citas de Inteligencia Artificial (Guía UPDS 2026):**
   * Se citan únicamente en el texto como comunicación personal:  
     *(OpenAI, comunicación personal, 18 de marzo de 2027)* o *(Google, comunicación personal, 2027)*.  
   * **No se colocan en la bibliografía final.**
4. **Citas Textuales:**
   * Menos de 40 palabras: Entre comillas dobles, dentro del párrafo, con autor, año y página: `(p. 45)`.
   * Más de 40 palabras: Párrafo aparte con sangría izquierda de 1,27 cm, sin comillas. **Evitar abusar de citas largas** para no inflar artificialmente el texto.
