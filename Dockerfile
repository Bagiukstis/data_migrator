FROM python:3.9
RUN mkdir -p /project/
RUN apt-get update
WORKDIR /project/
COPY requirements.txt /project/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /project/
ENV APP_ENV development
EXPOSE 4025
VOLUME ["/app-data"]
ENTRYPOINT ["python", "run.py"]