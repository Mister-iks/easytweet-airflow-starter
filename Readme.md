# easytweet-airflow-starter

Is a subproject of the EasyTweet project which is a data collection and analysis python package that focuses on the social network twitter.
This sub-project named easytweet-airflow-starter is an implementation of some basic features of the package on Apache Airflow.

### Built with

| techno         | version |
| -------------- | ------- |
| Python         | 3.9.13  |
| Apache airflow | 2.4.3   |
| Pyspark        | 3.3.1   |
| Tweepy         | 4.12.1  |

# Installing / Getting started

## Prerequisites

Before starting the project, make sure that you

- have at least python3 installed
- installed the spark

## Setting up Dev

```
  git pull
```

## Building

```
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

```
docker build . --tag extending_airflow:latest
docker-compose up airflow-init
docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler
```

## Starting

To start the project run

```
docker compose-up
```

and open your browser then go to localhost:8080

## NB : If you have any problems, write to me ibrahimapro289@gmail.com
