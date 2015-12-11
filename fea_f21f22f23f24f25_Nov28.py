import json
import codecs

def subjectivePrepare(path,tag):
    f = codecs.open(path,"r","utf-8")
    lst = []
    for i in f:
        s = i.rstrip().split()
        t = s[0].split('=')
        if t[1] == tag:
            g = s[2].split('=')
            lst.append(g[1])
    with open('../../retryData/subjective'+tag+'Lst_Nov28.json','w') as o:
        json.dump(lst,o)
    return lst

def f21():
    ## first time load strong subjective list
    # StrongSubjLst = subjectivePrepare('/home/sik211/dusk/npov_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff','strongsubj')
    ## load strong subjective list from existing list json file
    with open('../../retryData/subjectivestrongsubjLst_Nov28.json') as o:
        StrongSubjLst = json.load(o)

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in StrongSubjLst:
                wsubj = True
            else:
                wsubj = False
            print word, wsubj
            tdict = {}
            tdict['Word'] = word
            tdict['Strong subjective'] = wsubj
            res.append(tdict)
    with open('../../retryData/train_fea21_strongSubjective_noPuncNum_Nov28.json','w') as r:
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


def f22():
    ## load strong subjective list from existing list json file
    with open('../../retryData/subjectivestrongsubjLst_Nov28.json') as o:
        StrongSubjLst = json.load(o)
    


    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            stext = contextCheck(StrongSubjLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Strong subjective in context'] = stext
            res.append(tdict)
            print ind, word, stext
    with open('../../retryData/test_fea22_strongSubjectiveInContext_noPuncNum_Nov28.json','w') as t:
        json.dump(res,t)

def f23():
    ## first time load weak subjective list
    # WeakSubjLst = subjectivePrepare('/home/sik211/dusk/npov_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff','weaksubj')
    ## load weak subjective list from existing list json file
    with open('../../retryData/subjectiveweaksubjLst_Nov28.json') as o:
        WeakSubjLst = json.load(o)

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in WeakSubjLst:
                wsubj = True
            else:
                wsubj = False
            print word, wsubj
            tdict = {}
            tdict['Word'] = word
            tdict['Weak subjective'] = wsubj
            res.append(tdict)
    with open('../../retryData/test_fea23_weakSubjective_noPuncNum_Nov28.json','w') as r:
        json.dump(res,r)

    
def f24():
    ## load weak subjective list from existing list json file
    with open('../../retryData/subjectiveweaksubjLst_Nov28.json') as o:
        WeakSubjLst = json.load(o)
    


    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            stext = contextCheck(WeakSubjLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Weak subjective in context'] = stext
            res.append(tdict)
            print ind, word, stext
    with open('../../retryData/train_fea24_weakSubjectiveInContext_noPuncNum_Nov28.json','w') as t:
        json.dump(res,t)

def polarityPrepare(path):
    f = codecs.open(path,"r","utf-8")
    pdict = {}
    for i in f:
        s = i.rstrip().split()
        t = s[2].split('=')
        w = s[5].split('=')
        # print t
        # print w
        pdict[t[1]] = w[1]
    with open('../../retryData/polarityDictionary_Nov28.json','w') as g:
        json.dump(pdict,g)
    return pdict

def polarityCheck(pdict,w):
    
    if w in pdict:
        return pdict[w]
    else:
        return 'NA'

def f25():
    ## first time load polarity dict
    # PolarityDict = polarityPrepare('/home/sik211/dusk/npov_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff')
    ## load polarity dict from existing json file
    with open('../../retryData/polarityDictionary_Nov28.json') as g:
        PolarityDict = json.load(g)
  
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            ptext = polarityCheck(PolarityDict,word)
            tdict = {}
            tdict['Word'] = word
            tdict['Polarity'] = ptext
            res.append(tdict)
            print ind, word, ptext
    with open('../../retryData/test_fea25_polarity_noPuncNum_Nov28.json','w') as t:
        json.dump(res,t)

f25()
