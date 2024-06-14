from confluent_kafka import Producer
from typing import List
import json
from .git_command import GitCommand

def send_to_kafka(data: List[GitCommand], broker: str, topic: str) -> None:
    """Send the data to a Kafka broker."""
    producer = Producer({'bootstrap.servers': broker})

    def delivery_report(err, msg):
        """Callback for Kafka delivery reports."""
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    for record in data:
        producer.produce(topic, key=record.command_name, value=json.dumps(record.__dict__), callback=delivery_report)
        producer.poll(0)

    producer.flush()
