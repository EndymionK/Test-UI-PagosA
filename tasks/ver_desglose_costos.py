from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from userinterfaces.pago import PagoUI

class VerDesgloseCostos:
    @staticmethod
    def esperar_desglose_visible(driver):
        """
        Espera hasta que el desglose de costos sea visible en la página.
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, PagoUI.DESGLOSE_COSTOS))  # Usamos la variable DESGLOSE_COSTOS
        )

    @staticmethod
    def verificar_detalles(driver, valores_esperados):
        """
        Verifica los valores del desglose de costos contra los valores esperados.

        Args:
            driver: WebDriver activo.
            valores_esperados: Diccionario con los valores esperados. Ejemplo:
                               {"Precio de tickets": "155.000 COP", "Total": "159.200 COP"}
        """
        desglose = driver.find_element(By.CSS_SELECTOR, PagoUI.DESGLOSE_COSTOS)  # Usamos la variable DESGLOSE_COSTOS
        
        for key, value in valores_esperados.items():
            # Localizar el valor asociado a la clave en el desglose
            elemento = desglose.find_element(By.XPATH, f"//span[normalize-space(text())='{key}']/following-sibling::span")
            assert value in elemento.text, f"Se esperaba '{value}' para '{key}', pero se encontró: {elemento.text}"
