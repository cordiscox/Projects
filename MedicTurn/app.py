from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from config import Config

account_sid = Config.account_sid
auth_token = Config.auth_token
twilio_number = Config.twilio_number
my_number = Config.my_number

client = Client(account_sid, auth_token)

driver = webdriver.Chrome()

try:
    driver.get("https://turnos.institutomedicodelosarroyos.com.ar/turnos-1.php")

    # Esperar hasta que el botón de ingreso esté presente y hacer clic
    ingresar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="caja-complementarios"]/div/a[1]'))
    )
    ingresar.click()

    # Esperar hasta que el combo de doctores esté presente
    select_doctor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cmbmedicos"]'))
    )
    select = Select(select_doctor)
    select.select_by_value("46")  # Cambia a "46" o el valor necesario

    # Esperar hasta que el botón "OK" esté presente y hacer clic
    ok_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="caja-complementarios"]/div[2]/img'))
    )
    ok_button.click()

    # Si no encuentra días, pasa al próximo mes
    try:
        dias = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="refdiapuntual"]'))
        )
    except TimeoutException:
        next_month = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'flecha-der-dia'))
        )
        next_month.click()

    disponibilidad = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'tooltip-style3'))
        )

    for dispo in disponibilidad:
        print(dispo.get_attribute("innerHTML"))
        if "DISPONIBLE" in dispo.get_attribute("innerHTML"):
            message = client.messages.create(
            from_= twilio_number,
            body='Hay Turno para la doctora',
            to=my_number
            )

finally:
    driver.quit()
