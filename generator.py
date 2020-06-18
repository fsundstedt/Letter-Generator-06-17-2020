from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from datetime import date
from textBody import personalInfo, textP2, textP3, textP4

font = 'Times-Roman'

print('Type company name below:')
companyName = input()
print('Type position below:')
position = input()

today = date.today()
fileDateString = today.strftime('%m-%d-%Y')
letterDateString = today.strftime('%m/%d/%Y')

fileName = fileDateString + '-' + companyName + '.pdf'

blankLine = ''

myInfoLines = personalInfo

intro = 'To Whom it May Concern,'

def textLinesP1():
    maxLength = 27
    textContent = ['I am writing to express my interest in the ' + position + ' position at ' + companyName + '.']
    print(len(textContent[0]))
    if (len(companyName) + len(position)) > maxLength:
        textContent = ['I am writing to express my interest in the ' + position + ' position at ', companyName + '.']
    return textContent

textLinesP2 = textP2

textLinesP3 = textP3

textLinesP4 = textP4

pdf = canvas.Canvas(fileName)

text = pdf.beginText(40, 790)
text.setFont(font, 12)

for line in myInfoLines:
    text.textLine(line)
text.textLine(blankLine)
text.textLine(blankLine)
text.textLine(letterDateString)
text.textLine(blankLine)
text.textLine(intro)
text.textLine(blankLine)
for line in textLinesP1():
    text.textLine(line)
text.textLine(blankLine)
for line in textLinesP2:
    text.textLine(line)
text.textLine(blankLine)
for line in textLinesP3:
    text.textLine(line)
text.textLine(blankLine)
for line in textLinesP4:
    text.textLine(line)
text.textLine(blankLine)

pdf.drawText(text)

pdf.save()