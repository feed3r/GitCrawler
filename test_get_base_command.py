import unittest

from command_scraper import GitCommandScraper

class TestGetBaseCommandDocumentation(unittest.TestCase):
    
    def test_base(self):
        # Test case 1: Test with a valid git command
        link = "https://git-scm.com/docs/git"
        scraper = GitCommandScraper(link)
        command = scraper.fetch_command(link)
        assert(command is not None)
        assert(command.Name is not None)
        
        # Test case 2: Test with an invalid git command
        command = "invalid_command"
        expected_output = None
        self.assertEqual(get_base_command_documentation(command), expected_output)

        # Test case 3: Test with an empty command
        command = ""
        expected_output = None
        self.assertEqual(get_base_command_documentation(command), expected_output)

if __name__ == '__main__':
    unittest.main()