import string
import json
import os
import sys
import StanfordDependencies
from nltk.parse import stanford

from corenlp import StanfordCoreNLP

def sentLength2file():
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        data = json.load(f)
    res = []
    for tupl in data:
        res.append(len(tupl[3]))
    sumi = 0
    for i in res:
        sumi += i
    print sumi
    with open('../../retryData/train_sentLength_Dec1.json','w') as o:
        json.dump(res,o)

# sentLength2file()

# def label_generation():
    
def trydepen():
    ## stanfordDependencies setting
    sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
    os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2014-08-27/'
    os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2014-08-27/'
    parser = stanford.StanfordParser(model_path="stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        data = json.load(f)

    ## record how many sentence split unequal
    sentSplitUnequal = 0
    ## structure to save {word:abc,gramatical relationship: xx}
    res = []
    for num,tupl in enumerate(data):
        if not tupl[3]:
            continue
        newStr = ' '.join(tupl[3])
        print num,newStr
        
        sentences = parser.raw_parse(newStr)
        s=""
        for line in sentences:
            for sentence in line:
                s+=str(sentence)

        sent = sd.convert_tree(s)
        
        tem = [] ## a list of the depent split words
        temp_gram = [] ## record gramatical relationship
        for t in sent:
            detemp = {}
            detemp['Word'] = t[1]
            detemp['Grammatical relation'] = t[7]
           
            temp_gram.append(detemp)
           
            tem.append(t[1])
        if tem != tupl[3]:
            print 'depen split:',tem
            print 'corenlp split:',tupl[3]
            sentSplitUnequal += 1
            ## record index
            print 'unequal sentence No.',num
            print 'No. of sentence:',num,'begin index:',len(res),'end index:',len(res)+len(tupl[3])

        else:
            
            res = res+temp_gram
    with open('../../retryData/test_fea_f30_reduceUnequalSplit_Dec2.json','w') as l:
        json.dump(res,l)
    print sentSplitUnequal
        
        

    

trydepen()
