#########################################################################
#                      IMPORT

import spacy

##############################################################################
#                     GLOBAL VARIABLES

# global example_var

#########################################################################
#                      PARAMETERS

# global nlp_sm

global nlp_lg

#########################################################################
#                      CLASSES
#------------------------------------------------------------------------

#########################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  accumulate

# Accumulate the elements of a list.

def accumulate(op, initial, inlist):
    l = inlist
    accum = initial
    if inlist == []:
        return initial
    else:
        while len(l) > 0:
            accum = op(*[accum, l[0]])
            l = l[1:len(l)] 
    return accum

# accumulate(lambda x, y: x + y, 0, [1,2,3,4])

#########################################################################
#                      INSTRUCTIONS

# to download from the shell
# python -m spacy download it_core_news_lg

#------------------------------------------------------------------------

# nlp_sm = spacy.load("it_core_news_sm")

nlp_lg = spacy.load("it_core_news_lg")

#------------------------------------------------------------------------

# doc = nlp_lg("La banana e la mela sono due esempi di frutta.")

# banana = doc[1]
# mela = doc[4] 
# esempi = doc[7]
# frutta = doc[9]
# la_banana_e_la_mela = doc[0:5]

# banana.similarity(mela)
# banana.similarity(frutta)
# mela.similarity(frutta)
# banana.similarity(esempi)
# la_banana_e_la_mela.similarity(mela)

#------------------------------------------------------------------------

doc = nlp_lg("La banana e la mela sono due esempi di frutta.")


#similarities = {}

#for x in doc:
#    for y in doc


#def get_sorted_word_similarity_list(word_list):
#    step1 = get_word_similarity_list(word_list)



#def get_word_similarity_list(word_list):
#    output = accumulate(lambda x, y: x + y, 0, word_list)
#    return output


# compute similarity    
similarities = {}   
for x in doc:
    similarities[x.text] ={}
    for y in doc:
        similarities[x.text].update({y.text:x.similarity(y)})

# sort
top10 = lambda x: {k: v for k, v in sorted(similarities[x].items(), key=lambda item: item[1], reverse=True)[:10]}

# desired output
top10("banana")






"""
text = "I have a text file that contains the content of a web page that I have extracted using BeautifulSoup. I need to find N similar words from the text file based on a given word. The process is as follows"
doc = nlp(text)
words = ['goal', 'soccer']



# compute similarity    
similarities = {}   
for word in words:
    tok = nlp(word)
    similarities[tok.text] ={}
    for tok_ in doc:
        similarities[tok.text].update({tok_.text:tok.similarity(tok_)})

# sort
top10 = lambda x: {k: v for k, v in sorted(similarities[x].items(), key=lambda item: item[1], reverse=True)[:10]}

# desired output
top10("goal")
{'need': 0.41729581641359625,
 'that': 0.4156277030017712,
 'to': 0.40102258054859163,
 'is': 0.3742535591719576,
 'the': 0.3735002888862756,
 'The': 0.3735002888862756,
 'given': 0.3595024941701789,
 'process': 0.35218102758578645,
 'have': 0.34597281472837316,
 'as': 0.34433650293640194}

"""

#------------------------------------------------------------------------
# List of all words in the corpus

# words = list(nlp_lg.vocab.strings)

# sentences (they are only four!)
# from spacy.lang.it.examples import sentences 


# sentences = list(nlp_lg(sentences))

