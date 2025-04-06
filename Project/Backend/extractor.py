import spacy
import re

nlp = spacy.load("en_core_web_sm")

QUANTITY_PATTERN = re.compile(r"(\d+(\.\d+)?)(\s?(kg|hg|g|lb|oz|l|ml|cl|pz|pack))", re.IGNORECASE)

def extract_quantity(text):
    matches = QUANTITY_PATTERN.findall(text)
    extracted_data = [{"value": float(match[0]), "unit": match[3]} for match in matches]
    return extracted_data

if __name__ == "__main__":
    sample_text = "5kg of pasta and 10l of milk"
    print(extract_quantity(sample_text))
