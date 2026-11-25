# Evaluacion Experimental de Deteccion de Anomalias Wi-Fi con Zeek e Isolation Forest (UPDS - Tarija)

[![UPDS Modalidad de Grado II](https://img.shields.io/badge/UPDS-Modalidad%20de%20Grado%20II-blue.svg)](https://www.upds.edu.bo/)
[![Status](https://img.shields.io/badge/Estado-Fase%202%20En%20Desarrollo-orange.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)]()

Repositorio oficial del proyecto de Tesis de Grado en **Ingenieria en Redes y Telecomunicaciones**, Universidad Privada Domingo Savio (Sede Tarija).

* **Postulante:** Britney Aracelly Arratia Gonzales
* **Tutor:** Ing. Gonzalo Tarifa Rodriguez
* **Periodo de Ejecucion:** 7 de diciembre de 2026 - 5 de marzo de 2027

---

## 📋 Resumen del Proyecto

Este proyecto evalua experimentalmente un prototipo de deteccion de anomalias en redes Wi-Fi (IEEE 802.11) y trafico IP combinando la observacion pasiva estructurada con **Zeek**, el algoritmo no supervisado **Isolation Forest** y mecanismos de respuesta automatizada dentro de un entorno emulado y aislado representativo de la UPDS - Tarija.

Se contrasta el modelo predictivo frente a una **linea base de reglas estaticas** sobre **20 escenarios de ataque** y **600 corridas experimentales**, evaluando:
1. **Exhaustividad (Recall):** Meta $\ge 85\%$.
2. **Tasa de Falsos Positivos (FPR):** Meta $\le 5\%$.
3. **Tiempo de Respuesta (Contencion):** Meta $\le 60\text{ s}$.

---

## 📚 Estándares del Proyecto y Guías Metodológicas

Para garantizar la máxima calidad técnica y metodológica, el proyecto se rige por los siguientes documentos en [`docs/`](docs/):

| Documento | Descripción y Propósito |
| :--- | :--- |
| 📖 [**Guía de Implementación**](docs/GUIA_IMPLEMENTACION.md) | Arquitectura del banco emulado, topología, puesta en modo monitor y los 20 escenarios de ataque. |
| ⚙️ [**Estándar de Ingeniería**](docs/ESTANDAR_INGENIERIA.md) | Normas PEP 8, registro obligatorio de las 600 corridas, seguridad y protocolos fail-safe. |
| 📝 [**Estándar de Documentación de Tesis**](docs/ESTANDAR_DOCUMENTACION.md) | Estructura capitular UPDS 2026, APA 7.ª ed. (mínimo 30 fuentes) y regla de conclusiones por objetivos. |
| 🔄 [**Flujo de Aprobación por PR**](docs/FLUJO_DE_APROBACION.md) | Cómo enviar avances y consultas mediante Pull Requests para revisión y aprobación del Tutor. |
| 🤖 [**Instrucciones para la IA**](docs/INSTRUCCIONES_IA.md) | Directrices éticas, técnicas y de citas para ChatGPT / Claude / Gemini / DeepSeek. |
| 📅 [**Plan de Acción Integral**](docs/PLAN_DE_ACCION.md) | Cronograma oficial de Grado II, hitos institucionales y desglose de capítulos. |

---

## 🤝 Modelo de Trabajo Tutor - Tesista (Flujo de Pull Requests)

1. **La estudiante crea una rama:**
   ```bash
   git checkout -b feature/avance-fase2
   ```
2. **Desarrolla o redacta sus avances:**
   * Agrega sus scripts o documentos.
   * Ejecuta pruebas locales.
3. **Envía un Pull Request (PR):**
   * En GitHub abre un PR hacia `main`.
   * La plantilla automática se cargará para describir el avance o formular dudas técnicas.
4. **Revisión del Tutor:**
   * El Tutor revisa el código o texto, deja sugerencias en línea y, cuando cumple los estándares, realiza el **Approve & Merge**.

---

## 📂 Estructura del Repositorio

```text
├── docs/                      # Estándares, guías y documentos metodológicos
│   ├── GUIA_IMPLEMENTACION.md # Guía técnica de arquitectura y los 20 escenarios
│   ├── ESTANDAR_INGENIERIA.md # Estándar de código, logging de 600 pruebas y seguridad
│   ├── ESTANDAR_DOCUMENTACION.md # Guía de redacción UPDS 2026 y APA 7.ª edición
│   ├── FLUJO_DE_APROBACION.md # Mecánica de Pull Requests y revisión tutorial
│   ├── INSTRUCCIONES_IA.md    # Reglas para la IA conversacional de Britney
│   └── PLAN_DE_ACCION.md      # Cronograma e hitos de Modalidad de Grado II
├── src/                       # Código fuente del prototipo
│   ├── capture/               # Captura Wi-Fi 802.11 y Zeek runner
│   ├── pipeline/              # Fusión temporal de características (ventanas 60s)
│   ├── model/                 # Modelos Isolation Forest y Reglas Estáticas
│   ├── response/              # Módulo de mitigación automatizada (iptables/fail-safe)
│   └── test_pipeline.py       # Script de validación integral de extremo a extremo
├── experiments/               # Fichas experimentales y datasets de prueba
├── iniciar_entorno.bat         # Instalador y ejecutor de 1 solo clic para Windows
├── setup_linux.sh             # Instalador automático para Ubuntu/Debian en Laboratorio
├── requirements.txt           # Dependencias científicas en Python
└── README.md                  # Este documento
```

---

## 🚀 Inicio Rápido

### En Windows (Desarrollo y pruebas):
Solo haz **doble clic en `iniciar_entorno.bat`** y luego escribe:
```cmd
python src\test_pipeline.py
```

### En Linux / Laboratorio (Entorno completo):
```bash
chmod +x setup_linux.sh
./setup_linux.sh
source venv/bin/activate
python src/test_pipeline.py
```
