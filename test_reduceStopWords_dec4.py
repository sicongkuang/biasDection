import json
from nltk.corpus import stopwords
stop = stopwords.words('english')

def testFeaSet2SentWithLabl():
    with open('../../retryData/testFullFea32_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_dec3.json') as a:
        fullFea = json.load(a)
    with open('../../retryData/test_labels_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec2.json') as b:
        labl = json.load(b)
    with open('../../retryData/test_sentLength_reduceBiasWordNoOrMoreThanOnceInOriginalSentenceCol8.json') as c:
        sentLength = json.load(c)

    for d,e in zip(fullFea,labl):
        if d['Word'] == e[0]:
            d['label'] = e[1]
        else:
            print d['Word'],'**************'
            break
    
    base = 0
    newFullFea = []
    for f in sentLength:
        if f == 0:
            print 'sent length is 0!'
            continue
        temp = fullFea[base:base+f]
        newFullFea.append(temp)
        base = base + f
    
    with open('../../retryData/test_fullFeawLabel_listoflistSent_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec4.json','w') as g:
        json.dump(newFullFea,g)

# testFeaSet2SentWithLabl()

def removStopWord():
    with open('../../retryData/test_fullFeawLabel_listoflistSent_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec4.json') as a:
        data = json.load(a)
    fullfealab = []
    for sent in data:
        tmp = []
        for word in sent:
            if word['Word'] not in stop:
                tmp.append(word)
        fullfealab.append(tmp)

    with open('../../retryData/test_fullFeawLabel_listoflistSent_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_reduceStopWord_dec4.json','w') as c:
        json.dump(fullfealab,c)

# removStopWord()

def afterRemovStop_label():
    with open('../../retryData/test_fullFeawLabel_listoflistSent_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_reduceStopWord_dec4.json') as a:
        fullfealab = json.load(a)
    labl = []
    for sent in fullfealab:
        for word in sent:
            labl.append(word['label'])
    print labl[:4]
    for ss in fullfealab:
        for o in ss:
            o.pop('label')
    sentLen = []
    for i in fullfealab:
        sentLen.append(len(i))
    
    fea = []
    for b in fullfealab:
        fea = fea + b
    with open('../../retryData/test_labels_reduceUnequalSplitNone_reduceBiasWordNoneMorethanOne_reduceStop_dec4.json','w') as n:
        json.dump(labl,n)
    with open('../../retryData/test_fullFea32_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_reduceStop_dec3.json','w') as o:
        json.dump(fea,o)
    with open('../../retryData/test_sentLenth_reduceBiasWordNoOrMoreThanOnceInOriginalSentenceCol8_reduceStop_dec4.json','w') as j:
        json.dump(sentLen,j)

afterRemovStop_label()
