from bs4 import BeautifulSoup
import re


def read_html_file(filename):
    with open(filename, "r") as f:
        html = f.read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup


def get_html_body_text(soup):
    # kill all script and style elements
    for script in soup(["script", "style", "a"]):
        script.extract()

    for script in soup.find_all("div", {"class": re.compile("foot*")}):
        script.extract()

    # get text
    text = soup.get_text()
    # # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text


def get_html_footer_text(soup):
    texts = []
    for script in soup.find_all("div", {"class": re.compile("foot*")}):
        text = script.get_text()
        # # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # # drop blank lines
        text = "\n".join(chunk for chunk in chunks if chunk)

        texts.append(text)    

    return "\n".join(texts)
