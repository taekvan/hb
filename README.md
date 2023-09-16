## Technologies

All project dependencies are listed in [requirements.txt](requirements.txt) file.


## Preparation
1) Use python version 3.10 and above
2) install requirements
```bash
pip install -r requirements.txt
```
3) install allure according to :https://docs.qameta.io/allure/#_installing_a_commandline. Check allure version:
```bash
allure --version
```

## How to run tests
E.g.:
```bash
pytest --browser chrome -n 2 --alluredir=.\allure-results
```
where 
- ```--browser chrome``` runs tests in chrome browser. Possible values [chomre, firefox] (*chrome* is used by default). Optional argument,
- ```--alluredir=.\allure-results``` is for generating .json tests results. Optional argument,
- ```-n 2``` run tests in 2 parallel threads. Optional argument.

## Reports
To generate allure report execute the following command after tests run:
```bash
allure generate --clean
```
Generated report will be placed in ```allure-report``` folder.
To see the results run:
```bash
allure serve allure-results
```

## Screenshots
Screenshots are managed by Selenium and attached to allure-reports in hooks listed in [conftest.py](conftest.py) file.


## Environment configuration
[Python-dotenv](https://github.com/theskumar/python-dotenv)

Environment variables are listed in [.env](.env) file.

Variables usage, e.g.:
```python
import os
from dotenv import load_dotenv

load_dotenv()
APP_URL = os.getenv("APP_URL")
```

## Code analysis
[Flake8 Guide](https://flake8.pycqa.org/en/latest/)

To run code analysis:
```bash
python -m flake8
```
Flake8 configuration is placed in [.flake8](.flake8) file.





