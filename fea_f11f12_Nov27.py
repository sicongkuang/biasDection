import json
import codecs
def f11():
    ## load factive list
    FactiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/factives_hooper1975.txt','r','utf-8') if ('#' not in line)])
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in FactiveLst:
                wfactive = True
            else:
                wfactive = False
            print word, wfactive
            tdict = {}
            tdict['Word'] = word
            tdict['Factive verb'] = wfactive
            res.append(tdict)
    with open('../../retryData/test_fea11_factiveVerb_noPuncNum_Nov27.json','w') as r:
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


def f12():
    ## load factive list
    FactiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/factives_hooper1975.txt','r','utf-8') if ('#' not in line)])
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            ftext = contextCheck(FactiveLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Factive verb in context'] = ftext
            res.append(tdict)
            print ind, word, ftext
    with open('../../train_fea12_factiveVerbInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)
f12()
