from behave import given, then, when
from tasks.ver_reservas import VerReservas
from tasks.seleccionar_reserva import SeleccionarReserva
from questions.metodo_pago import MetodoPago
from utils.browser_setup import get_driver
from selenium.common.exceptions import TimeoutException

@given('que el pasajero ya está en la sección "Mis reservas"')
def step_user_on_reservas(context):
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=1")

@then("debería poder ver las reservas marcadas como pendientes, pagadas o canceladas.")
def step_verify_reservas(context):
    reservas = VerReservas.obtener_reservas(context.driver)
    VerReservas.verificar_estados_reservas(reservas)

@given("que el pasajero tiene una reserva pendiente")
def step_given_reserva_pendiente(context):
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=4")
    context.reserva_pendiente = VerReservas.obtener_reserva_por_estado(context.driver, "Pendiente")
    assert context.reserva_pendiente, "No se encontró ninguna reserva pendiente."

@when("selecciona la reserva pendiente")
def step_when_selecciona_reserva(context):
    SeleccionarReserva.por_elemento(context.driver, context.reserva_pendiente)

@then("debe poder elegir un método de pago para la transacción.")
def step_then_verifica_metodo_pago(context):
    try:
        etiqueta_metodo = MetodoPago.obtener_etiqueta(context.driver)
        print(f"Etiqueta encontrada: {etiqueta_metodo}")
    except TimeoutException as e:
        print(f"Error: {e}")
        raise AssertionError("No se pudo encontrar el método de pago.")

@given("que el pasajero tiene una reserva pagada")
def step_given_reserva_pagada(context):
    context.driver = get_driver()
    context.driver.get("https://pagos-a.vercel.app/pagos-A/bookings?userId=2")
    context.reserva_pagada = VerReservas.obtener_reserva_por_estado(context.driver, "Pagado")
    assert context.reserva_pagada, "No se encontró ninguna reserva pagada."

@when("selecciona la reserva pagada")
def step_when_selecciona_reserva_pagada(context):
    SeleccionarReserva.por_elemento(context.driver, context.reserva_pagada)

@then("no debe poder elegir un método de pago para la transacción.")
def step_then_no_metodo_pago(context):
    mensaje = MetodoPago.verificar_mensaje_reserva_pagada(context.driver)
    assert mensaje == "Su reserva esta pagada y confirmada.", "El mensaje esperado no fue encontrado."
