import os
from flask import Flask, render_template, request, redirect, url_for
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from heapq import nlargest
from gtts import gTTS
import pyttsx3

# Initialize Flask app
app = Flask(__name__)

# Set the Pytesseract path (change for mac os )
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

# Text extraction function
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            extracted_text = ' '.join([page.extract_text() for page in pdf.pages])
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(img)
    else:
        extracted_text = "Unsupported file format."
    return extracted_text

# Text summarization function
# def text_summarization(text, num_sentences=3):
    # sentences = sent_tokenize(text)
    # words = word_tokenize(text.lower())
    # stop_words = set(stopwords.words('english'))
    # words = [word for word in words if word not in stop_words]
    # word_freq = {}
    # for word in words:
    #     word_freq[word] = word_freq.get(word, 0) + 1
    # sentence_scores = {}
    # for sentence in sentences:
    #     for word in word_tokenize(sentence.lower()):
    #         if word in word_freq:
    #             sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]
    # summarized_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    # summary = ' '.join(summarized_sentences)
    # return summary

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def text_summarization(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summarized = summarizer(parser.document, sentences_count)
    summary = ' '.join([str(sentence) for sentence in summarized])
    return summary


# Text-to-speech function
def text_to_speech(text, language='en', output_file='output.mp3'):
    tts_obj = gTTS(text=text, lang=language, slow=False)
    tts_obj.save(output_file)
    return output_file

# Main route
@app.route("/")
def main():
    return render_template("index.html")

# process route
@app.route("/process_file", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    extracted_text = extract_text(file_path)
    # print("Extracted text:", extracted_text)
    summary = text_summarization(extracted_text)
    # output_file = text_to_speech(summary)
    return redirect(url_for("output", extracted_text=extracted_text, summary=summary))

# output route
@app.route("/output")
def output():
    extracted_text = request.args.get("extracted_text", "")
    summary = request.args.get("summary","")
    # output_file = request.args.get("output_file", "")
    return render_template("output.html", extracted_text=extracted_text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)