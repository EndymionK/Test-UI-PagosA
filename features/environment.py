def before_all(context):
    print("Iniciando pruebas con Behave y Selenium")

def after_all(context):
    print("Pruebas completadas.")
    if hasattr(context, 'driver'):
        context.driver.quit()
