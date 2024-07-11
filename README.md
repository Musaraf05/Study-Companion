# Study Companion

Study Companion is a Flask-based web application designed to help students extract text from documents, summarize the text, convert it to speech, and calculate their GPA and CGPA. The application supports PDF and image files for text extraction.

## Features

- **Text Extraction**: Extracts text from PDF and image files using OCR (Optical Character Recognition).
- **Text Summarization**: Summarizes extracted text to provide concise information.
- **Text-to-Speech**: Converts summarized text to speech and generates an audio file.

## Installation

To run this project locally, follow these steps:

1. **Install the required packages**:

    ```sh
    pip install  Flask PyPDF2 Pillow pytesseract nltk heapq gtts pyttsx3 sumy

    ```

2. **Set up Tesseract**:

    - **Mac OS**: Install Tesseract using Homebrew:

        ```sh
        brew install tesseract
        ```

    - **Windows**: Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).

3. **Run the application**:

    ```sh
    python app.py
    ```

6. **Open your browser** and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

### Text Extraction and Summarization

1. **Upload a file**: On the main page, upload a PDF or an image file.
2. **Process the file**: The app will extract the text and generate a summary.
3. **View the output**: The extracted text and summary will be displayed on the output page.



## Requirements

- Flask
- PyPDF2
- Pillow
- pytesseract
- nltk
- heapq
- gtts
- pyttsx3
- sumy


## License

This project is licensed under the MIT License.

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [NLTK](https://www.nltk.org/)
- [Sumy](https://github.com/miso-belica/sumy)
- [Flask](https://flask.palletsprojects.com/)


## Contact

- linkedin: [Your LinkedIn Profile](www.linkedin.com/in/mohamed-musaraf-180877244)
