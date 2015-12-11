import json
from corenlp import StanfordCoreNLP

def f1f2f3f4f5f6f7():
    ## using corenlp to do split up job
    ## corenlp setting
    corenlp_dir = "stanford-corenlp-full-2014-08-27/"
    corenlp = StanfordCoreNLP(corenlp_dir)
    ## load dataset
    with open('../../dataclean_Nov8_2015/test_afterdataclean_modifiedcleanedTupleNov8.json') as t:
        trainTup = json.load(t)
    ## data structure to hold fea1 to fea7 a list
    feaLst = []
    for num,tup in enumerate(trainTup):
        ## after modify col8 and save, col8 now may be empty..
        if not tup[8]:
            continue
        print "No. %d tup in processing.." % (num)
        ## use corenlp to splitup
        res = corenlp.parse(tup[8])
        par = json.loads(res)
        print tup[8]
        ## use corenlp to get lemma and pos
        for p,word in enumerate(par["sentences"][0]['words']):
            print str(p)+'th w in tupl '+str(num)
            
            
            tmp = {}
            tmp['Word'] = word[0]
            tmp['Lemma'] = word[1]['Lemma']
            tmp['POS'] = word[1]['PartOfSpeech']
            feaLst.append(tmp)
        ## add pos-1,pos+1,pos-2 and pos+2    
        slen = len(feaLst)
        for ind,val in enumerate(feaLst):
            if (ind-1) >= 0 and (ind-1) <= slen-1:
                val['POS-1'] = feaLst[ind-1]['POS']
            else:
                val['POS-1'] = "NA"

            if (ind+1) >= 0 and (ind+1) <= slen -1:
                val['POS+1'] = feaLst[ind+1]['POS']
            else:
                val['POS+1'] = "NA"

            if (ind-2) >= 0 and (ind-2) <= slen -1:
                val['POS-2'] = feaLst[ind-2]['POS']
            else:
                val['POS-2'] = "NA"

            if (ind+2) >=0 and (ind+2) <= slen -1:
                val['POS+2'] = feaLst[ind+2]['POS']
            else:
                val['POS+2'] = "NA"
        
        for i in feaLst:
            print 'w:',i['Word'],' lemma:',i['Lemma'],' pos-2:',i['POS-2'],' pos-1:',i['POS-1'],' pos:',i['POS'],' pos+1:',i['POS+1'],' pos+2:',i['POS+2']
        
    with open('../../retryData/test_f1f2f3f4f5f6f7_Nov25.json','w') as o:
        json.dump(feaLst,o)
    print len(feaLst)






f1f2f3f4f5f6f7()
