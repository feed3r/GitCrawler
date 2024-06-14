# main.py

from .scraper import scrape_git_commands
from .kafka_producer import send_to_kafka
from .config import load_config

def main() -> None:
    config = load_config('GitCrawler/config.yaml')
    base_url = "https://git-scm.com/docs/git#_git_commands"
    broker = config['kafka']['broker']
    topic = config['kafka']['topic']

    commands = scrape_git_commands(base_url)
    send_to_kafka(commands, broker, topic)

if __name__ == "__main__":
    main()
