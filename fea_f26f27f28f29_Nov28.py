import json
import codecs
def f26():
    ## load positive list
    PositiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/opinion-lexicon-English/positive-words.txt','r','utf-8') if (';' not in line)])
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in PositiveLst:
                wpositive = True
            else:
                wpositive = False
            print word, wpositive
            tdict = {}
            tdict['Word'] = word
            tdict['Positive word'] = wpositive
            res.append(tdict)
    with open('../../retryData/train_fea26_positiveWord_noPuncNum_Nov28.json','w') as r:
        json.dump(res,r)

def contextCheck(checkLst,senWl,i):
    # checkLst = filter(None,[ line.rstrip() for line in open(path) if ('#' not in line)])
    slen = len(senWl)
    if slen == 1:
        return False
    if i - 1 >= 0 and i - 1 <= slen - 1:
        w = senWl[i - 1].lower()
        if w in checkLst:
            return True
    if i + 1 >= 0 and i + 1 <= slen - 1:
        w = senWl[i + 1].lower()
        if w in checkLst:
            return True
    if i - 2 >= 0 and i - 2 <= slen - 1:
        w = senWl[i - 2].lower()
        if w in checkLst:
            return True
    if i + 2 >= 0 and i + 2 <= slen - 1:
        w = senWl[i + 2].lower()
        if w in checkLst:
            return True
    return False


def f27():
    ## load positive list
    PositiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/opinion-lexicon-English/positive-words.txt','r','utf-8') if (';' not in line)])

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            ptext = contextCheck(PositiveLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Positive word in context'] = ptext
            res.append(tdict)
            print ind, word, ptext
    with open('../../test_fea27_positiveWordInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)

def f28():
    ## load negative list
    NegativeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/opinion-lexicon-English/negative-words.txt','r') if (';' not in line)])
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in NegativeLst:
                wnegative = True
            else:
                wnegative = False
            print word, wnegative
            tdict = {}
            tdict['Word'] = word
            tdict['Negative word'] = wnegative
            res.append(tdict)
    with open('../../retryData/test_fea28_negativeWord_noPuncNum_Nov28.json','w') as r:
        json.dump(res,r)
    
def f29():
    
    ## load negative list
    NegativeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/opinion-lexicon-English/negative-words.txt','r') if (';' not in line)])

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            ntext = contextCheck(NegativeLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Negative word in context'] = ntext
            res.append(tdict)
            print ind, word, ntext
    with open('../../retryData/train_fea29_negativeWordInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)


f29()
