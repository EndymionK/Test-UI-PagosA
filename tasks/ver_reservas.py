from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from userinterfaces.reservas import ReservasUI  # Importamos las variables de reservas

class VerReservas:
    @staticmethod
    def obtener_reservas(driver):
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ReservasUI.TARJETAS_RESERVA))  # Usamos la variable TARJETAS_RESERVA
        )
        return driver.find_elements(By.CSS_SELECTOR, ReservasUI.TARJETAS_RESERVA)  # Usamos la variable TARJETAS_RESERVA

    @staticmethod
    def verificar_estados_reservas(reservas):
        estados = [reserva.find_element(By.CSS_SELECTOR, ReservasUI.ESTADO_RESERVA).text for reserva in reservas]  # Usamos la variable ESTADO_RESERVA
        assert "Pendiente" in estados, "No se encontró ninguna reserva pendiente."
        assert "Pagado" in estados, "No se encontró ninguna reserva pagada."

    @staticmethod
    def obtener_reserva_por_estado(driver, estado_deseado):
        reservas = VerReservas.obtener_reservas(driver)
        for reserva in reservas:
            estado = reserva.find_element(By.CSS_SELECTOR, ReservasUI.ESTADO_RESERVA).text  # Usamos la variable ESTADO_RESERVA
            if estado_deseado in estado:
                return reserva
        return None
    