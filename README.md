
Organge HRM automation using selenium python 


## Documentation

[Documentation](https://linktodocumentation)

this is a smoke suite for PIM module in Orange HRM 

frame work designed in page object model design with multi browser support

tools

python 3.11.1,
selenium,
pytest,
allure reporting




## Installation

install and set up python

setup IDE(pycharm)

for allure report

install java and setup JAVA_HOME

install allure

clone the project from master branch


run below commands

git clone https://github.com/honeysdet/PythonTechDemo.git

cd PythonTechDemo

git fetch origin master

git checkout  master

**********************
creating virtual env 

python -m pip install --user virtualenv

python -m venv myvenv

activate newly created virtual env

windows

.\myvenv\Scripts\activate

*********************
install all required packages


 pip install -r requirements.txt

********************

running test 

with html report

python -m pytest --html=report.html

report.html will be genearted in root directory


with allure report

python -m pytest --alluredir=allure-report/  

view report use below command 

allure serve allure-report/  

```
    
