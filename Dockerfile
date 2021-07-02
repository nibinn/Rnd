FROM python:3.6

COPY manage.py gunicorn-cfg.py requirements.txt .env ./
COPY app app
COPY authentication authentication
COPY core core

RUN pip install -r requirements.txt


EXPOSE 8005

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
