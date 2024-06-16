import requests
from bs4 import BeautifulSoup
from typing import List
from git_command import GitCommand

class GitCommandScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _parse_command_name(self, page: BeautifulSoup) -> str:
        return page.find('div', id='main').text

    def fetch_command(self, command_link: str) -> GitCommand:
        """Fetch command details from a given link."""
        response = requests.get(command_link)
        command_soup = BeautifulSoup(response.text, 'html.parser')

        main_element = command_soup.find('div', id='main')
        filter(lambda div: div.find('h2', id='name'), main_element.find_all)
        
        
        
        all_elements = main_element.find_all('div', class_='sect1')


        command_name = self._parse_command_name(command_soup)
        # description = command_soup.find('p').text
        # usage = command_soup.find('pre', class_='usage').text if command_soup.find('pre', class_='usage') else ""
        # options = [opt.text for opt in command_soup.find_all('code', class_='option')]
        # examples = [ex.text for ex in command_soup.find_all('pre', class_='example')]
        # details = command_soup.find('div', class_='description').text if command_soup.find('div', class_='description') else ""

        return GitCommand(
            command_name=command_name,
            # description=description,
            # usage=usage,
            # options=options,
            # examples=examples,
            # details=details
        )

    # def scrape_git_commands(self) -> List[GitCommand]:
    #     """Scrape git commands from the base URL."""
    #     response = requests.get(self.base_url)
    #     soup = BeautifulSoup(response.text, 'html.parser')

    #     commands = []

    #     for section in soup.find_all('div', class_='command-listing'):
    #         for command in section.find_all('a'):
    #             command_link = f"{self.base_url}{command['href']}"
    #             command_details = self.fetch_command(command_link)
    #             commands.append(command_details)

    #     return commands
