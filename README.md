## Technologies

All project dependencies are listed in [requirements.txt](requirements.txt) file.


## How to run tests
E.g.:
```bash
pytest --browser firefox -n 2 --alluredir=.\allure-results
```
where 
- ```--browser firefox``` is for running tests in e.g. firefox (*chrome* is used by default),
- ```--alluredir=.\allure-results``` is for generating .json tests results. Optional argument.
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

*NOTE*:
In case of allure related errors install allure according to :https://docs.qameta.io/allure/#_installing_a_commandline
```bash
allure --version
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





