import requests
from bs4 import BeautifulSoup
import os
import re

websites = [
    "https://en.wikipedia.org/wiki/Dyslexia", "https://www.mayoclinic.org/diseases-conditions/adhd/symptoms-causes/syc-20350889", "https://www.nimh.nih.gov/health/publications/attention-deficit-hyperactivity-disorder-what-you-need-to-know", "https://www.mayoclinic.org/diseases-conditions/autism-spectrum-disorder/symptoms-causes/syc-20352928", "https://www.mayoclinic.org/diseases-conditions/autism-spectrum-disorder/diagnosis-treatment/drc-20352934", "https://www.nationwidechildrens.org/conditions/autism-spectrum-disorder", "https://www.nationwidechildrens.org/conditions/autism-spectrum-disorder", "https://my.clevelandclinic.org/health/diseases/23949-dyscalculia", "https://leafcare.co.uk/learning-difficulty/dyscalculia/", "https://psychcentral.com/health/dyscalculia-symptoms",
    "https://www.houstonent.com/blog/what-is-auditory-processing-disorder-definition-symptoms-and-treatments"
    # Add more URLs if needed
]

# Create an output directory to store files
output_dir = "scraped_texts"
os.makedirs(output_dir, exist_ok=True)

for url in websites:
    try:
        # Make a GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parse the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract all text
        text = soup.get_text(separator="\n", strip=True)

        # Remove square brackets and numbers inside them
        cleaned_text = re.sub(r"\[\n\d+\n\]", "", text)
        cleaned_text = re.sub(r"\s", "", cleaned_text)
        cleaned_text = re.sub(r"\(", "", cleaned_text)


        # Generate a filename from the URL
        filename = url.split("//")[-1].replace("/", "_") + ".txt"
        filepath = os.path.join(output_dir, filename)

        # Write text to a file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"Content from {url}:\n")
            file.write(cleaned_text + "\n")

        print(f"Successfully saved cleaned content to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

print("All websites processed.")
