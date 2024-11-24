from behave import given, then, when
from utils.browser_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# Feature: Integración Pago Web ----------------------------------------------

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


@given("que el pasajero tiene una reserva pendiente")
def step_given_reserva_pendiente(context):
    """Navega a la página de reservas y asegura que existe al menos una reserva pendiente."""
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=2")

       # Espera hasta que los elementos de reserva estén visibles en la página
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a > div.border"))
    )

    # Espera y verifica que haya reservas en la página
    reservas = context.driver.find_elements(By.CSS_SELECTOR, "a > div.border")
    assert len(reservas) > 0, "No se encontraron reservas en la página."

    # Encuentra una reserva pendiente
    context.reserva_pendiente = None
    for reserva in reservas:
        estado_element = reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div")
        if "Pendiente" in estado_element.text:
            context.reserva_pendiente = reserva
            break

    assert context.reserva_pendiente, "No se encontró ninguna reserva pendiente."

@when("selecciona la reserva pendiente")
def step_when_selecciona_reserva(context):
    """Da clic en la reserva pendiente."""
    assert context.reserva_pendiente, "No hay reserva pendiente seleccionada."
    actions = ActionChains(context.driver)
    actions.move_to_element(context.reserva_pendiente).click().perform()

    # Verifica que se cargue la página correcta
    assert "transaction-details" in context.driver.current_url, "No se cargó la página de detalles de la transacción."

@then("debe poder elegir un método de pago para la transacción.")
def step_then_verifica_metodo_pago(context):
    try:
        # Seleccionar el contenedor del método de pago
        metodo = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-white.p-2.rounded-md"))
        )

        # Buscar un label dentro del contenedor del método de pago
        etiqueta = WebDriverWait(metodo, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label"))
        )
        
        # Imprimir el texto del label encontrado
        print(f"Etiqueta encontrada: {etiqueta.text}")

    except TimeoutException:
        # Imprimir el HTML del contenedor si falla la búsqueda
        metodo_html = metodo.get_attribute('outerHTML') if metodo else "Contenedor no encontrado"
        print(f"HTML del método de pago: {metodo_html}")
        raise AssertionError("No se pudo encontrar el elemento 'label' dentro del método de pago.")
    
@given("que el pasajero tiene una reserva pagada")
def step_given_reserva_pagada(context):
    """Navega a la página de reservas y asegura que existe al menos una reserva pagada."""
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=2")

       # Espera hasta que los elementos de reserva estén visibles en la página
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a > div.border"))
    )

    # Espera y verifica que haya reservas en la página
    reservas = context.driver.find_elements(By.CSS_SELECTOR, "a > div.border")
    assert len(reservas) > 0, "No se encontraron reservas en la página."

    # Encuentra una reserva pagada
    context.reserva_pagada = None
    for reserva in reservas:
        estado_element = reserva.find_element(By.CSS_SELECTOR, "div.mb-4 > div")
        if "Pagado" in estado_element.text:
            context.reserva_pagada = reserva
            break

    assert context.reserva_pagada, "No se encontró ninguna reserva pagada."

@when("selecciona la reserva pagada")
def step_when_selecciona_reserva(context):
    """Da clic en la reserva pagada."""
    assert context.reserva_pagada, "No hay reserva pagada seleccionada."
    actions = ActionChains(context.driver)
    actions.move_to_element(context.reserva_pagada).click().perform()

    # Verifica que se cargue la página correcta
    assert "transaction-details" in context.driver.current_url, "No se cargó la página de detalles de la transacción."

@then("no debe poder elegir un método de pago para la transacción.")
def step_then_no_metodo_pago(context):
    try:
        # Verificar si el mensaje "Su reserva esta pagada y confirmada." está presente
        mensaje_reserva_pagada = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Su reserva esta pagada y confirmada.')]"))
        )
        print(f"Mensaje encontrado: {mensaje_reserva_pagada.text}")

    except TimeoutException:
        print("No se encontró el mensaje de reserva pagada.")


# Feature: Desglose de costos al usuario ----------------------------------------------

@given("que el pasajero está viendo la página de pago")
def step_given_pagina_pago(context):
    """Navega directamente a la página de 'Mis pagos'."""
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/transaction-details?id=12") 

@when("el sistema muestra el desglose de costos")
def step_when_muestra_desglose_costos(context):
    # Esperamos a que el desglose de costos sea visible
    try:
        desglose_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-xl.border.text-card-foreground.shadow"))
        )
        print("Desglose de costos visible en la página.")
    except TimeoutException:
        raise AssertionError("No se encontró el desglose de costos en la página.")

@then("debe mostrar todos los costos y tarifas detallados aplicados")
def step_then_muestra_costos_detallados(context):
    try:
        # Espera explícita para el resumen de compra
        resumen_compra = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-xl.border.text-card-foreground.shadow"))
        )
        
        # Verificar el precio de los tickets
        precio_tickets = resumen_compra.find_element(By.XPATH, "//ul/li/span[normalize-space(text())='Precio de tickets']/following-sibling::span")
        assert "155.000 COP" in precio_tickets.text, f"Se esperaba '155.000 COP', pero se encontró: {precio_tickets.text}"

        # Verificar impuestos y cargos
        impuestos_cargos = resumen_compra.find_element(By.XPATH, "//ul/li/span[normalize-space(text())='Impuestos y cargos']/following-sibling::span")
        assert "4.200 COP" in impuestos_cargos.text, f"Se esperaba '4.200 COP', pero se encontró: {impuestos_cargos.text}"

        # Verificar el total
        total = resumen_compra.find_element(By.XPATH, "//li[span[contains(text(), 'Total')]]/span[2]")
        assert "159.200 COP" in total.text, f"Se esperaba '159.200 COP', pero se encontró: {total.text}"

        print("Desglose de costos verificado correctamente.")

    except AssertionError as e:
        print(f"Error de verificación: {e}")
        raise

@then("cerrar el navegador")
def step_close_browser(context):
    """Cierra el navegador después de las pruebas."""
    context.driver.quit()
