import PyPDF4
from sys import argv

def fix(name) :

    reader = PyPDF4.PdfFileReader(name)
    writer = PyPDF4.PdfFileWriter()


    for i in range(0, reader.numPages, 2):
        questionPage = reader.getPage(i)
        writer.addPage(questionPage)
        
        answerPage = reader.getPage(i+1)
        
        newPage1 = PyPDF4.pdf.PageObject.createBlankPage(None,
            answerPage.mediaBox.getWidth(), answerPage.mediaBox.getHeight())
        newPage1.mergeTranslatedPage(questionPage, answerPage.mediaBox.getWidth()/2, 0)
        newPage1.mergeTranslatedPage(answerPage, -answerPage.mediaBox.getWidth()/2, 0)
        writer.addPage(newPage1)

        newPage2 = PyPDF4.pdf.PageObject.createBlankPage(None,
            answerPage.mediaBox.getWidth(), answerPage.mediaBox.getHeight())
        newPage2.mergeTranslatedPage(questionPage, -answerPage.mediaBox.getWidth()/2, 0)
        newPage2.mergeTranslatedPage(answerPage, answerPage.mediaBox.getWidth()/2, 0)
        writer.addPage(newPage2)

    writer.write(open(name[:-4] + "__.pdf","wb"))

    
for i in range(1,len(argv)):
    print(argv[i])
    fix(argv[i])
    print("ok")
    
input("Press enter to exit ...")