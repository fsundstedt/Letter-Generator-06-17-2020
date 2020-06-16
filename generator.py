from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from datetime import date

font = 'Times-Roman'

print('Type company name below:')
companyName = input()
print('Type position below:')
position = input()

today = date.today()
dateString = today.strftime('%m-%d-%Y')

fileName = dateString + ' ' + companyName + '.pdf'
documentTitle = 'sample doc title'
title = 'sample title'
subTitle = 'sample subtitle'

blankLine = ''
intro = 'To Whom it May Concern,'
textLines = ['sample text here to test',' test']

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)

pdf.drawString(300, 770, title)
pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
text.setFont(font, 18)
text.textLine(intro)
text.textLine(blankLine)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)

pdf.save()