FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

WORKDIR /app
COPY . .

# logs 폴더 추가 (중요!)
RUN mkdir -p /app/logs

# Django 환경 설정 추가
ENV DJANGO_SETTINGS_MODULE=config.settings.local

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
