#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

# Cible à scanner
TARGET_URL = 'https://www.selenium.dev/selenium/web/web-form.html'
ZAP_URL = 'http://127.0.0.1:8081'  # Port de ZAP (assure-toi qu'il est ouvert)
API_KEY = None  # Si l'API key est activée, remplace `None` par la clé

# Connexion à ZAP
print(f"🔌 Connexion à ZAP sur {ZAP_URL}")
zap = ZAPv2(apikey=API_KEY, proxies={'http': ZAP_URL, 'https': ZAP_URL})

# Accès à l'URL cible
print(f"🌐 Accès à {TARGET_URL}")
zap.urlopen(TARGET_URL)
time.sleep(2)  # Laisse le temps à ZAP de capturer la cible

# 🚀 Lancement du Spider
print(f"🕷️ Lancement du Spider sur {TARGET_URL}")
scan_id = zap.spider.scan(TARGET_URL)
time.sleep(2)

# Suivi de la progression du Spider
while int(zap.spider.status(scan_id)) < 100:
    progress = zap.spider.status(scan_id)
    print(f"🕷️ Progression du Spider : {progress}%")
    time.sleep(2)

print("✅ Spider terminé avec succès !")

# 🚦 Lancement du scan actif après le Spider
print(f"🔥 Lancement du scan actif sur {TARGET_URL}")
scan_id = zap.ascan.scan(TARGET_URL)
time.sleep(2)

# Suivi de la progression du scan actif
while int(zap.ascan.status(scan_id)) < 100:
    progress = zap.ascan.status(scan_id)
    print(f"🔥 Progression du scan actif : {progress}%")
    time.sleep(5)

print("✅ Scan actif terminé avec succès !")

# ✅ Attente de la fin de l'analyse passive
while int(zap.pscan.records_to_scan) > 0:
    records_left = zap.pscan.records_to_scan
    print(f"🛡️ En attente de la fin de l'analyse passive : {records_left} enregistrements restants")
    time.sleep(2)

print("✅ Analyse passive terminée !")

# 📊 Récupération du rapport HTML
print("📄 Génération du rapport HTML...")
report = zap.core.htmlreport()
with open("zap_report.html", "w", encoding="utf-8") as file:
    file.write(report)

print("✅ Rapport ZAP généré : 'zap_report.html'")

# 💡 Affichage des alertes dans la console
alerts = zap.core.alerts()
if alerts:
    print("🚨 Alerte(s) détectée(s) :")
    pprint(alerts)
else:
    print("✅ Aucune alerte détectée !")

print("🏁 Test ZAP terminé avec succès !")
