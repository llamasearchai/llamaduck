"""
Tests for the CLI module.
"""
import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from llamaduck.cli import cli, search, chat


class TestCLI(unittest.TestCase):
    """Test suite for the CLI module."""

    def setUp(self):
        """Set up test cases."""
        self.runner = CliRunner()

    def test_cli_version(self):
        """Test CLI version command."""
        result = self.runner.invoke(cli, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("version", result.output.lower())

    def test_cli_help(self):
        """Test CLI help command."""
        result = self.runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("usage", result.output.lower())
        self.assertIn("search", result.output.lower())
        self.assertIn("chat", result.output.lower())

    @patch('llamaduck.cli.DDGS')
    def test_search_command(self, mock_ddgs):
        """Test search command."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = [
            {"title": "Test Result", "body": "Test body", "href": "https://example.com"}
        ]
        
        # Run command
        result = self.runner.invoke(search, ["python test"])
        
        # Assertions
        self.assertEqual(result.exit_code, 0)
        self.assertIn("test result", result.output.lower())
        self.assertIn("test body", result.output.lower())
        self.assertIn("example.com", result.output.lower())

    @patch('llamaduck.cli.DDGS')
    def test_search_command_with_options(self, mock_ddgs):
        """Test search command with options."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = [
            {"title": "Test Result", "body": "Test body", "href": "https://example.com"}
        ]
        
        # Run command with options
        result = self.runner.invoke(search, ["python test", "--limit", "3", "--region", "us-en"])
        
        # Assertions
        self.assertEqual(result.exit_code, 0)
        mock_instance.text.assert_called_once_with("python test", region="us-en", max_results=3)

    @patch('llamaduck.cli.DDGS')
    def test_chat_command(self, mock_ddgs):
        """Test chat command."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = [
            {"body": "Python is a programming language"}
        ]
        
        # Run command
        result = self.runner.invoke(chat, ["What is Python?"])
        
        # Assertions
        self.assertEqual(result.exit_code, 0)
        self.assertIn("python is a programming language", result.output.lower())

    @patch('llamaduck.cli.DDGS')
    def test_search_command_error(self, mock_ddgs):
        """Test search command with error."""
        # Setup mock to raise exception
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.side_effect = Exception("API Error")
        
        # Run command
        result = self.runner.invoke(search, ["python test"])
        
        # Assertions
        self.assertEqual(result.exit_code, 0)  # Should handle error gracefully
        self.assertIn("error", result.output.lower())


if __name__ == "__main__":
    unittest.main() 