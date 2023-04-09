from helper.pdf_reader import pdf_reader
from glob import glob
import os

import json 
import pandas as pd


from nltk.corpus import stopwords
stpwrds = set(stopwords.words('english'))


def clean_text(text):
  new_text = [word for word in text.split(" ") if word not in stpwrds]
  return " ".join(new_text)

gpt_data={"data":[]}
pdfdata="pdf_data" + "/*"

for pdf in glob(pdfdata):

    pdfname=pdf.split(os.sep)[-1].split(".")[0]
    prompt="Report on " + pdfname + "\n\n###\n\n"

    reader_obj=pdf_reader(pdf)

    raw_completion=reader_obj.main()
    # print(raw_completion)

    completion=clean_text(raw_completion)

    subdata={"prompt":prompt,"completion":completion[:2048]}
    gpt_data["data"].append(subdata)


with open("sample.json", "w") as outfile:
    json.dump(gpt_data, outfile)

df = pd.DataFrame(gpt_data["data"])
print(df.head())
df.to_csv('sample.csv', index=False, header=True)




