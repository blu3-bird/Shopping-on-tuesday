"""
Meesho scraping service for dropshipping product import.

This module provides functions to scrape product data from Meesho's website
using requests and BeautifulSoup4. It is designed to be lightweight and
respectful of rate limits.

The scraping layer is isolated behind this service interface so it can be
swapped in for the official Meesho API later without touching the rest of the app.
"""

import time
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


# Default headers to look like a real browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Delay between requests in seconds (be respectful)
REQUEST_DELAY = 2.0

# Meesho domain
MEESHO_DOMAIN = "meesho.com"


def _get_soup(url):
    """Fetch a URL and return a BeautifulSoup object."""
    time.sleep(REQUEST_DELAY)
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def _extract_price(text):
    """Extract a float price from a string like '₹299' or '299'."""
    if not text:
        return None
    cleaned = re.sub(r"[^\d\.]", "", text)
    try:
        return float(cleaned)
    except ValueError:
        return None


def _extract_images(soup):
    """Extract product image URLs from the page."""
    images = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if src:
            images.append(src)
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for img in images:
        if img not in seen:
            seen.add(img)
            unique.append(img)
    return unique[:10]  # Limit to 10 images


def scrape_product(url):
    """
    Scrape a single Meesho product page.

    Args:
        url (str): Meesho product URL.

    Returns:
        dict: Product data with keys:
            - title (str)
            - price (float or None)
            - description (str or None)
            - category (str or None)
            - image_urls (list of str)
            - source_url (str)
            - stock (int) - always 1 (unknown from scraping)
    """
    soup = _get_soup(url)

    # Title - try multiple selectors
    title = None
    for selector in ["h1", "[data-testid='product-title']", ".product-title"]:
        el = soup.select_one(selector)
        if el:
            title = el.get_text(strip=True)
            break

    # Price
    price = None
    for selector in ["[data-testid='product-price']", ".product-price", ".price"]:
        el = soup.select_one(selector)
        if el:
            price = _extract_price(el.get_text())
            if price:
                break

    # Description
    description = None
    for selector in ["[data-testid='product-description']", ".product-description", ".description"]:
        el = soup.select_one(selector)
        if el:
            description = el.get_text(strip=True)
            break

    # Category
    category = None
    breadcrumb = soup.select_one("[data-testid='breadcrumb']")
    if breadcrumb:
        category = breadcrumb.get_text(strip=True)
    else:
        # Try to find category from URL path
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p]
        if parts:
            category = parts[-1].replace("-", " ").title()

    # Images
    image_urls = _extract_images(soup)

    return {
        "title": title or "Untitled Product",
        "price": price,
        "description": description,
        "category": category,
        "image_urls": image_urls,
        "source_url": url,
        "stock": 1,
    }


def scrape_category(category_url, limit=10):
    """
    Scrape multiple products from a Meesho category page.

    Args:
        category_url (str): Meesho category URL.
        limit (int): Maximum number of products to scrape.

    Returns:
        list of dict: Product data dicts (same format as scrape_product).
    """
    soup = _get_soup(category_url)

    # Find product links - try multiple selectors
    product_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/product/" in href or "/p/" in href:
            full_url = urljoin("https://www.meesho.com", href)
            if full_url not in product_links:
                product_links.append(full_url)

    products = []
    for link in product_links[:limit]:
        try:
            product = scrape_product(link)
            products.append(product)
        except Exception:
            # Skip products that fail to scrape
            continue

    return products


def is_meesho_url(url):
    """Check if a URL belongs to Meesho."""
    return MEESHO_DOMAIN in urlparse(url).netloc
