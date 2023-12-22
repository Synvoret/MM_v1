FROM python:3.10
LABEL maintainer="Synvoret"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV PATH="/app/venv/bin:$PATH"

COPY ./app /app

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
