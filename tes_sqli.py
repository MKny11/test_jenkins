import subprocess

# URL cible
TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html"

# Options sqlmap
options = [
    "--batch",  # Mode automatique (pas d'interaction manuelle)
    "--risk", "3",  # Niveau de risque (1 = faible, 3 = élevé)
    "--level", "5",  # Niveau de profondeur (1 = bas, 5 = élevé)
    "--tamper", "space2comment",  # Technique de contournement (facultatif)
    "--random-agent",  # Utilise un User-Agent aléatoire
    "--dbs",  # Recherche des bases de données disponibles
]

# Commande complète
command = ["python", "sqlmap.py", "-u", TARGET_URL] + options

# Lancer la commande
print(f"📡 Lancement de sqlmap sur {TARGET_URL}...")
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Lire la sortie en temps réel
with open("sqlmap_report.txt", "w") as report:
    for line in process.stdout:
        decoded_line = line.decode('utf-8')
        print(decoded_line, end="")  # Affiche en console
        report.write(decoded_line)  # Écrit dans le fichier

# Vérifier si le processus a terminé correctement
return_code = process.wait()
if return_code == 0:
    print("\n✅ Test terminé avec succès ! Rapport généré dans 'sqlmap_report.txt'")
else:
    print("\n❌ Une erreur est survenue. Consulte le rapport pour plus de détails.")

