Feature: Proceso completo de pago
  Como usuario
  Quiero seleccionar un vuelo, pagar y recibir una confirmación
  Para completar mi reserva con éxito.

  Scenario: Reserva exitosa de un vuelo
    Given que el usuario navega al sitio web de reservas
    And que el pasajero tiene una reserva pendiente
    When selecciona la reserva pendiente
    And elige un método de pago y da click en pagar
    And completa los datos de pago
    Then debería recibir una confirmación de reserva
