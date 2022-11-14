'''
PyPDF:  Pure-Python library built as a PDF toolkit. It is capable of: extracting document information (title, author,..)
splitting documents page by page, merging documents page by page, cropping pages, merging multiple pages into a single
page, encrypting and decrypting PDF files. By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries. It can also work entirely on StringIO objects rather than file streams, allowing for
PDF manipulation in memory. It is therefore a useful tool for websites that manage or manipulate PDFs.
-----------------------------------------------------------------------------------------------------------------

You see, depending on the program that you're running, it might not be able to read the PDF file.
So what we need to do, and this is just a standard that you have to remember, is that we want to read the binary.
So it's read and then binary. So what happens here is that this creates a file stream object. So it's going to convert
the file object to binary mode. So that the pdf to file reader. Can read this binary file object. So now if I run this
again, look at that. It's able to read it.
'''

import PyPDF2

# rb - read binary
filepath = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\dummy.pdf'
with open(filepath, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
