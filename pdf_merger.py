from pypdf import PdfWriter
merger = PdfWriter()
num = int(input("Enter number of PDF files to merge: "))
pdfs = []
for i in range(num):
    name = input(f"Enter the name of PDF file {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()