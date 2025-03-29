"""
DuckDuckGo search implementation for LlamaDuck Pro.

This module provides functions to search the web using DuckDuckGo's search API.
It handles various types of searches, error conditions, and provides proper typing.
"""
from typing import List, Dict, Any, Optional, Union, TypedDict
import logging
from duckduckgo_search import DDGS

# Configure logging
logger = logging.getLogger(__name__)


class SearchResult(TypedDict, total=False):
    """Type definition for a search result."""
    
    title: str
    body: str
    href: str


class ImageResult(TypedDict, total=False):
    """Type definition for an image search result."""
    
    title: str
    image: str
    thumbnail: str
    url: str
    height: int
    width: int
    source: str


def search_web(
    query: str, 
    max_results: int = 5, 
    region: str = "wt-wt",
    safe_search: str = "moderate"
) -> List[SearchResult]:
    """
    Search the web using DuckDuckGo API.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return (default: 5)
        region: Region for search results (default: "wt-wt")
        safe_search: Safe search setting: "off", "moderate", or "strict" (default: "moderate")
        
    Returns:
        List of search results, each containing title, body, and href
        
    Raises:
        No exceptions are raised; errors are logged and an empty list is returned
    """
    if not query:
        logger.warning("Empty search query provided")
        return []
        
    try:
        logger.debug(f"Searching for: {query} (region: {region}, max_results: {max_results})")
        with DDGS() as ddgs:
            results = list(ddgs.text(
                query, 
                region=region, 
                max_results=max_results,
                safesearch=safe_search
            ))
        
        logger.info(f"Found {len(results)} results for query: {query}")
        return results
    except Exception as e:
        logger.error(f"Error during search: {e}", exc_info=True)
        return []


def image_search(
    query: str, 
    max_results: int = 5,
    safe_search: str = "moderate",
    size: Optional[str] = None
) -> List[ImageResult]:
    """
    Search for images using DuckDuckGo API.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return (default: 5)
        safe_search: Safe search setting: "off", "moderate", or "strict" (default: "moderate")
        size: Image size filter: "small", "medium", "large" (default: None)
        
    Returns:
        List of image results containing URLs and metadata
        
    Raises:
        No exceptions are raised; errors are logged and an empty list is returned
    """
    if not query:
        logger.warning("Empty image search query provided")
        return []
        
    try:
        logger.debug(f"Searching for images: {query} (max_results: {max_results})")
        with DDGS() as ddgs:
            image_params = {
                "safesearch": safe_search,
                "max_results": max_results
            }
            if size:
                image_params["size"] = size
                
            images = list(ddgs.images(query, **image_params))
            
        logger.info(f"Found {len(images)} image results for query: {query}")
        return images
    except Exception as e:
        logger.error(f"Error during image search: {e}", exc_info=True)
        return []
