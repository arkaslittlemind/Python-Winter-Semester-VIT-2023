import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_links(url):
    # Check if the URL is valid and accessible
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract links
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            cleaned_href = href.strip()
            links.append(cleaned_href)
    
    return links

# Get user input
url = input("Enter the URL of the webpage to extract links from: ")

# Check if the URL is valid and accessible
parsed_url = urlparse(url)
if not all([parsed_url.scheme, parsed_url.netloc]):
    print("Invalid URL format.")
else:
    # Extract links from the webpage
    extracted_links = extract_links(url)
    
    # Print the extracted links
    print("Links:")
    for link in extracted_links:
        print(link)
