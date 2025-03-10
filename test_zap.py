import time
import requests

# URL de l'API ZAP
ZAP_URL = "http://127.0.0.1:8081"  # L'adresse de ton serveur ZAP

# Cibler l'URL à scanner
TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html"

# Démarrer un scan actif sur l'URL cible
scan = requests.get(f"{ZAP_URL}/JSON/ascan/action/scan/?url={TARGET_URL}")
scan_id = scan.json().get("scan")

# Vérifier l'état du scan jusqu'à ce qu'il soit terminé
while True:
    status = requests.get(f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}")
    progress = status.json().get("status")
    print(f"Scan progress: {progress}%")
    if progress == "100":
        break
    time.sleep(1)  # Vérification plus rapide (1 seconde)

# Récupérer le rapport HTML du scan
report = requests.get(f"{ZAP_URL}/OTHER/core/other/htmlreport/")

# Sauvegarder le rapport
with open("zap_report.html", "w") as f:
    f.write(report.text)

print("Scan terminé ! Rapport généré.")
