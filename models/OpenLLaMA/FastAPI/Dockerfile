FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

EXPOSE 80

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 80"]
