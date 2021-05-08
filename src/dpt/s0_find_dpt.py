import stanza
import pickle
import os
from dpt import Dpt,DptSet,DptFull

dataset_path = r"/home/data_for_dpt"
save_path = r"/home/output_dpt"

def main():
    found_dpt = DptSet()
    all_dpt = DptSet(duplication = True)
    nlp = stanza.Pipeline(lang='en')

    for dataset_filename in os.listdir(dataset_path):
        all_sentences_in_book = None
        with open(os.path.join(dataset_path,dataset_filename),"r") as input_file:
            all_sentences_in_book = input_file.read()

        doc = nlp(all_sentences_in_book)
        for sentence in doc.sentences:
            this_dpt = Dpt()
            this_full_dpt = DptFull()
            for word in sentence.words:
                this_dpt.add(word.id,word.head,word.deprel)
                this_full_dpt.add(word.id,word.text,word.head,word.deprel)

            found_dpt.add(this_dpt)
            all_dpt.add(this_full_dpt)


    print("all possible dpt",len(found_dpt))
    with open(f"{save_path}/dpt",'wb') as save_file:
        pickle.dump(found_dpt, save_file,protocol=pickle.HIGHEST_PROTOCOL)
    with open(f"{save_path}/all_dpt",'wb') as save_file:
        pickle.dump(all_dpt, save_file,protocol=pickle.HIGHEST_PROTOCOL)


try:
    main()
except stanza.pipeline.core.ResourcesFileNotFoundError:
    stanza.download('en')
    main()