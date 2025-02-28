import re
from bs4 import BeautifulSoup
import requests
import json

url1 = "https://www.understood.org/en/articles/what-is-autism"
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.text, "html.parser")

data = {}

target_phrases = [
    "Autism is a neurodevelopmental disorder that",
    "Autism often co-occurs with other conditions, like ADHD "
]

autism_paragraphs = []

for para in soup1.find_all("p"):
    text = para.get_text(" ", strip=True)

    # Check if the paragraph starts with any target phrase
    if any(text.startswith(phrase) for phrase in target_phrases):
        cleaned_text = text

        # Remove in-text citations (e.g., "(Barkley, 1997; Cantwell, 1997)")
        cleaned_text = re.sub(r"\(.*?\)", "", cleaned_text)

        # Remove "They share common challenges with social skills and communication" phrase
        cleaned_text = re.sub(r"They share common challenges with social skills and communication, including:?\s*", "", cleaned_text, flags=re.I)

        # Remove extra spaces
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)

        # Fix misplaced punctuation
        cleaned_text = re.sub(r"\.\s*,", ".", cleaned_text)

        # Trim leading/trailing spaces
        cleaned_text = cleaned_text.strip()

        # Append to the autism_paragraphs list
        autism_paragraphs.append(cleaned_text)

# Signs associated with autism
signs = [
    "Trouble reading nonverbal cues or picking up on social cues",
    "Difficulty participating in conversation",
    "Not always being able to modulate their tone of voice",
    "Taking language literally and having trouble understanding sarcasm",
    "Arm flapping or rocking",
    "Repeating certain sounds or phrases"
]

autism_signs = []

for para in soup1.find_all("p"):
    text = para.get_text(" ", strip=True)

    # Check if any of the signs appear in the paragraph
    for sign in signs:
        if sign.lower() in text.lower():  # Case-insensitive search
            autism_signs.append(text)

# If we have paragraphs to save
if autism_paragraphs:
    data["autism_info"] = autism_paragraphs

if autism_signs:
    data["autism_signs"] = autism_signs
    
    # Write the data to a JSON file
    with open("autism_symptoms.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print("✅ Data successfully saved in autism_symptoms.json!")
else:
    print("❌ No relevant paragraphs found.")
