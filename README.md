# Backend-practice-flask

Technique:

Flask + PostgreSQL

- Flask-Restfulplus
- SQLAlchemy
- Mixin CRUD on my own
- SocketIO
- Kafka
- CI/CD with Jenkins and GitHub WebHook
- pre-commit check
- GraphQL


## Set up

#### PostgreSQL Database:

For Dev Env
```bash
$ export DATABASE_URL="postgresql://[username]@[host]:[port]/[database]"
```

For Test Env
```bash
$ export DATABASE_URL_TEST="postgresql://[username]@[host]:[port]/[database]"
```

### Install Python Packages
```bash
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt
```

## Start Application


1. Database Initialization

```bash
# step 1: initializing
$ python manage.py db init


# step 2: migrate new model setting
$ python manage.py db migrate --message 'initial database'

# step 3: exec new model
$ python manage.py db upgrade
```
Once modifying the models, run the step 2 and 3.

2. Run the Application
```bash
$ python manage.py run
```

3. Run the Unit Test
```bash
$ python manage.py test
```

## Pre-Commit Settings
Check the coding style and run the unit test before committing.
```bash
$ vim .pre-commit-config.yaml
```

## Kafka

1. Environment Setting
start the kafka server
```bash
$ git clone https://github.com/wurstmeister/kafka-docker
```

modify the docker compose file (Mac OS)
```bash
# retrieve the docker host
$ export DOCKERHOST=$(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d: | head -n1)

# modify the compose file
$ vim docker-compose.yml
```

```yml
version: '3.4'
services:
  zookeeper:
    image: wurstmeister/zookeeper:3.4.6
    ports:
      - 2181:2181
    healthcheck:
      test: ["CMD", "/opt/zookeeper/zkServer.sh", "status"]
      interval: 5s
      timeout: 5s
      retries: 3
    volumes:
      - ./data/zookeeper:/opt/zookeeper/data
  kafka:
    image: wurstmeister/kafka:0.10.0.0
    ports:
      - 9092:9092
    environment:
      KAFKA_PORT: 9092
      KAFKA_DELETE_TOPIC_ENABLE: "true"
      KAFKA_BROKER_ID: 0
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_ADVERTISED_HOST_NAME: "${DOCKERHOST}"
      KAFKA_ADVERTISED_LISTENERS: "PLAINTEXT://${DOCKERHOST}:9092"
      KAFKA_ZOOKEEPER_CONNECT: "${DOCKERHOST}:2181"
      KAFKA_LOG_DIRS: /kafka/logs
    depends_on:
      - zookeeper
    volumes:
      - ./data/kafka/:/kafka/
    extra_hosts:
      - "dockerhost:$DOCKERHOST"
```

2. Add Topic
```bash
$ docker network ls

$ docker run --network [container id] -it kafka-docker_kafka bash
```

3. Try producer and consumer

In the Kafka Container
```bash
$ cd /opt/kafka/bin/

$ kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic [topic name]
```

Listen on topic
```bash
$ kafka-console-consumer.sh --bootstrap-server kafka:9092 --from-beginning --topic [topic name]
```
Open another bash and Broadcast message
```bash
$ kafka-console-producer.sh --broker-list kafka:9092
$ > Hello World
```

## CI/CD with Jenkins and GitHub

1. Environment Setting
Launch the Jenkins server with docker
```bash
$ docker run \
  --rm \
  -u root \
  -p 8080:8080 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME":/home \
  jenkinsci/blueocean
```

Follow the instructions from [this link](https://medium.com/@zoejoyuliao/%E7%94%A8-docker-%E5%AE%89%E8%A3%9D-ci-%E5%B7%A5%E5%85%B7-jenkins-347ffe630e40)


2. Mapping the GitHub WebHook to the Jenkin Server
Refer to [this link](https://medium.com/@zoejoyuliao/%E7%94%A8-docker-%E5%AE%89%E8%A3%9D-ci-%E5%B7%A5%E5%85%B7-jenkins-347ffe630e40)



