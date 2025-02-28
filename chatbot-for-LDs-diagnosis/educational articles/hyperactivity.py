import requests
from bs4 import BeautifulSoup
import json

# URL of the CDC ADHD diagnosis page
url = "https://www.cdc.gov/adhd/diagnosis/index.html"

# Get the webpage content
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all("div", class_="table dfe-table table-no-header")

# Ensure that there are at least two tables (one for Inattention, one for Hyperactivity-Impulsivity)
if len(tables) >= 2:
    # Extracting Hyperactivity-Impulsivity symptoms from the second table
    hyperactivity_table = tables[1]
    rows = hyperactivity_table.find_all("div", role="row")
    hyperactivity_symptoms = [row.get_text(strip=True) for row in rows]

    # Load existing data from the JSON file
    try:
        with open("adhd_symptoms.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"hyperactivity_impulsivity_symptoms": []}

    # Ensure we don't duplicate hyperactivity-impulsivity symptoms
    if "hyperactivity_impulsivity_symptoms" not in data:
        data["hyperactivity_impulsivity_symptoms"] = []

    # Remove duplicates and append new Hyperactivity-Impulsivity symptoms
    existing_hyperactivity_symptoms = set(data["hyperactivity_impulsivity_symptoms"])
    new_hyperactivity_symptoms = [symptom for symptom in hyperactivity_symptoms if symptom not in existing_hyperactivity_symptoms]
    data["hyperactivity_impulsivity_symptoms"].extend(new_hyperactivity_symptoms)

    # Save the updated data back to the JSON file
    with open("adhd_symptoms.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"{len(new_hyperactivity_symptoms)} new hyperactivity-impulsivity symptoms added.")
else:
    print("Required tables not found on the page.")
