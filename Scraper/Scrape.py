import json
import requests
from bs4 import BeautifulSoup

# Load the initial sign mappings from the JSON file
with open('SignMappings/words.json') as file:
    sign_mappings = json.load(file)
# Add alphabets.json and digits.json to the sign mappings
with open('SignMappings/alphabets.json') as file:
    sign_mappings.update(json.load(file))
with open('SignMappings/digits.json') as file:
    sign_mappings.update(json.load(file))
print("Loaded initial sign mappings.")

# Base URL of the website
base_url = "https://www.signbsl.com"
print("Fetching video links for the signs...")
print("First 5 signs:")
print(list(sign_mappings.items())[:5])
# New dictionary to store the updated mappings
updated_sign_mappings = {}

# Iterate over the initial mappings
for word, path in sign_mappings.items():
    # Construct the full URL to fetch
    url = f"{base_url}{path}"
    print(f"Fetching video link for {word} from {url}...")
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first video link in the <head> section
        for link in soup.head.find_all('meta', attrs={'content': True}):
            content = link['content']
            if content.startswith('https://media.signbsl.com/videos/bsl/'):
                updated_sign_mappings[word] = content
                break
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Write the updated mappings to a new JSON file
with open('SignMappings/updated_mappings.json', 'w') as file:
    json.dump(updated_sign_mappings, file, indent=4)

print("Updated mappings have been written to SignMappings/updated_mappings.json.")
