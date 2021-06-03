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

## How to Execute via Docker
- Build the docker image `docker build -t url_shortner .` or Download from `docker pull sbalasa/url_shortner:2021`
- Verify if the image is created/available `docker image ls`
- Run it in a Docker container `docker run url_shortner` or `docker run sbalasa/url_shortner:2021` (if image is downloaded from docker hub)
- Open a new terminal and call curl commands Eg: `curl http://<ip shown by the container>:8080/ -X POST -d '{"long_url": "http://thisistesting.com/"}'`
