import requests
import pyperclip
import keyboard
import time
import json

def get_japanese_word_data(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or not data["data"]:
        return None

    entry = data["data"][0]
    
    # Get the reading and word
    japanese_data = entry["japanese"][0]
    word = japanese_data.get("word", word)  # Use input word if no word field
    reading = japanese_data.get("reading", "")

    # Get the first definition
    meaning = ", ".join(entry["senses"][0]["english_definitions"]) if entry["senses"] else ""

    # Example sentence placeholder
    example_sentence = "No example sentence available"

    return word, reading, meaning, example_sentence

def check_anki_running():
    try:
        response = requests.post("http://localhost:8765", json={
            "action": "version",
            "version": 6
        })
        return True
    except requests.exceptions.ConnectionError:
        return False

def add_to_anki(word, reading, meaning, example_sentence, deck_name="Japanese"):
    if not check_anki_running():
        print("Error: Cannot connect to Anki. Please make sure Anki is running and AnkiConnect is installed.")
        return

    # Check if deck exists
    try:
        deck_response = requests.post("http://localhost:8765", json={
            "action": "deckNames",
            "version": 6
        })
        deck_data = deck_response.json()
        if not deck_data.get("result"):
            print("Error: Could not get deck list from Anki")
            return
        if deck_name not in deck_data["result"]:
            print(f"Error: Deck '{deck_name}' not found!")
            return
    except Exception as e:
        print(f"Error checking deck: {str(e)}")
        return

    # Create the note
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "基本",
                "fields": {
                    "表": f"{word} [{reading}]",
                    "裏": f"<div>Meaning: {meaning}</div><div>Example: {example_sentence}</div>"
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": ["auto-added"]
            }
        }
    }

    try:
        # First, check if the note type exists
        model_names_response = requests.post("http://localhost:8765", json={
            "action": "modelNames",
            "version": 6
        })
        model_data = model_names_response.json()
        if "基本" not in model_data.get("result", []):
            print("Error: Note type '基本' not found in Anki!")
            return

        # Then try to add the note
        response = requests.post("http://localhost:8765", json=payload)
        result = response.json()
        
        if result.get("error"):
            print(f"Error adding card: {result['error']}")
            return
        
        if result.get("result") is None:
            print("Error: Failed to add card. Please check your note type fields.")
            return
            
        print(f"Successfully added card for: {word}")
            
    except Exception as e:
        print(f"Error communicating with Anki: {str(e)}")

def main():
    print("Starting Japanese word addition script...")
    print("Make sure AnkiConnect is installed and Anki is running!")
    print("Press Ctrl + Shift + A to add the copied Japanese word to Anki.")
    
    while True:
        try:
            keyboard.wait("ctrl+shift+a")
            time.sleep(0.1)  # Small delay to ensure text is copied
            
            word = pyperclip.paste().strip()
            if not word:
                print("No text in clipboard!")
                continue
                
            print(f"Processing word: {word}")
            
            data = get_japanese_word_data(word)
            if data:
                word, reading, meaning, example_sentence = data
                print(f"Found: {word} ({reading}) - {meaning}")
                add_to_anki(word, reading, meaning, example_sentence)
            else:
                print(f"Could not find data for word: {word}")
                
        except Exception as e:
            print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
