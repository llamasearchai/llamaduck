"""
Tests for the search module.
"""

import unittest
from unittest.mock import MagicMock, patch

from llamaduck.search import search_web


class TestSearch(unittest.TestCase):
    """Test suite for the search module."""

    @patch("llamaduck.search.DDGS")
    def test_search_web_success(self, mock_ddgs):
        """Test successful web search."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = [
            {"title": "Test Result", "body": "Test body", "href": "https://example.com"}
        ]

        # Execute function
        results = search_web("test query", max_results=1)

        # Assertions
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Result")
        mock_instance.text.assert_called_once_with(
            "test query", region="wt-wt", max_results=1
        )

    @patch("llamaduck.search.DDGS")
    def test_search_web_custom_region(self, mock_ddgs):
        """Test web search with custom region."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = [
            {"title": "Test Result", "body": "Test body", "href": "https://example.com"}
        ]

        # Execute function with custom region
        results = search_web("test query", max_results=1, region="us-en")

        # Assertions
        mock_instance.text.assert_called_once_with(
            "test query", region="us-en", max_results=1
        )

    @patch("llamaduck.search.DDGS")
    def test_search_web_empty_results(self, mock_ddgs):
        """Test web search with empty results."""
        # Setup mock
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.return_value = []

        # Execute function
        results = search_web("test query")

        # Assertions
        self.assertEqual(results, [])

    @patch("llamaduck.search.DDGS")
    def test_search_web_exception(self, mock_ddgs):
        """Test web search handling exceptions."""
        # Setup mock to raise exception
        mock_instance = MagicMock()
        mock_ddgs.return_value.__enter__.return_value = mock_instance
        mock_instance.text.side_effect = Exception("API Error")

        # Execute function - should handle exception gracefully
        results = search_web("test query")

        # Assertions
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
