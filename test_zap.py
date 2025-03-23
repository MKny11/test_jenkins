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
    
    # Lancer le scan actif
    scan_id = ZAP.ascan.scan(TARGET_URL)
    
    # Vérifier si l'ID de scan est valide
    if not scan_id or scan_id == 'does_not_exist':
        print("Erreur : Le scan n'a pas pu être démarré correctement.")
        return
    
    print(f"Scan démarré avec l'ID : {scan_id}")
    
    # Suivi de la progression du scan
    while True:
        status = ZAP.ascan.status(scan_id)
        
        if status == 'does_not_exist':
            print(f"Erreur : Scan avec l'ID {scan_id} n'existe pas.")
            break
        
        progress = int(status)
        print(f"Progression du scan : {progress}%")
        
        if progress >= 100:
            print("Scan actif terminé !")
            break
        
        time.sleep(5)

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
