import json
import string

def f31():
    ## load dataset
    with open('../../retryData/test_f1f2f3f4f5f6f7_Nov25.json') as f:
        tupleSet = json.load(f)
    biasLexicon = []
    ## load biasLexicon
    with open('/home/sik211/dusk/npov_data/bias-lexicon/bias-lexicon.txt') as j:
        for li in j:
            li = li.rstrip('\n')
            biasLexicon.append(li)
    
    for tupl in tupleSet:
        if tupl['Lemma'] in biasLexicon:
            tupl['Bias lexicon'] = True
        else:
            tupl['Bias lexicon'] = False

    with open('../../retryData/test_f1f2f3f4f5f6f7f31_Nov26.json','w') as t:
        json.dump(tupleSet,t)

f31()
    
