class PagoUI:
    DESGLOSE_COSTOS = ".rounded-xl.border.text-card-foreground.shadow"
    PRECIO_TICKETS = "//ul/li/span[normalize-space(text())='Precio de tickets']/following-sibling::span"
    IMPUESTOS_CARGOS = "//ul/li/span[normalize-space(text())='Impuestos y cargos']/following-sibling::span"
    TOTAL = "//li[span[contains(text(), 'Total')]]/span[2]"
    CONTENEDOR_METODO_PAGO = ".bg-white.p-2.rounded-md"
    LABEL_METODO_PAGO = "label"
