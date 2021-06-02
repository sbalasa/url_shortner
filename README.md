# url_shortner
This is a Web service and REST API service to shorten a very long url.

## To Prepare Environment
#### Run:
- `pip3 install -r requirements.txt`

## To Test
#### Run:
- `pytest -v`

## How to Execute
#### As a Web service
- `python3 flask_runner.py`
- Open the browser `http://localhost:8080/`

#### As a REST API Service
- Open a terminal `python3 flask_rest_api.py`
- Open a new terminal and call curl commands Eg: `curl http://localhost:8080/ -X POST -d '{"long_url": "http://thisistesting.com/"}'`
