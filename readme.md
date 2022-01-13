# Text To Speech

Generates mp3 files (and a text file showing what will be on the mp3 file) from HTML files using gTTS (Google Text-to-Speech) (Currently for testing purposes), the HTML file is currently broken down to into 2 parts:

1. Body
2. Footer

This currently only works with one html file at a time (html splitting is currently WIP, as we don't know the extent of what files we will receive).

### Process 

1. HTML File is passed into text_to_speech
2. File is converted into text (body, footer)
3. Text is converted into mp3 files

### Note

```
gTTs is not affiliated with Google or Google Cloud. Breaking upstream changes can occur without notice. This project is leveraging the undocumented Google Translate speech functionality and is different from Google Cloud Text-to-Speech.
```

- Initial idea was to perform the text to speech on the whole html page but that could take a rather long time to product the mp3 - currently it takes a while for it to generate a 5mb mp3 file
- This has been adjusted to split the text into smaller sections - everytime it reaches a new line using '\n'

- The Speech side of things is only useful for testing purposes - frontend will need to handle the audio output

## Setup

```bash
pipenv shell
pip install
```

## Usage

```python
python text_to_speech.py

```

## Improvements and Considerations

- Voice Change - male/female/different accents
- Language Change and support?

- Perform on client side or server side?
- How would the eReader use these files?
- How will they implement each of these mp3 files in the correct location?
- Can they implement text highlighting alongside with the speech?
- What would be the best time to perform text to speech conversions? - very costly if you do it for every book
    - we could potentially do it for when a book gets open?
    - when a user highlight's certain passages?