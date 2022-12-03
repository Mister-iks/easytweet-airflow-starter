FROM apache/airflow:2.4.3
USER root
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && apt-get install -y default-jdk && apt-get clean
USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
