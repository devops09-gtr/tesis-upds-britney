# FLUJO DE TRABAJO, REVISIÓN Y APROBACIÓN POR PULL REQUEST (PR)

**Modelo de Colaboración Tutor - Tesista en GitHub**  
**Postulante:** Britney Aracelly Arratia Gonzales  
**Tutor:** Ing. Gonzalo Tarifa Rodríguez  
**Repositorio:** `devops09-gtr/tesis-upds-britney`

---

## 1. CICLO DE TRABAJO BASADO EN RAMAS (BRANCHING STRATEGY)

La estudiante **nunca debe hacer push directo a la rama `main`**. Toda consulta, avance de código o entrega de capítulos se gestiona mediante ramas de trabajo y **Pull Requests (PR)**:

```text
 [ main ] ──────────────────────────────────────────────────────────► (Código y Tesis Aprobada)
    │                                                        ▲
    │ (Crea rama por fase o capítulo)                        │ (Merge tras revisión y aprobación)
    ▼                                                        │
 [ feature/capitulo-1-introduccion ] ────────► [ Pull Request (PR) ]
```

---

## 2. TIPOS DE PULL REQUEST (PR) QUE PUEDE ABRIR BRITNEY

1. **PR de Consulta Técnica o Metodológica:**
   * Cuando tenga dudas sobre cómo extraer una característica de Zeek, cómo configurar Scapy o cómo formular una sección metodológica.
   * En el título: `[CONSULTA] Duda sobre sincronización de timestamps en Zeek`.
2. **PR de Avance de Código / Fase:**
   * Cuando complete un componente del prototipo (*ej.* el capturador Wi-Fi o el modelo Isolation Forest).
   * En el título: `[FASE 2] Implementación del sensor Wi-Fi en modo monitor`.
3. **PR de Entrega de Capítulo de Tesis:**
   * Cuando redacte o actualice un capítulo de su documento de tesis.
   * En el título: `[DOCUMENTO] Borrador completo del Capítulo II (Marco Teórico y Normativo)`.

---

## 3. CHECKLIST DE CONTROL DEL TUTOR PARA APROBACIÓN

Antes de dar el **"Approve & Merge"** a un PR de la estudiante, el Tutor (o el asistente del tutor) verificará:

- [ ] **Rigor de Código:** ¿El código sigue PEP 8 y no contiene contraseñas ni rutas absolutas locales (`C:\Users\...`)?
- [ ] **Reproducibilidad:** ¿El código incluye comentarios y puede ejecutarse sin fallar en Linux/Windows?
- [ ] **Rigor Académico:** Si el PR incluye texto de tesis, ¿cumple con la Guía UPDS 2026 y no tiene párrafos copiados sin cita?
- [ ] **Verificación de Fuentes:** ¿Las citas añadidas son reales y están en formato APA 7.ª edición?
- [ ] **Cero Alucinación de IA:** Si se usó IA como apoyo, ¿la estudiante revisó y validó críticamente el contenido?

---

## 4. ESTADOS Y ETIQUETAS DE UN PR (LABELS EN GITHUB)

* `estado: revision-tutor`: El PR está listo para que el Ing. Tarifa lo examine y comente.
* `estado: ajustes-requeridos`: El tutor dejó observaciones que Britney debe corregir en la misma rama.
* `estado: aprobado`: Cumple los estándares y se fusiona a `main`.
* `fase: fase-2` / `fase: fase-3` / `fase: fase-4`: Indica a qué hito del cronograma corresponde.
