# anki-jisho-hotkey

A Python script that allows you to quickly add Japanese vocabulary to Anki using a hotkey. When you copy a Japanese word and press Ctrl+Shift+A, the script automatically fetches the word's reading and meaning from Jisho.org and creates a new Anki card.

## Features

- Quick card creation with a simple hotkey (Ctrl+Shift+A)
- Automatic fetching of readings and meanings from Jisho.org
- Support for custom note types and field names
- Error handling for common issues
- Automatic tagging of added cards

## Prerequisites

Before using this script, make sure you have:

1. Anki installed
2. AnkiConnect add-on installed in Anki
3. Python 3.6 or higher
4. The following Python packages:
   - `requests`
   - `pyperclip`
   - `keyboard`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/YourUsername/anki-jisho-hotkey.git
    cd anki-jisho-hotkey
    ```

2. Install required Python packages:
    ```bash
    pip install requests pyperclip keyboard
    ```

## Configuration

Before running the script, make sure:

1. Your Anki is running.
2. You have a deck named "Japanese" (or modify the `deck_name` parameter in the script).
3. You have a note type that matches your configuration (default is "Basic" with "Front" and "Back" fields).

To modify the deck name or note type configuration, edit these lines in the script:
```python
"deckName": "Japanese",  # Change to your deck name
"modelName": "Basic",    # Change to your note type name
"fields": {
    "Front": f"{word} [{reading}]",  # Change to your front field name
    "Back": f"<div>Meaning: {meaning}</div>"  # Change to your back field name
}

```


 ## Note Type Configuration:

The script uses Anki's default note type and field names:

Note Type: "Basic"

Front Field: "Front"

Back Field: "Back"

If you're using:

- Different field names (e.g., "Question"/"Answer" or localized names)
- A different note type name (e.g., "Basic-reversed" or localized names)
- Custom fields

Simply modify the corresponding values in the script to match your Anki setup.

## Usage:

1.Run the script:
```bash
python add_to_anki.py

```
2. Copy any Japanese word you want to add to Anki.
3. Press Ctrl+Shift+A.
4. The script will automatically:
   - `Fetch the word's data from Jisho.org`
   - `Create a new card in your specified deck`
   - `Add the word, reading, and meaning to the card`

## Example:

1. Copy the word "接点".
2. Press Ctrl+Shift+A.
3. A new card will be created with:
   - `Front: 接点 [せってん]`
   - `Back: Meaning: point of tangency, point of contact`

## Limitations:

- `Currently works best with single words rather than sentences.`
- `Requires an active internet connection to fetch data from Jisho.org.`
- `Must have Anki running with AnkiConnect installed.`

## Contributing:

Feel free to open issues or submit pull requests if you have suggestions for improvements or bug fixes.

## Acknowledgments

- `Jisho.org for the API`
- `AnkiConnect for enabling Anki automation`
- `Created with assistance from AI`

## License

This project is licensed under the MIT License - see the LICENSE file for details.







