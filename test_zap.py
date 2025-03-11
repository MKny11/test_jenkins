import time
import requests

# URL de l'API ZAP
ZAP_URL = "http://127.0.0.1:8081"  # L'adresse de ton serveur ZAP

# Cibler l'URL à explorer avec le spider
TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html"

# Démarrer le spider
spider = requests.get(f"{ZAP_URL}/JSON/spider/action/scan/?url={TARGET_URL}&maxChildren=5")
spider_id = spider.json().get("scan")

# Vérifier l'état du spider jusqu'à ce qu'il soit terminé
while True:
    status = requests.get(f"{ZAP_URL}/JSON/spider/view/status/?scanId={spider_id}")
    progress = status.json().get("status")
    print(f"Spider progress: {progress}%")
    if progress == "100":
        break
    time.sleep(2)

# Récupérer le rapport HTML après le spider
report = requests.get(f"{ZAP_URL}/OTHER/core/other/htmlreport/")
with open("zap_spider_report.html", "w") as f:
    f.write(report.text)

print("Exploration terminée ! Rapport généré.")
