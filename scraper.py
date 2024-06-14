import requests
from bs4 import BeautifulSoup
from typing import List
from .git_command import GitCommand

def fetch_command_details(command_link: str) -> GitCommand:
    """Fetch command details from a given link."""
    command_response = requests.get(command_link)
    command_soup = BeautifulSoup(command_response.text, 'html.parser')

    command_name = command_link.split('/')[-1]
    description = command_soup.find('p').text
    usage = command_soup.find('pre', class_='usage').text if command_soup.find('pre', class_='usage') else ""
    options = [opt.text for opt in command_soup.find_all('code', class_='option')]
    examples = [ex.text for ex in command_soup.find_all('pre', class_='example')]
    details = command_soup.find('div', class_='description').text if command_soup.find('div', class_='description') else ""

    return GitCommand(
        command_name=command_name,
        description=description,
        usage=usage,
        options=options,
        examples=examples,
        details=details
    )

def scrape_git_commands(base_url: str) -> List[GitCommand]:
    """Scrape git commands from the base URL."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    commands = []

    for section in soup.find_all('div', class_='command-listing'):
        for command in section.find_all('a'):
            command_link = f"{base_url}{command['href']}"
            command_details = fetch_command_details(command_link)
            commands.append(command_details)

    return commands
