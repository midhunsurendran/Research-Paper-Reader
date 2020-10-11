from tkinter.filedialog import askopenfilename
import pyttsx3 as p
import pyPDF2


engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1])

paper=askopenfilename()
pdfReader=pyPDF2.PdfFileReader(paper)
pages=pdfReader.numPages

for num in range(0,pages):
    page=pdfReader.getpage(num)
    text=page.extractText()
    engine.say(text)
    engine.runAndWait()