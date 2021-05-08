import stanza
import pickle
import os
from dpt import Dpt,DptSet,DptFull

dataset_path = r"/home/data_for_dpt"
save_path = r"/home/output_dpt"

def main():
    words = {}
    nlp = stanza.Pipeline(lang='en')

    for dataset_filename in os.listdir(dataset_path):
        all_sentences_in_book = None
        with open(os.path.join(dataset_path,dataset_filename),"r") as input_file:
            all_sentences_in_book = input_file.read()

        doc = nlp(all_sentences_in_book)
        for sentence in doc.sentences:
            for word in sentence.words:
                word_string = word.text

                if(word_string.strip() in ["",",",",",'"']):
                    continue

                if(word_string not in words):
                    words[word_string] = 1
                else:
                    words[word_string]+=1
                

    with open(f"{save_path}/word_count.csv",'w') as save_file:
        for word in words:
            save_file.write(f"{word}, {words[word]}\n")
    


try:
    main()
except stanza.pipeline.core.ResourcesFileNotFoundError:
    stanza.download('en')
    main()