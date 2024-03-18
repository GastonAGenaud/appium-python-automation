# Automation for mobile testing
## Python, Behave &amp; Appium ( skeleton )

This is example how to run appium on local machin for Android.
Example is based on BDD Test Scenario (Successful Login).

#### How to run:
1. Go to project root folder "appium-python-automation"
2. Add credentials.py (/features/credentials.py)
``` credentials.py 
PHONE=''
PASSWORD=''
```
3. Update desired capabilities for Android (/features/environment.py)
4. Execute command: "behave"


#### Environment:
- macOS Mojave 
- Python 3.7.2 
- appium 1.16.0
- device Android 11

#### Useful links:
- https://www.swtestacademy.com/how-to-install-appium-on-mac/
- https://automated-testing.info/t/mobilnaya-avtomatizacziya-s-appium-opyt-napisaniya-pervogo-testa/17221
- https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_1

### Capabilities used in this test:
            'platformName': 'android',
            'platformVersion': '14.0',
            'deviceName': 'Pixel XL API 34',
            'automationName': 'UiAutomator2',
            'app': basedir + r'/Android_Appium_Demo.apk',
            'appPackage': 'com.skill2lead.appiumdemo',

#### Device specifications:
- AVD Pixel XL API 34
- Android 14.0

### Command to run the tests:
"behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure/ -f pretty -o ./AppiumPython/appium-python-automation\features\tests"   

"behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure/"