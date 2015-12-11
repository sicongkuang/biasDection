__author__ = 'wxbks'
import StanfordDependencies
import os
from nltk.parse import stanford
import json
from corenlp import StanfordCoreNLP


# sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
# # os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-corenlp-python-3.3.9/corenlp/stanford-corenlp-full-2014-08-27V3.4.1/'
# # os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-corenlp-python-3.3.9/corenlp/stanford-corenlp-full-2014-08-27V3.4.1/'
# # parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-corenlp-python-3.3.9/corenlp/stanford-corenlp-full-2014-08-27V3.4.1/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
#
# os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
# os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
# parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
#
#
#
# sentences =  parser.raw_parse("even if his equation  \\frac   = s(statement),  = (-1), =\sqrt -1 had a meaning, the ' signifier', ' signified' and ' statement' are are obviously not  numbers and the horizontal bar does not denote the  division of two numbers.")
# s=""
# for line in sentences:
#     for sentence in line:
#         s+=str(sentence)
#
# # print s
#
# sent = sd.convert_tree(s)
# print sent
# for t in sent:
#     print t[1]

def corenlpLemmaPOS_stanfordparserDependency_split_equalChecking():
    ## corenlp setting
    corenlp_dir = "stanford-corenlp-full-2014-08-27/"
    corenlp = StanfordCoreNLP(corenlp_dir)
    ## stanfordDependencies setting
    sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
    os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2014-08-27/'
    os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2014-08-27/'
    parser = stanford.StanfordParser(model_path="stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

    with open('../../dataclean_Nov8_2015/train_afterdataclean_modifiedcleanedTupleNov8.json') as t:
        trainTup = json.load(t)
    for num,tup in enumerate(trainTup):
        ## after modify col8 and save, col8 now may be empty..
        if not tup[8]:
            continue
    ## use corenlp to split sentence
        print 'No.', num
        print tup[8]
        res = corenlp.parse(tup[8])
        par = json.loads(res)
        slist =  par["sentences"][0]['words']
        print slist
        temp = []
        for s in slist:
            temp.append(s[0])
        print temp
        ## use stanfordDependencies to do split sentence
        sentences = parser.raw_parse(tup[8])
        s=""
        for line in sentences:
            for sentence in line:
                s+=str(sentence)

        sent = sd.convert_tree(s)
        print sent
        detemp = []
        for t in sent:
            detemp.append(t[1])
        print detemp
        for di,ti in zip(detemp,temp):
            if di == ti:
                pass
            else:
                if (ti == '(' and di == '-LRB-') or (ti == ')' and di == '-RRB-') or (ti == '[' and di == '-LSB-') or (ti == ']' and di == '-RSB-'):
                    print "diff in parenthesis"
                    pass
                else:
                    print "{",di,' ,',ti," }"






corenlpLemmaPOS_stanfordparserDependency_split_equalChecking()
