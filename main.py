
from PyPDF2 import PdfFileMerger as pdf
from tkinter import filedialog


def merger():
    merger = pdf(strict=False)

    lista = []

    arquivo1 = (filedialog.askopenfilename())
    arquivo2 = (filedialog.askopenfilename())
    lista.append(arquivo1)
    lista.append(arquivo2)

    for a in lista:
        merger.append(a)

    merger.write(filedialog.asksaveasfilename(defaultextension=".pdf"))

def pdf_to_word():
    pass

pdf_to_word()

