import stanza
from dpt import Dpt,DptSet
def main():
    found_dpt = DptSet()
    all_sentences_in_book = "Look up. Look down. No matter where you are:"
    nlp = stanza.Pipeline(lang='en')

   
    doc = nlp(all_sentences_in_book)
    for sentence in doc.sentences:
        this_dpt = Dpt()
        for word in sentence.words:
            this_dpt.add(word.id,word.head,word.deprel)
        found_dpt.add(this_dpt)
    print(found_dpt)


try:
    main()
except stanza.pipeline.core.ResourcesFileNotFoundError:
    stanza.download('en')
    main()