import PyPDF2

"""This program takes two separate pdfs and combines them into one."""

# Create variables to open original pdfs
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

# Create a reader for each PDF
reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

# Create a writer variable to create new pdf
writer = PyPDF2.PdfWriter()

# Use a for loop to add reader 1
for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

# Use a for loop to add  reader 2
for pageNum in range(len(reader1.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

# Create a variable for new pdf
outputFile = open('combinedminutes.pdf', 'wb')

# Call  write function to write new pdf
writer.write(outputFile)

# Close files
outputFile.close()
pdf1File.close()
pdf2File.close()
