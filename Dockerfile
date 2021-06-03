FROM python:3.8
ADD . /srv
WORKDIR /srv
ARG file
RUN pip install -r requirements.txt
CMD ["python", "flask_rest_api.py"]