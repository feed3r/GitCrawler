from .scraper import scrape_git_commands
from .kafka_producer import send_to_kafka
from .config import load_config

def main() -> None:
    config = load_config('GitCrawler/config.yaml')
    base_url = "https://git-scm.com/docs/git#_git_commands"
    broker = config['kafka']['broker']
    topic = config['kafka']['topic']

    print("Starting to scrape Git commands...")
    commands = scrape_git_commands(base_url)
    print(f"Scraping completed. Found {len(commands)} commands.")

    for command in commands:
        print("------")
        print(f"Command Name: {command.command_name}")
        print(f"Description: {command.description}")
        print(f"Usage: {command.usage}")
        print(f"Options: {command.options}")
        print(f"Examples: {command.examples}")
        print(f"Details: {command.details}")
        print("------")

    print("Sending data to Kafka broker...")
    send_to_kafka(commands, broker, topic)
    print("Data successfully sent.")

if __name__ == "__main__":
    main()
