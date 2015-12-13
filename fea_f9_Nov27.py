import codecs
import json
def f9(path_,hedgePath_,newpath_):
    ## load hedge list
     HedgeLst = filter(None,[ line.rstrip() for line in codecs.open(hedgePath_,'r','utf-8') if ('#' not in line)])
     ## load dataset
     with open(path_) as f:
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


## context check(2 words ahead and 2 words below)
def f10(path_,hedgePath_,feaPath_):
     ## load dataset
     with open(path_) as f:
        tupleSet = json.load(f)
    ## load hedge list
     HedgeLst = filter(None,[ line.rstrip() for line in codecs.open(hedgePath_,'r','utf-8') if ('#' not in line)])

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
     with open(feaPath_,'w') as o:
          json.dump(res,o)

# f10()
               
# f9('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','/home/sik211/dusk/npov_data/bias_related_lexicons/hedges_hyland2005.txt','../../devDataclean_Dec8_2015/dev_f9_corenlpSplit_elimBias0orMoreThan1_Dec12.json')
f10('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','/home/sik211/dusk/npov_data/bias_related_lexicons/hedges_hyland2005.txt','../../devDataclean_Dec8_2015/dev_f10_HedgeContext_corenlpSplit_elimBias0orMoreThan1_Dec13.json')
