import codecs
import json
def f9():
    ## load hedge list
     HedgeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/hedges_hyland2005.txt','r','utf-8') if ('#' not in line)])
     ## load dataset
     with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
     res = []
     for tupl in tupleSet:
         for ind,word in enumerate(tupl[3]):
              
             if word in HedgeLst:
                 whedge = True
             else:
                 whedge = False
             print word, whedge
             tdict = {}
             tdict['Word'] = word
             tdict['Hedge'] = whedge
             res.append(tdict)
     with open('../../retryData/train_fea9_noPuncNum_Nov27.json','w') as r:
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


## context check(2 words ahead and 2 words below)
def f10():
     ## load dataset
     with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    ## load hedge list
     HedgeLst = filter(None,[ line.rstrip() for line in codecs.open('/home/sik211/dusk/npov_data/bias_related_lexicons/hedges_hyland2005.txt','r','utf-8') if ('#' not in line)])

     res = []
     for num,tupl in enumerate(tupleSet):
          print str(num)+' :'+str(tupl[3])
          for ind,word in enumerate(tupl[3]):
               htext = contextCheck(HedgeLst,tupl[3],ind)
               tdict = {}
               tdict['Word'] = word
               tdict['Hedge in context'] = htext
               res.append(tdict)
               print ind, word, htext
     with open('../../test_fea10_hedgeInContext_noPuncNum_Nov28.json','w') as o:
          json.dump(res,o)

f10()
               
