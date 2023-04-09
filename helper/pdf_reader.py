import PyPDF2
  
# creating a pdf file object
class pdf_reader:
    def __init__(self, path) -> None:
        self.filePath=path
    
    def main(self):


        pdfFileObj = open(self.filePath, 'rb')
        
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        
        # number of pages in pdf file
        # print(pdfReader.numPages)
        pagesnum=len(pdfReader.pages)
        print(pagesnum)
        
        doc=""

        for page in range(pagesnum):
            # creating a page object
            pageObj = pdfReader.pages[page]
            
            # extracting text from page
            # print(pageObj.extractText())
            doc+= pageObj.extract_text() + " "
        
        # closing the pdf file object
            # pdfFileObj.close()

            # print("===>>>",doc)
        
        return doc
    