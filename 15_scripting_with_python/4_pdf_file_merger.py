import PyPDF2
import sys

inputs = ['list of pdfs']


def pdfmeregr(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdfmeregr(inputs)
