import uuid

from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka import TopicPartition

from api import socketio
from config import BOOTSTRAP_SERVERS
from config import TOPIC_NAME


@socketio.on('connect')
def test_connect():
    socketio.emit('logs', {'data': 'Connection established'})


@socketio.on('kafkaproducer')
def kafkaproducer(message):
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    producer.send(TOPIC_NAME, value=bytes(str(message), encoding='utf-8'),
                  key=bytes(str(uuid.uuid4()), encoding='utf-8'))
    socketio.emit('logs', {'data': 'Added ' + message + ' to topic'})
    socketio.emit('kafkaproducer', {'data': message})
    producer.close()
    kafkaconsumer(message)


@socketio.on('kafkaconsumer')
def kafkaconsumer(message):
    consumer = KafkaConsumer(group_id='group-a',
                             bootstrap_servers=BOOTSTRAP_SERVERS)
    tp = TopicPartition(TOPIC_NAME, 0)
    # register to the topic
    consumer.assign([tp])

    # obtain the last offset value
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    consumer.seek_to_beginning(tp)
    socketio.emit('kafkaconsumer1', {'data': ''})
    for message in consumer:
        socketio.emit('kafkaconsumer', {'data': message.value.decode('utf-8')})
        if message.offset == lastOffset - 1:
            break
    consumer.close()
