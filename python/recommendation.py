import sys
import openai
import spacy
import PyPDF2
import os

# Set up OpenAI API credentials
openai.api_key = os.environ['API_KEY']

pdf_path = os.path.abspath('python/pdf/pdf1.pdf')

# Load SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Read the PDF file
pdf_file = open(pdf_path, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_text = ""
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Get the prompt from command line arguments
prompt = sys.argv[1]

# Search for matching answers in the PDF
pdf_answer = ""
if prompt in pdf_text:
    pdf_answer = "____"

# Generate an answer from OpenAI if no answer was found in the PDF
if not pdf_answer:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    openai_answer = response.choices[0].text

# Combine the PDF answer and OpenAI answer, if applicable
if pdf_answer and openai_answer:
    recommendation = f"PDF: {pdf_answer}\nOpenAI: {openai_answer}"
elif pdf_answer:
    recommendation = pdf_answer
else:
    recommendation = openai_answer

# Print the recommendation
print(recommendation)
