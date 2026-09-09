# SOC L1: Automation for Log Analysis and AI-Driven Triage

## 📌 Descripción
Herramienta de automatización para Analistas SOC Level 1 diseñada para procesar registros del sistema (`syslog`), identificar patrones de actividad maliciosa (fuerza bruta SSH, accesos no autorizados) y generar reportes de triaje enriquecidos mediante Inteligencia Artificial (Google Gemini API).

## 🚀 Características
- **Parsing Automático:** Extracción de eventos sospechosos basada en expresiones y reglas de coincidencia.
- **Enriquecimiento con IA:** Clasificación automática de severidad, extracción de IoCs y recomendaciones de mitigación redactadas bajo la perspectiva de un Analista SOC L2.
- **Resiliencia:** Implementación de reintentos exponenciales para garantizar la ejecución ante incidencias de red o API.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Librerías:** `google-genai`, `tenacity`
- **Modelos de IA:** Gemini 2.5 Flash

## 📋 Requisitos Previos e Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/soc-l1-log-analyzer.git](https://github.com/TU_USUARIO/soc-l1-log-analyzer.git)
   cd soc-l1-log-analyzer
2. Instalar dependencias:
   Bash
pip install -r requirements.txt
3. Configurar la clave API:
   Bash
export GEMINI_API_KEY="tu_api_key_aqui"  # Linux/macOS
set GEMINI_API_KEY="tu_api_key_aqui"     # Windows CMD
4. Ejecutar el analizador:
   Bash
python log_analyzer.py
