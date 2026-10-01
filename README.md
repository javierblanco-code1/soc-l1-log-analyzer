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

Además, el caso documentado de este repositorio utiliza contexto de **IP + usuario + servicio + ventana temporal** para investigar actividad compatible con password guessing.

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

## Case Study 001

El caso completo de **SSH Password Guessing / Brute Force Detection** documenta cuatro fallos de autenticación sobre SSH en un dataset sintético, junto con timeline, IOC, MITRE ATT&CK, severidad, criterios de escalamiento y limitaciones.

- [Case Study 001](docs/CASE-STUDY-001-BRUTE-FORCE.md)
- [SOC Ticket 001](docs/SOC-001-TICKET.md)
- [Structured Triage](docs/CASE-001-triage.json)

## Estructura del proyecto

```text
.
├── log_analyzer.py
├── syslog.log
├── requirements.txt
├── docs/
│   ├── CASE-STUDY-001-BRUTE-FORCE.md
│   ├── SOC-001-TICKET.md
│   └── CASE-001-triage.json
└── README.md
```

## Limitaciones actuales

- El dataset es sintético y pequeño.
- El extractor no debe interpretarse como un SIEM completo.
- La correlación por threshold/window está documentada como procedimiento de triaje y no como una regla nativa del parser actual.
- La salida asistida por IA requiere validación del analista antes de tomar una decisión.

## Roadmap

- [ ] Unit tests para parsing y detección.
- [ ] Reglas configurables en YAML/JSON.
- [ ] Correlación threshold/window nativa.
- [ ] Exportación JSON/CSV de resultados.
- [ ] Enriquecimiento automático de IPs/dominios.
- [ ] Integración opcional con el proyecto VirusTotal.
- [ ] Pipeline CI con tests.

## Security Notes

Nunca subir API keys, tokens, credenciales reales ni logs que contengan PII. Usar datos sintéticos o previamente anonimizados.

## Portfolio

Este repositorio forma parte del portfolio SOC L1 de Javier Blanco y se utiliza como evidencia técnica de **log analysis, alert triage, MITRE ATT&CK y Python automation**.
