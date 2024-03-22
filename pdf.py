import PyPDF2 as pdf
text = ""
pdf_reader = pdf.PdfReader("sample.pdf")

for p in (3, 4, 5):
    page = pdf_reader.pages[p]
    text += page.extract_text()

with open("text.txt", "w") as f:
    f.write(text)