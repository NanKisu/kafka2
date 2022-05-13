from confluent_kafka import Consumer

broker = 'kisu-kafka01.foo.bar, kisu-kafka02.foo.bar, kisu-kafka03.foo.bar'
group = 'kisu-consumer01'
topic = 'kisu-test06'

c = Consumer({
    'bootstrap.servers': broker,
    'group.id': group,
    'auto.offset.reset': 'earliest'
})
c.subscribe([topic])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print('Topic: {}, '
          'Partition: {}, '
          'Offset: {}, '
          'Received message: {}'.format(msg.topic(),
                                        msg.partition(),
                                        msg.offset(),
                                        msg.value().decode('utf-8')))
c.close()
