import time
import requests

# Définition des paramètres ZAP
ZAP_URL = "http://localhost:8081"  # URL de ZAP
TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html")
 # Site web cible

# Démarrer un scan actif
scan = requests.get(f"{ZAP_URL}/JSON/ascan/action/scan/?url={TARGET_URL}")
scan_id = scan.json()["scan"]

# Suivre la progression du scan
while True:
    progress = requests.get(f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}").json()["status"]
    print(f"Progression du scan : {progress}%")
    if progress == "100":
        break
    time.sleep(5)

# Générer un rapport HTML
report = requests.get(f"{ZAP_URL}/OTHER/core/other/htmlreport/")
with open("zap_report.html", "w") as file:
    file.write(report.text)

print("Scan terminé ! Rapport généré : zap_report.html")
