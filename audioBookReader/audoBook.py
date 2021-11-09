
import pyttsx3
import PyPDF2

my_file = open('test.pdf', 'rb')
myFileReader = PyPDF2.PdfFileReader(my_file)
pages = myFileReader.numPages

work = pyttsx3.init()

for pageNumber in range(pages):
    page = myFileReader.getPage(pageNumber)
    text = page.extractText()
    work.say(text)
    work.runAndWait()
