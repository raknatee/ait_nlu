import stanza

def main():
    nlp = stanza.Pipeline(lang='en')
    doc = nlp('No matter where you are:')
    print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
    print(doc.sentences[0].print_dependencies())



try:
    main()
except stanza.pipeline.core.ResourcesFileNotFoundError:
    stanza.download('en')
    main()