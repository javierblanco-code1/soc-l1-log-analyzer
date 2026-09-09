import os
from google import genai
from tenacity import retry, stop_after_attempt, wait_exponential

LOG_FILE = "syslog.log"

def extract_suspicious_events(file_path: str) -> list[str]:
    """Lee el archivo de logs y aísla eventos sospechosos."""
    suspicious_patterns = ["Failed password", "403 Forbidden", "Unauthorized"]
    events = []

    if not os.path.exists(file_path):
        print(f"[!] Error: El archivo {file_path} no existe.")
        return events

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if any(pattern in line for pattern in suspicious_patterns):
                events.append(line.strip())

    return events

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def generate_soc_report(events: list[str], api_key: str) -> str:
    """Envía los eventos a Gemini para generar el informe de triaje L2."""
    client = genai.Client(api_key=api_key)

    prompt = f"""
    Actúa como un Analista SOC L2. Analiza los siguientes eventos de log aislados por nuestro script L1:

    {events}

    Genera un informe técnico de triaje breve en formato Markdown con la siguiente estructura:
    1. Resumen de la Amenaza.
    2. Nivel de Severidad (Bajo, Medio, Alto, Crítico).
    3. Indicadores de Compromiso (IoCs) identificados (IPs, Usuarios, etc.).
    4. Recomendaciones de Mitigación Inmediata para el Analista L1.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[!] Error: La variable de entorno GEMINI_API_KEY no está configurada.")
        return

    print("[-] Analizando logs del sistema...")
    events = extract_suspicious_events(LOG_FILE)

    if not events:
        print("[-] No se detectaron eventos sospechosos.")
        return

    print(f"[!] {len(events)} eventos sospechosos identificados. Solicitando triaje con IA...")
    try:
        report = generate_soc_report(events, api_key)
        print("\n--- INFORME DE TRIAJE GENERADO ---\n")
        print(report)

        with open("informe_triaje.md", "w", encoding="utf-8") as f:
            f.write(report)
        print("\n[-] Informe guardado exitosamente en 'informe_triaje.md'")

    except Exception as e:
        print(f"[!] Fallo en el procesamiento del informe: {e}")

if __name__ == "__main__":
    main()
