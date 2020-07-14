FROM python:3.6
MAINTAINER Artem Averin
ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["example_rest.py"]
EXPOSE 5000
