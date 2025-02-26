from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Lancer le navigateur Chrome
driver = webdriver.Chrome()

# Accéder au site web à tester
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# Attendre 3 secondes
time.sleep(3)

# Cliquer sur un bouton (exemple)
try:
    bouton = driver.find_element(By.ID, "btnTest")
    bouton.click()
    print("Bouton cliqué avec succès")
except:
    print("Erreur : Bouton introuvable")

# Fermer le navigateur
driver.quit()
