import os
import playsound
from gtts import gTTS
import logging
from get_text import read_html_file, get_html_body_text, get_html_footer_text

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def execute(filename):
    logging.info("Starting process")
    print("here!")
    name = filename.split('.')[0]
    html = read_html_file(filename)
    f_text = get_html_footer_text(html)
    filename = f"tmp/{name}_footer.txt"
    save_text_file(filename, f_text)

    b_text = get_html_body_text(html)
    filename = f"tmp/{name}.txt"
    save_text_file(filename, b_text)
    logging.info("saving txt")

    texts = b_text.split("\n")
    for index, text in enumerate(texts):
        filename = f"tmp/{name}_{index}.mp3"
        save_audio_file(filename, text)
        
    # os.remove(filename)


def save_text_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)


def save_audio_file(filename, text, language="en"):
    tts = gTTS(text=text, lang=language)
    logging.info(f"creating {filename}")
    tts.save(filename)
    logging.info(f"{filename} - saved")


def speak(filename):
    playsound.playsound(filename)


filename = "2.html"
execute(filename)

# filename = "2_6.mp3"
# speak(filename)
