import PyPDF2
import collections
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + ' '
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation
    words = text.split()
    return words

def word_frequency(words):
    return collections.Counter(words)

def main(file_path):
    text = read_pdf(file_path)
    words = clean_text(text)
    freq_dict = word_frequency(words)
    return freq_dict

if __name__ == '__main__':
    freq_dict = main('./Nayeel_s_SWE_Resume_2_14_24.pdf')
    print(freq_dict)
