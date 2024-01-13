import nltk
from nltk.tokenize import word_tokenize
import PyPDF2
from docx import Document

# Ensure you have the necessary NLTK data
nltk.download('punkt')

# Function to load words from a DOCX file
def load_words_from_docx(docx_path):
    doc = Document(docx_path)
    words = []
    for para in doc.paragraphs:
        words.extend(para.text.split())
    return list(set(word.lower() for word in words))

# Updated function to process text and find words
def process_text(text, word_list, page_number):
    found_words = {}
    tokens = word_tokenize(text)
    for token in tokens:
        for word in word_list:
            if word in token.lower():
                found_words[word] = found_words.get(word, []) + [page_number]
    return found_words

# Load words from DOCX file
docx_path = '/path_to_your_docx_file.docx'
words_to_find = load_words_from_docx(docx_path)

# Reading the PDF and processing text
def process_pdf(pdf_path, words_to_find):
    found_words_in_pdf = {}
    occurrences_count = {}

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            found_words = process_text(text, words_to_find, page_number + 1)

            # Combine results and count occurrences
            for word, pages in found_words.items():
                if word in found_words_in_pdf:
                    found_words_in_pdf[word].add(pages[0])
                    occurrences_count[word] += len(pages)
                else:
                    found_words_in_pdf[word] = {pages[0]}
                    occurrences_count[word] = len(pages)

    return found_words_in_pdf, occurrences_count

# Example PDF path - replace this with the actual path of your PDF
pdf_path = '/path_to_your_pdf_file.pdf'

# Process the PDF
found_words_in_pdf, occurrences_count = process_pdf(pdf_path, words_to_find)

# Output the final list with sorted pages and count of occurrences
for word, pages in found_words_in_pdf.items():
    sorted_pages = sorted(pages)
    print(f"'{word}' found on pages: {sorted_pages} (Total occurrences: {occurrences_count[word]})")
