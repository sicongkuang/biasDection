import json
from nltk.corpus import stopwords
stop = stopwords.words('english')
def f33_stopwords():
    with open('../../retryData/trainFullFea32_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_dec3.json') as f:
        trainX = json.load(f)
        f.close()
        
    with open('../../retryData/testFullFea32_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_dec3.json') as tf:
        testX = json.load(tf)
        tf.close()

    ## for training
    for ea in trainX:
        if ea['Word'] in stop:
            ea['Stop word'] = True
        else:
            ea['Stop word'] = False
    for tea in testX:
        if tea['Word'] in stop:
            tea['Stop word'] = True
        else:
            tea['Stop word'] = False
    with open('../../retryData/trainFullFea33_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_stopwordfea_dec8.json','w') as a:
        json.dump(trainX,a)
    with open('../../retryData/testFullFea33_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_stopwordfea_dec8.json','w') as b:
        json.dump(testX,b)
    
f33_stopwords()
