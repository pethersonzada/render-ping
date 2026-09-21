import os
import time
import urllib.request
from datetime import datetime

URL = "https://rota-estudantil-backend.onrender.com/health"
SLEEP_SECONDS = int(os.getenv("SLEEP_SECONDS", "300"))
MAX_RUNTIME_SECONDS = int(os.getenv("MAX_RUNTIME_SECONDS", "21000"))

def main():
    print(f"Iniciando vigília perpétua para: {URL}")
    print(f"Intervalo: {SLEEP_SECONDS}s | Duração máxima: {MAX_RUNTIME_SECONDS}s")
    
    start_time = time.time()
    tentativa = 0

    while time.time() - start_time < MAX_RUNTIME_SECONDS:
        tentativa += 1
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            req = urllib.request.Request(URL, headers={"User-Agent": "Python-KeepAlive/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resposta:
                print(f"[{agora}] Tentativa {tentativa}: Sucesso. O servidor respira (Status {resposta.status})")
        except Exception as e:
            print(f"[{agora}] Tentativa {tentativa}: Falha na escuridão. Erro: {e}")

        time.sleep(SLEEP_SECONDS)

    print("O tempo da vigília esgotou. O ciclo será renovado pelos deuses do cron.")

if __name__ == "__main__":
    main()
