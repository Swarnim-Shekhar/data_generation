from kafka import SimpleProducer, KafkaClient

# To send messages synchronously
kafka = KafkaClient('3.168.100.21:9092')
producer = SimpleProducer(kafka)

# Note that the application is responsible for encoding messages to type bytes
producer.send_messages('cctrans', 'whatup son?')

