import json
def createLabel():
     ## load dataset
     with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
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
     with open('../../retryData/test_labels_fullNov16Ver_Dec1','w') as l:
         json.dump(res,l)

createLabel()
             


