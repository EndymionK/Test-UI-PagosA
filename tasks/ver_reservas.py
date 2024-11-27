from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VerReservas:
    @staticmethod
    def obtener_reservas(driver):
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a > div.border"))
        )
        return driver.find_elements(By.CSS_SELECTOR, "a > div.border")

    @staticmethod
    def verificar_estados_reservas(reservas):
        estados = [reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div").text for reserva in reservas]
        assert "Pendiente" in estados, "No se encontró ninguna reserva pendiente."
        assert "Pagado" in estados, "No se encontró ninguna reserva pagada."

    @staticmethod
    def obtener_reserva_por_estado(driver, estado_deseado):
        reservas = VerReservas.obtener_reservas(driver)
        for reserva in reservas:
            estado = reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div").text
            if estado_deseado in estado:
                return reserva
        return None
