from .scraper import scrape_git_commands
from .kafka_producer import send_to_kafka

def main() -> None:
    base_url = "https://git-scm.com/docs/git#_git_commands"
    broker = 'localhost:9092'  # Kafka broker URL
    topic = 'git_commands'     # Kafka topic Name

    commands = scrape_git_commands(base_url)
    send_to_kafka(commands, broker, topic)

if __name__ == "__main__":
    main()
