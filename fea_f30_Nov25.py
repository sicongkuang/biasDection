import os
import sys
import StanfordDependencies
from nltk.parse import stanford
import json
from corenlp import StanfordCoreNLP
def f30():
    ## stanfordDependencies setting
    sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
    os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2014-08-27/'
    os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2014-08-27/'
    parser = stanford.StanfordParser(model_path="stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
    resDepent = []
    ## loaddataset
    with open('../../dataclean_Nov8_2015/test_afterdataclean_modifiedcleanedTupleNov8.json') as t: 
        dataset = json.load(t)

    for num, tup in enumerate(dataset):
        print 'No.'+str(num)+ ": "+ tup[8]
        if not tup[8]:
            continue
        
        ## use stanfordDependencies to do split sentence
        sentences = parser.raw_parse(tup[8])
        s=""
        for line in sentences:
            for sentence in line:
                s+=str(sentence)

        sent = sd.convert_tree(s)
        
        
        for t in sent:
            detemp = {}
            detemp['Word'] = t[1]
            detemp['Grammatical relation'] = t[7]
            print detemp
            resDepent.append(detemp)

    with open('../../retryData/test_f30_wPunNum_Nov25.json','w') as u:
        json.dump(resDepent,u)
    len(resDepent)
    # with open('../../retryData/test_f1f2f3f4f5f6f7_Nov25.json') as o:
    #     temp = json.load(o)
    # for i,v in zip(temp,detemp[:3]):
    #     if i['Word'] == v:
    #         pass
    #     else:
    #         print i['Word']
    #         print v
    #         print "oh no.."
    #         sys.exit("not match in words split of sentence")
        
f30()
