FROM python:3.7
WORKDIR /app
RUN pip3 install flask SQLalchemy Flask-SQLAlchemy
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]