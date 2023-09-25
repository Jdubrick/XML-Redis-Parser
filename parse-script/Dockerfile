FROM python:latest

WORKDIR /app

COPY main.py ./
COPY requirements.txt ./

RUN apt-get update -y

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]