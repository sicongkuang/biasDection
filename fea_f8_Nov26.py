import json
def postionInSentence(s, i, n=3):
    '''
    :param s:length of sentence
    :param i: index of the word in question
    :return: position in senwl {start, mid, end}
    '''
    if s == 1:
        return "start"
    elif s == 2:
        if i + 1 == 1:
            return "start"
        else:
            return "end"
    else:
        avg = s/float(n)
        out = []
        last = 0.0
        while last < s:
            out.append(int(last + avg))
            last += avg
        # print avg
        # print out
        if i < out[0]:

            return "start"
        elif i >= out[0] and i < out[1]:
            # print " in mid"
            return "mid"
        else:
            # print "in end"
            return "end"



## put the whole sentence with punctuation and number and divide it into 3 parts
def f8_positionInsentence(path_,newpath_):
    ## load dataset
    # with open('../../dataclean_Nov8_2015/test_afterdataclean_modifiedcleanedTupleNov8.json') as t:
        # trainTup = json.load(t)
    # print trainTup[0]
    with open(path_) as f:
        tupleSet = json.load(f)
    res = []
    for tupl in tupleSet:
        tlen = len(tupl[3])
        for ind,word in enumerate(tupl[3]):
            pos = postionInSentence(tlen,ind)
            tdict = {}
            tdict['Word'] = word
            tdict['Position in sentence'] = pos
            res.append(tdict)
    with open(newpath_,'w') as r:
        json.dump(res,r)
            
f8_positionInsentence('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','../../devDataclean_Dec8_2015/dev_f8_corenlpSplit_elimBias0orMoreThan1_Dec12.json')
