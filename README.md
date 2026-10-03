# SOC L1 Log Analyzer — Python

Herramienta de automatización orientada a **SOC Level 1** para acelerar el triaje inicial de logs de autenticación y extraer señales que merecen investigación.

> **Contexto:** proyecto de laboratorio / portfolio. No representa experiencia laboral en un SOC productivo.

## Objetivo

Convertir logs de sistema en información útil para un analista:

`Logs → Parsing → Event extraction → Correlation → Triage → Documentation`

El proyecto está diseñado para reducir tareas manuales repetitivas y dejar una salida estructurada que pueda revisarse y escalarse.

## Detecciones y señales

El extractor actual identifica patrones como:

- `Failed password`
- `403 Forbidden`
- `Unauthorized`

Además, los casos documentados utilizan contexto de **IP + usuario + servicio + ventana temporal** para investigar actividad compatible con password guessing y phishing.

### MITRE ATT&CK

**T1110.001 — Brute Force: Password Guessing**

El mapeo se utiliza como hipótesis de técnica durante el triaje y se valida contra la evidencia disponible.

## Stack

- Python 3.10+
- Regex / parsing de logs
- JSON
- `google-genai`
- `tenacity`
- Git / GitHub

## Ejecución

```bash
git clone https://github.com/javierblanco-code1/soc-l1-log-analyzer.git
cd soc-l1-log-analyzer
pip install -r requirements.txt
python log_analyzer.py
```

Para las funciones que requieren una API, usar variables de entorno y **no** guardar claves en el repositorio.

## SOC L1 Workflow

1. **Collect** — recibir los logs.
2. **Extract** — aislar eventos relevantes.
3. **Correlate** — agrupar por contexto.
4. **Triage** — valorar severidad y confianza.
5. **Enrich** — agregar contexto adicional.
6. **Document** — registrar evidencia y decisión.
7. **Escalate** — escalar cuando los criterios lo justifican.

---

# SOC Case Studies

Este repositorio incluye investigaciones de laboratorio documentadas de extremo a extremo.

## Case Study 001 — SSH Brute Force

El caso documenta cuatro fallos de autenticación sobre SSH en un dataset sintético, junto con timeline, IOC, MITRE ATT&CK, severidad, criterios de escalamiento y limitaciones.

- [Case Study 001](docs/CASE-STUDY-001-BRUTE-FORCE.md)
- [SOC Ticket 001](docs/SOC-001-TICKET.md)
- [Structured Triage](docs/CASE-001-triage.json)

## Case Study 002 — Phishing Investigation

Investigación de un correo de phishing orientado a credential theft. El caso demuestra análisis de metadata, autenticación de correo, URL/IOC extraction, timeline, MITRE ATT&CK, severity assessment y respuesta recomendada.

- [Case Study 002](docs/CASE-STUDY-002-PHISHING.md)
- [Email Evidence](docs/evidence/CASE-002/email-sample.eml)
- [Investigation Timeline](docs/evidence/CASE-002/timeline.md)
- [IOC Inventory](docs/evidence/CASE-002/iocs.md)
- [SOC Ticket 002](docs/evidence/CASE-002/SOC-002-TICKET.md)
- [Structured Triage](docs/evidence/CASE-002/triage.json)

> **Nota:** Case Study 002 utiliza datos completamente sintéticos y dominios reservados para documentación. No se requiere ni recomienda interactuar con el enlace incluido.

## Estructura del proyecto

```text
.
├── log_analyzer.py
├── syslog.log
├── requirements.txt
├── docs/
│   ├── CASE-STUDY-001-BRUTE-FORCE.md
│   ├── SOC-001-TICKET.md
│   ├── CASE-001-triage.json
│   ├── CASE-STUDY-002-PHISHING.md
│   └── evidence/
│       └── CASE-002/
│           ├── email-sample.eml
│           ├── timeline.md
│           ├── iocs.md
│           ├── SOC-002-TICKET.md
│           └── triage.json
└── README.md
```

## Limitaciones actuales

- Los datasets de los casos son sintéticos y pequeños.
- El extractor no debe interpretarse como un SIEM completo.
- La correlación por threshold/window está documentada como procedimiento de triaje y no como una regla nativa del parser actual.
- La salida asistida por IA requiere validación del analista antes de tomar una decisión.
- Los indicadores de phishing del Case Study 002 son simulados y no representan una campaña real.

## Roadmap

- [ ] Unit tests para parsing y detección.
- [ ] Reglas configurables en YAML/JSON.
- [ ] Correlación threshold/window nativa.
- [ ] Exportación JSON/CSV de resultados.
- [ ] Enriquecimiento automático de IPs/dominios.
- [ ] Integración opcional con el proyecto VirusTotal.
- [ ] Pipeline CI con tests.
- [x] SOC Case Study 001 — SSH Brute Force.
- [x] SOC Case Study 002 — Phishing Investigation.
- [ ] SOC Case Study 003 — PowerShell / Process Discovery.

## Security Notes

Nunca subir API keys, tokens, credenciales reales ni logs que contengan PII. Usar datos sintéticos o previamente anonimizados.

## Portfolio

Este repositorio forma parte del portfolio SOC L1 de Javier Blanco y se utiliza como evidencia técnica de **log analysis, alert triage, phishing investigation, MITRE ATT&CK y Python automation**.
