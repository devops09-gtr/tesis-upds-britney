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

## 🤖 Guia Rapida para Asistentes de IA (AI Agents & LLMs)

Si eres un modelo de Inteligencia Artificial (ChatGPT, Claude, Gemini, DeepSeek, etc.) asistiendo a Britney en esta tesis:
1. **Lee obligatoriamente** el archivo [`docs/INSTRUCCIONES_IA.md`](docs/INSTRUCCIONES_IA.md) para conocer las reglas de trabajo, directrices eticas, estilo academico y formato UPDS (APA 7.ª ed.).
2. **Revisa la planificacion completa** en [`docs/PLAN_DE_ACCION.md`](docs/PLAN_DE_ACCION.md).
3. **Consulta la guia de ejecucion tecnica** en [`docs/GUIA_FASE_2.md`](docs/GUIA_FASE_2.md) antes de proponer cambios en el codigo o en la arquitectura del laboratorio.

---

## 📂 Estructura del Repositorio

```text
├── docs/                      # Documentacion academica y guias metodologicas
│   ├── INSTRUCCIONES_IA.md    # Directrices clave para la IA conversacional
│   ├── PLAN_DE_ACCION.md      # Plan de accion integral (Capitulos, Hitos, Cronograma)
│   └── GUIA_FASE_2.md         # Guia paso a paso para el despliegue del prototipo (Fase 2)
├── src/                       # Codigo fuente del prototipo
│   ├── capture/               # Scripts de captura Wi-Fi 802.11 y Zeek
│   │   ├── wifi_monitor.py    # Capturador y parser de tramas 802.11 (Scapy/Tshark)
│   │   └── zeek_runner.sh     # Script para ejecucion y rotacion de logs de Zeek
│   ├── pipeline/              # Fision temporal y extraccion de caracteristicas
│   │   └── feature_extractor.py # Agrupador por ventanas de 60 segundos
│   ├── model/                 # Modelos de deteccion
│   │   ├── isolation_forest.py # Detector no supervisado (Scikit-Learn)
│   │   └── static_rules.py    # Detector de linea base (reglas y umbrales fijos)
│   └── response/              # Scripts de mitigacion y respuesta automatizada
│       └── responder.py       # Bloqueo temporal por iptables/MAC y alertas seguras
├── experiments/               # Fichas experimentales, 20 escenarios y datasets de prueba
│   ├── scenarios/             # Definicion de los 20 escenarios de ataque
│   └── logs/                  # Registro de corridas y marcas de tiempo
├── config/                    # Configuraciones de red, Zeek y parametros de modelo
├── requirements.txt           # Dependencias Python
└── README.md                  # Este documento
```

---

## 🚀 Inicio Rapido (Fase 2)

Para desplegar el prototipo en tu maquina Linux o maquina virtual de pruebas:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/devops09-gtr/tesis-upds-britney.git
   cd tesis-upds-britney
   ```
2. **Crear entorno virtual de Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Revisar y ejecutar la guia de la Fase 2:** Sigue los pasos descritos en [`docs/GUIA_FASE_2.md`](docs/GUIA_FASE_2.md).
