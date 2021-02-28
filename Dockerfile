FROM python:3.9.2-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
