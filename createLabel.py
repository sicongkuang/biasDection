import json
def createLabel(path,labelPath_):
     ## load dataset
     with open(path) as f:
        tupleSet = json.load(f)
     res = []
     for tupl in tupleSet:
         tupl_res = []
         for ind,word in enumerate(tupl[3]):
             if word != tupl[2]:
                 tupl_res.append((word,0))
             else:
                 tupl_res.append((word,1))
         res = res + tupl_res
     with open(labelPath_,'w') as l:
         json.dump(res,l)

createLabel('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','../../devDataclean_Dec8_2015/dev_labelwithWord_stripPuncNum_elimBiasWord0orMoreThanOne_Dec13.json')
             


