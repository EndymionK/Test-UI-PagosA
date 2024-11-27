Feature: Desglose de costos al usuario
    Como pasajero,
    quiero ver un desglose de todos los costos y tarifas antes de realizar el pago
    para poder entender el monto total a pagar.

    Scenario Outline: Mostrar un desglose detallado de costos y tarifas
        Given que el pasajero está viendo la página de pago
        When el sistema muestra el desglose de costos
        Then debe mostrar todos los costos y tarifas detallados aplicados:
            | <key>             | <value>       |

        Examples:
            | key                | value         |
            | Precio de tickets  | 155.000 COP   |
            | Impuestos y cargos | 4.200 COP     |
            | Total              | 159.200 COP   |
