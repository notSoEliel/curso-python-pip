FROM python:3.12.4

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# this will run the main.py file in the app directory and expose port 80 to the host machine within the container. using uvicorn as the server for the API.
