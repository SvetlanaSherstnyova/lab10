# первый этап
FROM python:3.10.0-slim AS builder
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

# второй этап для multi-stage
FROM python:3.10.0-slim  AS working

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /app /app

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata blog_dump.json \
    && python manage.py runserver 0.0.0.0:8000
