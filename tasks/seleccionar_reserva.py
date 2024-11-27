from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class SeleccionarReserva:
    @staticmethod
    def por_estado(driver, reservas, estado):
        for reserva in reservas:
            if estado in reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div").text:
                SeleccionarReserva.por_elemento(driver, reserva)
                break

    @staticmethod
    def por_elemento(driver, elemento):
        actions = ActionChains(driver)
        actions.move_to_element(elemento).click().perform()
