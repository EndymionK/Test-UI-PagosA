from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from userinterfaces.reservas import ReservasUI  # Importa la clase ReservasUI

class SeleccionarReserva:
    @staticmethod
    def por_estado(driver, reservas, estado):
        for reserva in reservas:
            # Reemplazar la cadena de texto por la constante de ReservasUI
            if estado in reserva.find_element(By.CSS_SELECTOR, ReservasUI.ESTADO_RESERVA).text:
                SeleccionarReserva.por_elemento(driver, reserva)
                break

    @staticmethod
    def por_elemento(driver, elemento):
        actions = ActionChains(driver)
        actions.move_to_element(elemento).click().perform()
