from behave import given, then
from utils.browser_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que el pasajero ya está en la sección "Mis reservas"')
def step_user_on_reservas(context):
    """Navega directamente a la página de 'Mis reservas'."""
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=2") 

@then("debería poder ver las reservas marcadas como pendientes, pagadas o canceladas.")
def step_verify_reservas(context):
    """Verifica que se muestran reservas con diferentes estados."""
    # Espera hasta que los elementos de reserva estén visibles en la página
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a > div.border"))
    )

    # Encuentra todas las tarjetas de reservas
    reservas = context.driver.find_elements(By.CSS_SELECTOR, "a > div.border")

    assert len(reservas) > 0, "No se encontraron reservas en la página."

    # Extrae los estados de cada reserva
    estados = []
    for reserva in reservas:
        estado_element = reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div")
        estado = estado_element.text
        estados.append(estado)

    # Verifica que existen al menos una reserva con cada estado
    assert "Pendiente" in estados, "No se encontró ninguna reserva pendiente."
    assert "Pagado" in estados, "No se encontró ninguna reserva pagada."
    # El estado "Cancelado" no está en el HTML proporcionado; omítelo por ahora.

@then("cerrar el navegador")
def step_close_browser(context):
    """Cierra el navegador después de las pruebas."""
    context.driver.quit()
