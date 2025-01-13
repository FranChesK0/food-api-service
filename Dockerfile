FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install --with dev

CMD ["poetry", "run", "python", "food/src/main.py"]

EXPOSE 8000
