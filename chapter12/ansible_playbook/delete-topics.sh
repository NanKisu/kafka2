#!/bin/bash

KAFKAPATH="/home/ec2-user/kafka_2.12-2.6.0/bin/kafka-topics.sh"
TOPICS=`${KAFKAPATH} --zookeeper kisu-zk01.foo.bar:2181/$1 --list`

for topic in $TOPICS
do
  if [ "${topic}" != "__consumer_offsets" ]; then
    ${KAFKAPATH} --zookeeper kisu-zk01.foo.bar:2181/$1 --delete --topic ${topic}
  fi
done