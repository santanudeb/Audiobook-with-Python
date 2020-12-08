# Libraries
import pyttsx3
import PyPDF2

# Opening the book and treating it as binary book
book = open('sample.pdf', 'rb')

# Reading the book
pdfReader = PyPDF2.PdfFileReader(book)

# Reading number of pages the pdf has
pages = pdfReader.numPages
print(pages)

# Speaker Initialization
speaker = pyttsx3.init()

# Speed
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)                          # current voice rate
speaker.setProperty('rate', 100)     # setting up new voice rate

# Volume
volume = speaker.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print(volume)                            # printing current volume level
speaker.setProperty('volume', 1.0)       # setting up volume level  between 0 and 1

# Voice
voices = speaker.getProperty('voices')           # getting details of current voice
speaker.setProperty('voice', voices[0].id)       # changing index, changes voices. 0 for male
# speaker.setProperty('voice', voices[1].id)     # changing index, changes voices. 1 for female

# Range(start page, end page)
for num in range(0, pages):
    page = pdfReader.getPage(num)    # Accessing every single page individually
    text = page.extractText()        # Extracting texts from the page
    speaker.say(text)
    speaker.runAndWait()
