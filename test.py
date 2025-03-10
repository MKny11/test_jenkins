from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Options pour Firefox
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran

# Chemin vers le geckodriver
driver = webdriver.Firefox(executable_path="K://M1_MIAGE//JENKINS//geckodriver.exe", options=firefox_options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Vérifier le titre de la page
print("Titre de la page:", driver.title)

# Augmenter l'attente implicite
driver.implicitly_wait(3)

# Trouver les éléments
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
text_box = driver.find_element(By.NAME, "my-text")
password_box = driver.find_element(By.NAME, "my-password")
textarea_box = driver.find_element(By.NAME, "my-textarea")

disabled_box = driver.find_element(By.NAME, "my-disabled")
readonly_box = driver.find_element(By.NAME, "my-readonly")

select_element = driver.find_element(By.NAME, "my-select")
datalist = driver.find_element(By.NAME, "my-datalist")
datalist_value = driver.find_element(By.ID, "my-options")

file_input = driver.find_element(By.NAME, "my-file")

checkbox = driver.find_element(By.NAME, 'my-check')
checkbox_2 = driver.find_element(By.ID, 'my-check-2')
radio = driver.find_element(By.NAME, 'my-radio')

color = driver.find_element(By.NAME, 'my-colors')
date = driver.find_element(By.NAME, 'my-date')
slider = driver.find_element(By.NAME, 'my-range')

link = driver.find_element(By.LINK_TEXT, "Return to index")

# Remplir le champ et soumettre
text_box.send_keys("Selenium")
password_box.send_keys("p123iop34")
textarea_box.send_keys("champs de saisie pour selenium")

# Vérifier les champs désactivés et readonly
if disabled_box.get_attribute("disabled"):
    print("Le champ disabled est désactivé.")
else:
    print("Le champ disabled est actif.")

if readonly_box.get_attribute("readonly"):
    print("Le champ readonly est activé.")
else:
    print("Le champ readonly est désactivé.")

# Sélectionner une valeur dans la liste déroulante
select = Select(select_element)
select.select_by_value("2")

# Remplir une valeur dans le datalist
options = datalist_value.find_elements(By.TAG_NAME, "option")
values = [option.get_attribute("value") for option in options]
datalist.send_keys(values[3])

# Télécharger un fichier
file_input.send_keys("C:/Users/Utilisateur/Pictures/Capture.png")

# Cocher les cases et le bouton radio
checkbox.click()
checkbox_2.click()
radio.click()

# Sélectionner une couleur et une date
color.send_keys('#0000FF')
date.send_keys('2030-12-02')

# Déplacer le slider à une valeur spécifique (exemple : 8)
driver.execute_script("arguments[0].value = 8;", slider)

# Envoi du formulaire
submit_button.click()

# Attendre le message après soumission du formulaire
try:
    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    print("Message après soumission:", message.text)
except:
    print("Le message n'est pas apparu à temps.")

# Fermer le navigateur
driver.quit()
