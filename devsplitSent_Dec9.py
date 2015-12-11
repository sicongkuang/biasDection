import json
from corenlp import StanfordCoreNLP

## input: full tuple set of json file
## output: a list of lists of split-up col8
def splitCol8toWords(): 
    ## using corenlp to do split up job
    ## corenlp setting
    corenlp_dir = "stanford-corenlp-full-2014-08-27/"
    corenlp = StanfordCoreNLP(corenlp_dir)
    
    ## load dataset
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTupleDec9.json') as t:
        trainTup = json.load(t)

    fres = open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_Dec9.txt','w')

    split_res = []
    for num,tup in enumerate(trainTup):
        ## after modify col8 and save, col8 now may be empty..
        if not tup[8]:
            continue
        ## use corenlp to splitup
        res = corenlp.parse(tup[8])
        par = json.loads(res)
        slist = par["sentences"][0]['words']
        temp = []
        for s in slist:
            temp.append(s[0])
        split_res.append([tup[0],tup[1],tup[6],temp])
        fres.write(tup[0]+'\t'+tup[1]+'\t'+tup[6]+'\t'+','.join(temp)+'\n')
        print 'No.', num,tup[6]
        print tup[8]
        print [tup[0],tup[1],tup[6],temp]
    ## record new dataset
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_Dec9.json','w') as f:
        json.dump(split_res,f)
    fres.close()
splitCol8toWords()
