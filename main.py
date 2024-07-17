import pyttsx3
import PyPDF2

# Ensure there are no spaces in the file name string

# Use page.extract_text() instead of page.extractText()
book = open('software.pdf', 'rb')

# Use PdfReader instead of PdfFileReader
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Loop through the pages and read the text
for num in range(7, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

