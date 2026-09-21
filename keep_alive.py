from datetime import datetime, timedelta
import time
import urllib.request


URL = "https://rota-estudantil-backend.onrender.com/health"
INTERVALO_SEGUNDOS = 300  
DURACAO_TOTAL_HORAS = 6

tempo_inicio = datetime.now()
tempo_limite = tempo_inicio + timedelta(hours=DURACAO_TOTAL_HORAS)

print(f"Iniciando keep-alive para: {URL}")
print(f"Vai rodar até: {tempo_limite.strftime('%H:%M:%S')}\n")

while datetime.now() < tempo_limite:
  agora = datetime.now().strftime("%H:%M:%S")
  try:
    req = urllib.request.Request(URL, headers={"User-Agent": "Python-KeepAlive"})
    with urllib.request.urlopen(req, timeout=10) as resposta:
      print(
          f"[{agora}] Ping enviado com sucesso! Status HTTP:"
          f" {resposta.status}"
      )
  except Exception as e:
    print(f"[{agora}] Falha ao pingar o servidor: {e}")

  if datetime.now() >= tempo_limite:
    break

  print(f"Próximo ping em 5 minutos...\n")
  time.sleep(INTERVALO_SEGUNDOS)

print("\nCiclo de 6 horas finalizado.")
