from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(1, 101):
    message = f"Message {i}"
    producer.send('test-topic', value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(0.1)  # Optional: slight delay for readability

producer.flush()
producer.close()

