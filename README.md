# Automatización para pruebas móviles
## Python, Behave y Appium (esqueleto)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=alert_status&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=sqale_rating&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=security_rating&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=bugs&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=vulnerabilities&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=duplicated_lines_density&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=reliability_rating&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=sqale_index&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=coverage&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=ncloc&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=koandina_app-ruta-digital-qa-movil&metric=code_smells&token=8472b9ab0f0bfa62d4725b0576f9d74c9cfb5274)](https://sonarcloud.io/summary/new_code?id=koandina_app-ruta-digital-qa-movil)

Este es un ejemplo de cómo ejecutar Appium en una máquina Android local.
El ejemplo se basa en varios escenarios de prueba BDD.

# Requisitos.
* instalación del controlador de appium uiautomator2
* ANDROID_HOME = \AppData\Local\Android\Sdk https://developer.android.com/studio/command-line/variables
* Python 3.10.X
* pip y setuptools
* [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (recomendado)

#### Ubicación de los archivos de características:

    *.feature = (/features/tests/*.feature)

#### Ubicación de los archivos de pasos: **.py = (/features/tests/*.feature)

    *.py = (/features/steps/*.py)

#### Ubicación de los archivos de página

    *.py = (/features/pages/*.py)

#### Descripción del archivo base_page.py
1. def() find_element: función que encuentra el selector en la página.
2. def() click_on_element: función que localiza y hace clic en el selector de la página.
3. def() input: función que localiza el selector del campo para escribir en él.
4. def() implicit_wait_visible: función que espera a que el selector sea visible en la página.

#### Aplicación
Los casos de prueba se ejecutan en la aplicación "rutadigital" que se encuentra en:
(/src/binaries/app-MiRuta.apk).

#### Cómo ejecutar:
1. Ir a la carpeta raíz del proyecto "app-ruta-digital-qa-movil".
2. Actualizar las capacidades deseadas para Android (/features/environment.py)
3. Ejecutar el comando: "behave -f html -o results/behave-report.html".

#### Resultados

1. Se generará un archivo de resultados (behave-report.html) en la carpeta "/results".

## Guía para ejecutar y generar informes con Behave y Allure:

### Ejecutar pruebas con Behave:

Para ejecutar pruebas usando Behave, usa el siguiente comando en tu terminal:

`behave -f html -o results/behave-report.html`.

Este comando ejecutará las pruebas y generará un informe en formato HTML en la ubicación especificada.

### Generar informes con Allure:

Para generar informes detallados usando Allure, ejecuta el siguiente comando después de ejecutar las pruebas con Behave:

`behave -f allure_behave.formatter:AllureFormatter -o ./reports/`

Este comando generará los informes de Allure en la carpeta especificada.

### Ver informes con Allure:

Una vez que hayas generado los informes de Allure, puedes verlos fácilmente usando el siguiente comando en tu terminal:

`allure serve ./reports/`

Este comando abrirá un servidor local y lanzará un navegador web para ver los informes generados por Allure.