import json
import codecs

def f13():
    ## load assertive verb list
    AssertiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/assertives_hooper1975.txt','r','utf-8') if ('#' not in line)])
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in AssertiveLst:
                wassertive = True
            else:
                wassertive = False
            print word, wassertive
            tdict = {}
            tdict['Word'] = word
            tdict['Assertive verb'] = wassertive
            res.append(tdict)
    with open('../../retryData/train_fea13_assertiveVerb_noPuncNum_Nov28.json','w') as r:
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


def f14():
    ## load assertive verb list
    AssertiveLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/assertives_hooper1975.txt','r','utf-8') if ('#' not in line)])

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            atext = contextCheck(AssertiveLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Assertive verb in context'] = atext
            res.append(tdict)
            print ind, word, atext
    with open('../../test_fea14_assertiveVerbInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)
f14()

