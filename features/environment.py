from appium import webdriver
from src.application import Application
import os
import json

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def before_scenario(context, scenario):
    try:
        with open(os.path.join(basedir, 'config.json')) as config_file:
            config = json.load(config_file)

        apk_path = os.path.join(basedir, config.get('target', {}).get('capabilities', {}).get('app', ''))

        if apk_path:
            config['target']['capabilities']['app'] = apk_path

            context.driver = webdriver.Remote(
                "http://127.0.0.1:4723",
                desired_capabilities=config['target']['capabilities']
            )

            context.driver.implicitly_wait(30)
            context.app = Application(context.driver)
        else:
            print("Error: No se pudo encontrar la ruta del APK en el archivo de configuración.")
    except FileNotFoundError:
        print("Error: El archivo de configuración 'config.json' no se encuentra en el directorio correcto.")
    except Exception as e:
        print(f"Error inesperado al inicializar el controlador de Appium: {e}")


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver is not None:
        context.driver.quit()