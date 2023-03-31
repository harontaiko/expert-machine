import sys
import openai
import spacy
import PyPDF2
import os

# Set up OpenAI api
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

# Get the prompt from nodejs
prompt = sys.argv[1]

# Check if the prompt matches any of the rules
if "milk" in prompt.lower():
    if "how to milk cows" in prompt.lower():
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        recommendation = response.choices[0].text
    else:
        recommendation = "Please provide more details about your milk-related inquiry."

elif "cows" in prompt.lower():
    if "how to raise cows" in prompt.lower():
        recommendation = "Raising cows involves providing them with adequate feed, water, and shelter. It's also important to monitor their health and provide veterinary care when necessary. You can find more information about raising cows in books and online resources."
    elif "how to milk cows" in prompt.lower():
        recommendation = "To milk cows, first, clean their udders and teats with a mild disinfectant. Then, position yourself behind the cow and place a bucket underneath the udders. Grab the teats with your thumb and forefinger, and squeeze downwards to release the milk. Repeat the process with all four teats until the udders are empty."
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        recommendation = response.choices[0].text

elif "farming" in prompt.lower():
    if "how to start a farm" in prompt.lower():
        recommendation = "Starting a farm involves finding suitable land, choosing the right crops and animals to raise, and securing financing. It's also important to have a solid business plan and marketing strategy. You can find more information about starting a farm in books and online resources."
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        recommendation = response.choices[0].text

else:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recommendation = response.choices[0].text

# Print the recommendation
print(recommendation)
