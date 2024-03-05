# Automation for mobile testing
## Python, Behave & Appium ( skeleton )

This is an example of how to run Appium on a local Android machine.
The example is based on several BDD test scenario.

# Requirements.

* Python 3.10.X
* pip and setuptools
* [venv](`https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/`) (recommended)

#### Location of feature files:

    *.feature = (/features/tests/*.feature)

#### Location of steps files: **.py = (/features/tests/*.feature)

    *.py = (/features/steps/*.py)

#### Location of page files

    *.py = (/features/pages/*.py)

#### File Description base_page.py file
1.def() find_element : function that finds the selector in the page.
2.def() click_on_element : function that locates and clicks the selector on the page.
3.def() input : function that locates the field selector to write in it.
4def() implicit_wait_visible : function that waits for the selector to be visible on the page.

#### App
The test cases are executed in the app "rutadigital" which is located: 
(/src/binaries/app-route-digital.apk).

#### How to run:  
Go to project root folder "appium-python-automation" 2.  
2. Add credentials.py (/features/credentials.py)  
``` credentials.py 
NAME = "Test"  
BODY = "Example"  
```  
3. Update desired capabilities for Android (/features/environment.py)  
4. Execute command: "behave -f html -o results/behave-report.html".

Translated with DeepL.com (free version)

#### Results

1. A results file (behave-report.html) will be generated in the "/results" folder.
  

## Guide to Running and Generating Reports with Behave and Allure:


### Running Tests with Behave:

To run tests using Behave, use the following command in your terminal:

`behave -f html -o results/behave-report.html`. 

This command will run the tests and generate a report in HTML format at the specified location.

### Generating Reports with Allure:

To generate detailed reports using Allure, run the following command after running the tests with Behave:

`behave -f allure_behave.formatter:AllureFormatter -o ./reports/` 

This command will generate the Allure reports in the specified folder.

### Viewing Reports with Allure:

Once you have generated the Allure reports, you can easily view them using the following command in your terminal:

`allure serve ./reports/`  

This command will open a local server and launch a web browser to view the reports generated by Allure.
  
  
#### Useful links:  
- https://www.swtestacademy.com/how-to-install-appium-on-mac/  
- https://automated-testing.info/t/mobilnaya-avtomatizacziya-s-appium-opyt-napisaniya-pervogo-testa/17221  
- https://www.youtube.com/watch?v=jnKd6PRhmDY