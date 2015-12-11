import re
import json
import codecs
from nltk.corpus import stopwords

## according to Marta Recasens email: only use the first column of Berant's word list, and intersect with weibe's strong+weak
def entailfeaturePrepare(entail_path,weibe_path):
    
    stop = stopwords.words('english')
    ## get entail list
    entailSet = set()
    f = codecs.open(entail_path,"r","utf-8")
    for i in f:
        s = i.rstrip().split('\t')
        
        u = re.sub('@R@','',s[0])
        g = u.split()
        for b in g:
            entailSet.add(b)
    entailLst = [c for c in entailSet if c not in stop]
    ## get weibe's strong and weak list
    weibeLst = []
    weibe = codecs.open(weibe_path,"r","utf-8")
    for w in weibe:
        wlst = w.rstrip().split()
        temp = wlst[2].split('=')
        weibeLst.append(temp[1])
    ## intersect with entailLst and weibeLst
    newLst = list(set(entailLst) & set(weibeLst))
    with open('../../retryData/entailFirstCol_WeibeStrongWeak_intersection_Nov28.json','w') as l:
        json.dump(newLst,l)
    return newLst



def f19():
    ## first time load entailment list
    # entailLst = entailfeaturePrepare('/home/sik211/dusk/npov_data/reverb_local_global/Resource0812/reverb_local_clsf_all.txt','/home/sik211/dusk/npov_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff')
    ## load entailment list from existing list json file
    with open('../../retryData/entailFirstCol_WeibeStrongWeak_intersection_Nov28.json') as l:
        entailLst = json.load(l)
    

    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
              
            if word in entailLst:
                wentail = True
            else:
                wentail = False
            print word, wentail
            tdict = {}
            tdict['Word'] = word
            tdict['Entailment'] = wentail
            res.append(tdict)
    with open('../../retryData/test_fea19_entailment_noPuncNum_Nov28.json','w') as r:
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


def f20():

    ## second time load entailment list from existing file
    with open('../../retryData/entailFirstCol_WeibeStrongWeak_intersection_Nov28.json') as l:
        entailLst = json.load(l)
    


    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    res = []
    for num,tupl in enumerate(tupleSet):
        print str(num)+' :'+str(tupl[3])
        for ind,word in enumerate(tupl[3]):
            etext = contextCheck(entailLst,tupl[3],ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Entailment in context'] = etext
            res.append(tdict)
            print ind, word, etext
    with open('../../train_fea20_entailmentInContext_noPuncNum_Nov28.json','w') as o:
        json.dump(res,o)

f20()
