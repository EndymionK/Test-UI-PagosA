Feature: Integración Pago Web
  Como pasajero registrado,
  Quiero pagar mis reservas directamente en el sitio web
  para poder completar el proceso de manera eficiente.

  Scenario: El pasajero visualiza y selecciona reservas pendientes, pagadas o canceladas
    Given que el pasajero ya está en la sección "Mis reservas"
    Then debería poder ver las reservas marcadas como pendientes, pagadas o canceladas.

  Scenario: El pasajero selecciona la reserva y el método de pago
    Given que el pasajero tiene una reserva pendiente
    When selecciona la reserva pendiente
    Then debe poder elegir un método de pago para la transacción.

  Scenario: El pasajero selecciona la reserva y el método de pago
    Given que el pasajero tiene una reserva pagada
    When selecciona la reserva pagada
    Then no debe poder elegir un método de pago para la transacción. 
