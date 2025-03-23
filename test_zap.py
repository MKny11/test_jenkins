#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

# Clé API ZAP
API_KEY = 'efou9m300gej2lrkbb4b51tsre'

# URL cible
TARGET_URL = 'https://www.selenium.dev/selenium/web/web-form.html'

# Configuration du proxy pour le daemon ZAP
ZAP = ZAPv2(apikey=API_KEY, proxies={'http': 'http://localhost:8081/', 'https': 'http://localhost:8081/'})

def start_scan():
    print(f"Démarrage du scan actif sur {TARGET_URL}...")
    scan_id = ZAP.ascan.scan(TARGET_URL)
    
    # Suivi de la progression du scan
    while int(ZAP.ascan.status(scan_id)) < 100:
        progress = ZAP.ascan.status(scan_id)
        print(f"Progression du scan : {progress}%")
        time.sleep(5)

    print("Scan actif terminé !")

    # Affichage des hôtes scannés
    print(f"Hôtes trouvés : {', '.join(ZAP.core.hosts)}")

    # Affichage des vulnérabilités trouvées
    print("Alertes :")
    alerts = ZAP.core.alerts(baseurl=TARGET_URL)
    pprint(alerts)

    # Génération d'un rapport HTML
    with open('zap_report.html', 'w', encoding='utf-8') as f:
        report = ZAP.core.htmlreport()
        f.write(report)
    print("Rapport généré : 'zap_report.html'")

if __name__ == "__main__":
    start_scan()
