from tasks.ver_desglose_costos import VerDesgloseCostos
from utils.browser_setup import get_driver
from selenium.common.exceptions import TimeoutException
from behave import given, then, when


@given("que el pasajero está viendo la página de pago")
def step_given_pagina_pago(context):
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/transaction-details?id=12")

@when("el sistema muestra el desglose de costos")
def step_when_muestra_desglose_costos(context):
    try:
        VerDesgloseCostos.esperar_desglose_visible(context.driver)
    except TimeoutException:
        raise AssertionError("No se encontró el desglose de costos en la página.")

@then("debe mostrar todos los costos y tarifas detallados aplicados")
def step_then_muestra_costos_detallados(context):
    """
    Verifica que los costos y tarifas mostrados en el desglose coincidan con los valores esperados
    proporcionados en la tabla de la feature.
    """
    # Convertir la tabla de la feature en un diccionario
    valores_esperados = {row["key"]: row["value"] for row in context.table}

    # Verificar los detalles del desglose usando los valores esperados
    VerDesgloseCostos.verificar_detalles(context.driver, valores_esperados)

@then("cerrar el navegador")
def step_close_browser(context):
    context.driver.quit()
