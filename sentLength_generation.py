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
    
def f30_usingCorenlpSplit(dataset_,f30file_):
    ## stanfordDependencies setting
    sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
    os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2014-08-27/'
    os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2014-08-27/'
    parser = stanford.StanfordParser(model_path="stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

    ## load dataset
    with open(dataset_) as f:
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
    with open(f30file_,'w') as l:
        json.dump(res,l)
    print sentSplitUnequal
        
        

def checkf1f7_f30_word(f1f7_,f30_):
    with open(f1f7_) as f1:
        f1f7 = json.load(f1)
    with open(f30_) as f2:
        f30 = json.load(f2)
    # res1 = []
    # res2 = []
    # for i in f1f7:
        # res1.append(i['Word'])
    # for j in f30:
        # res2.append(j['Word'])
    # if res1 == res2:
        # print 'ok'
    # else:
        # print 'no'
    for i,j in zip(f1f7,f30):
        if i['Word'] == j['Word']:
            pass
        else:
            print i['Word'],j['Word']


# f30_usingCorenlpSplit('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','../../devDataclean_Dec8_2015/dev_f30_corenlpSplit_elimBias0orMoreThan1_Dec12.json')
checkf1f7_f30_word('../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7_stripPuncNum_Dec12Ver2.json','../../devDataclean_Dec8_2015/dev_f30_corenlpSplit_elimBias0orMoreThan1_Dec12.json')
