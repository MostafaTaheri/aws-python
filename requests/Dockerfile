FROM 127.0.0.1:8003/at-python-api:v1.4
RUN apk add --no-cache tzdata
ENV TZ Asia/Tehran
RUN echo "Asia/Tehran" > /etc/timezone

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8007
CMD uvicorn --host 0.0.0.0 --port 8007 main:app
