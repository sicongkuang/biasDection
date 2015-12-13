import json
import codecs
def f11(path_,factivePath_,newpath_):
    ## load factive list
    FactiveLst = filter(None,[ line.rstrip() for line in codecs.open(factivePath_,'r','utf-8') if ('#' not in line)])
    ## load dataset
    with open(path_) as f:
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
    with open(newpath_,'w') as r:
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


def f12(path_,factivePath_,newpath_):
    ## load factive list
    FactiveLst = filter(None,[ line.rstrip() for line in codecs.open(factivePath_,'r','utf-8') if ('#' not in line)])
    ## load dataset
    with open(path_) as f:
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
    with open(newpath_,'w') as o:
        json.dump(res,o)

# f11('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','/home/sik211/dusk/npov_data/bias_related_lexicons/factives_hooper1975.txt','../../devDataclean_Dec8_2015/dev_f11_factive_corenlpSplit_elimBias0orMoreThan1_Dec12.json')
f12('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','/home/sik211/dusk/npov_data/bias_related_lexicons/factives_hooper1975.txt','../../devDataclean_Dec8_2015/dev_f12_factiveContext_corenlpSplit_elimBias0orMoreThan1_Dec13.json')
