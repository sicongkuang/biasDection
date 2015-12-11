import json
import codecs

def f15():
    ## load implicative verb list
    ImplicativeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/implicatives_karttunen1971.txt','r','utf-8') if ('#' not in line)])
    
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in ImplicativeLst:
                wimplicative = True
            else:
                wimplicative = False
            print word, wimplicative
            tdict = {}
            tdict['Word'] = word
            tdict['Implicative verb'] = wimplicative
            res.append(tdict)
    with open('../../retryData/test_fea15_implicativeVerb_noPuncNum_Nov28.json','w') as r:
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


def f16():
    ## load implicative verb list
    ImplicativeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/implicatives_karttunen1971.txt','r','utf-8') if ('#' not in line)])
    


    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            itext = contextCheck(ImplicativeLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Implicative verb in context'] = itext
            res.append(tdict)
            print ind, word, itext
    with open('../../train_fea16_implicativeVerbInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)
f16()

