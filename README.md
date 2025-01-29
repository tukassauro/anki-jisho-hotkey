# anki-jisho-hotkey

A Python script that allows you to quickly add Japanese vocabulary to Anki using a hotkey. When you copy a Japanese word and press Ctrl+Shift+A, the script automatically fetches the word's reading and meaning from Jisho.org and creates a new Anki card.
Features

Quick card creation with a simple hotkey (Ctrl+Shift+A)
Automatic fetching of readings and meanings from Jisho.org
Support for custom note types and field names
Error handling for common issues
Automatic tagging of added cards

Prerequisites
Before using this script, make sure you have:

Anki installed
AnkiConnect add-on installed in Anki
Python 3.6 or higher
The following Python packages:

requests
pyperclip
keyboard



Installation

Clone this repository:
bashCopygit clone https://github.com/YourUsername/anki-jisho-hotkey.git
cd anki-jisho-hotkey

Install required Python packages:
bashCopypip install requests pyperclip keyboard


Configuration
Before running the script, make sure:

Your Anki is running
You have a deck named "Japanese" (or modify the deck_name parameter in the script)
You have a note type that matches your configuration (default is "Basic" with "Front" and "Back" fields)

To modify the deck name or note type configuration, edit these lines in the script:
pythonCopy"deckName": "Japanese",  # Change to your deck name
"modelName": "Basic",    # Change to your note type name
"fields": {
    "Front": f"{word} [{reading}]",     # Change to your front field name
    "Back": f"<div>Meaning: {meaning}</div>..."  # Change to your back field name
}
Note Type Configuration
The script uses Anki's default note type and field names:

Note Type: "Basic"
Front Field: "Front"
Back Field: "Back"

If you're using:

Different field names (e.g., "Question"/"Answer" or localized names)
A different note type name (e.g., "Basic-reversed" or localized names)
Custom fields

Simply modify the corresponding values in the script to match your Anki setup.
Usage

Run the script:
bashCopypython add_to_anki.py

Copy any Japanese word you want to add to Anki
Press Ctrl+Shift+A
The script will automatically:

Fetch the word's data from Jisho.org
Create a new card in your specified deck
Add the word, reading, and meaning to the card



Example

Copy the word "接点"
Press Ctrl+Shift+A
A new card will be created with:

Front: 接点 [せってん]
Back: Meaning: point of tangency, point of contact



Limitations

Currently works best with single words rather than sentences
Requires an active internet connection to fetch data from Jisho.org
Must have Anki running with AnkiConnect installed

Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or bug fixes.
Acknowledgments

Jisho.org for their API
AnkiConnect for enabling Anki automation
Created with assistance from Claude AI

License
This project is licensed under the MIT License - see the LICENSE file for details.
