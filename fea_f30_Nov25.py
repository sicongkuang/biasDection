import os
import sys
import StanfordDependencies
from nltk.parse import stanford
import json
from corenlp import StanfordCoreNLP
def f30(file_,wfile_):
    ## stanfordDependencies setting
    sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
    os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2014-08-27/'
    os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2014-08-27/'
    parser = stanford.StanfordParser(model_path="stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
    resDepent = []
    ## loaddataset
    with open(file_) as t: 
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

    with open(wfile_,'w') as u:
        json.dump(resDepent,u)
    print len(resDepent)
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

def checkCorenlpsplit(file1_,file2_):
    with open(file1_) as f:
        data1 = json.load(f)
    with open(file2_) as t:
        data2 = json.load(t)
    for i,j in zip(data1,data2):
        if i['Word'] != j['Word']:
            print i['Word']
            print j['Word']

# f30('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_elimBiasWord0orMoreThanOne_fullTup_Dec11.json','../../devDataclean_Dec8_2015/dev_f30_Dec11.json')
checkCorenlpsplit('../../devDataclean_Dec8_2015/dev_f30_Dec11.json','../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7_Dec11.json')
