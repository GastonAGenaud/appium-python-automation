from appium import webdriver
from src.application import Application
import os
import json
import base64
import allure

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO_DIR = os.path.join(basedir, "videos")

# Crear el directorio de videos si no existe
if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)

def before_scenario(context, scenario):
    # Leer la configuración del archivo config.json
    with open(os.path.join(basedir, 'config.json')) as config_file:
        config = json.load(config_file)

    # Iniciar el driver de Appium con las capacidades deseadas
    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        desired_capabilities=config['target']['capabilities']
    )

    # Establecer un tiempo de espera implícito
    context.driver.implicitly_wait(30)

    # Inicializar la aplicación
    context.app = Application(context.driver)

    # Iniciar la grabación de la pantalla
    context.driver.start_recording_screen()

def after_scenario(context, scenario):
    # Detener la grabación de la pantalla
    video_data = context.driver.stop_recording_screen()

    # Asegurarse de que el nombre del archivo sea válido
    video_filename = f"{scenario.name}.mp4".replace(" ", "_").replace('"', '').replace("'", '')
    video_path = os.path.join(VIDEO_DIR, video_filename)

    # Guardar el video en un archivo
    with open(video_path, "wb") as video_file:
        video_file.write(base64.b64decode(video_data))

    # Adjuntar el video al reporte de Allure
    with open(video_path, "rb") as video_file:
        allure.attach(video_file.read(), name=f"{scenario.name}", attachment_type=allure.attachment_type.MP4)

    # Cerrar el driver
    context.driver.quit()