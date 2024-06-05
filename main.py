from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

# Webdriver-Optionen festlegen
options = webdriver.ChromeOptions()

# Undetected ChromeDriver verwenden
driver = uc.Chrome(options=options)

try:
    # Öffne die Webseite
    print("Öffne die Webseite...")
    driver.get("https://www.ligaportal.at/ooe/landesliga/landesliga-west/spieler-der-runde/105892-landesliga-west-2023-2024-waehle-den-bwin-spieler-der-runde-29")

    # Warte auf den iFrame des Cookie-Banners und wechsle hinein
    print("Warte auf den iFrame des Cookie-Banners...")
    cookie_iframe = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='privacymanager.io']"))
    )

    # Akzeptiere die Cookies
    print("Akzeptiere die Cookies...")
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "save"))
    )
    accept_cookies_button.click()

    # Wechsle zurück zum Hauptinhalt
    driver.switch_to.default_content()

    # Warte ein paar Sekunden, um sicherzustellen, dass alles geladen ist
    print("Warte auf das Laden der Seite...")
    time.sleep(5)

    # Überprüfe, ob das Element in einem weiteren iFrame vorhanden ist
    print("Überprüfe auf weitere iFrames...")
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            player_radio_button = driver.find_element(By.CSS_SELECTOR, "input[id='player-5356690']")
            break
        except:
            driver.switch_to.default_content()

    # Führe JavaScript aus, um den Radiobutton auszuwählen
    print("Wähle den Radiobutton per JavaScript aus...")
    script = """
    document.querySelector('input[id="player-5356690"]').checked = true;
    """
    driver.execute_script(script)

    # Warte ein paar Sekunden
    time.sleep(2)

    # Finde und klicke auf den Abstimmen-Button
    print("Warte auf den Abstimmen-Button und klicke darauf...")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='playerOneUp']"))
    )
    submit_button.click()

    print("Abstimmung erfolgreich abgeschlossen!")

finally:
    # Schließe den Webdriver
    print("Schließe den Webdriver...")
    driver.quit()
