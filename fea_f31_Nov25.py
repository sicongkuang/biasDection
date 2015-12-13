import json
import string

def f31(pathf1f7_,biasfile_,newpath_):
    ## load dataset
    with open(pathf1f7_) as f:
        tupleSet = json.load(f)
    biasLexicon = []
    ## load biasLexicon
    with open(biasfile_) as j:
        for li in j:
            li = li.rstrip('\n')
            biasLexicon.append(li)
    
    for tupl in tupleSet:
        if tupl['Lemma'] in biasLexicon:
            tupl['Bias lexicon'] = True
        else:
            tupl['Bias lexicon'] = False

    with open(newpath_,'w') as t:
        json.dump(tupleSet,t)

f31('../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7_stripPuncNum_Dec12Ver2.json','/home/sik211/dusk/npov_data/bias-lexicon/bias-lexicon.txt','../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7f31_stripPuncNum_Dec12.json')
    
