import PyPDF2

"""This program opens and reads a pdf"""

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfReader(pdfFile)
# print(len(reader.pages))

page = reader.pages[0]

# print(page.extract_text())

for pageNum in range(19):
    print(reader.pages[pageNum].extract_text())

# Close files
pdfFile.close()
