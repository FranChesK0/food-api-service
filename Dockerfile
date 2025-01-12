FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install poetry

RUN poetry shell
RUN poetry install --with dev

COPY . .

CMD ["python", "food/src/main.py"]

EXPOSE 8000
