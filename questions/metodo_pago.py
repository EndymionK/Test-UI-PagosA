from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MetodoPago:
    @staticmethod
    def obtener_etiqueta(driver):
        metodo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-white.p-2.rounded-md"))
        )
        etiqueta = metodo.find_element(By.CSS_SELECTOR, "label")
        return etiqueta.text

    @staticmethod
    def verificar_mensaje_reserva_pagada(driver):
        mensaje_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Su reserva esta pagada y confirmada.')]"))
        )
        return mensaje_element.text
