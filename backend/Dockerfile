FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 80

ARG SECRET_KEY

ENV OPEN_AI_KEY=$OPEN_AI_KEY

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
