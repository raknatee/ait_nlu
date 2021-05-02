from pdfminer.high_level import extract_text
import os

files = os.listdir('/home/dataset')

for _file in files:
    text = extract_text(f'/home/dataset/{_file}')
    filename = os.path.splitext(_file)[0]
    with open(f'/home/output/{filename}.txt','w',encoding='utf-8') as output_file:
        output_file.write(text)
