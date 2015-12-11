import os
import json
import string
from unidecode import unidecode
import sys
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def filter_col8_punctuation_number():
    ## split of col8 contain punctuations and number and single character
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_Dec9.json') as f:
        split_tuples = json.load(f)
    print len(split_tuples)
    newStripTuples = list(split_tuples)
    ## get rid of puntuation and number first from the splits
    for num,val in enumerate(split_tuples):
        print 'No.',num
        print 'orignal: '.rjust(10),str(val[3]).rjust(80)
        temp = filter(None,[i.strip(string.punctuation) for i in val[3] if not str(i).isdigit()])
        newCol8 = filter(None,[i.strip(string.punctuation) for i in temp if not str(i).isdigit()])
        print 'new: '.rjust(10),str(newCol8).rjust(80)
        newStripTuples[num][3] = newCol8
        print 'orignal: '.rjust(10),str(val).rjust(80)
        print 'new: '.rjust(10),str(newStripTuples[num]).rjust(80)
    print len(newStripTuples)
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Dec9.json','w') as t:
        json.dump(newStripTuples,t)

## no use at all
def fea32_numerator():
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        data = json.load(f)
    artDict = {}
    for tupl in data:
        if tupl[0] in artDict:
            if tupl[2] in artDict[tupl[0]]:
                artDict[tupl[0]][tupl[2]] += 1
            else:
                artDict[tupl[0]][tupl[2]] = 1
        else:
            artDict[tupl[0]]={}
            artDict[tupl[0]][tupl[2]] = 1
    with open('../../retryData/test_f32_numerator_arti_BW_num_Nov17.json','w') as t:
        json.dump(artDict,t)


## global var: artNpovDict={artName:{bw:num}} for numerator of fea32
artNpovDict = {}

## global var: freqArtDict = [] for denominator of fea32 (word count in article)
freqArtDict = {}

## global var: wordFeature = [] hold fea32 and word
wordFeature = []

## global var: indir hold the position of articles
indir = "/home/sik211/dusk/npov-data/npov-test"

## input:the split col8 with article title and revision number and col6 word NOTE: indir, dataset(tupleSet) and fea32's dumped file should be unianmous in train or test.
## output: a json and a txt file of single word and feature 32 collaborative feature
def fea32_generation():
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/test_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        tupleSet = json.load(f)
    ## a var to hold all words count for a article
    global freqArtDict 
    freqArtName = ''
    
    ## data structure to hold f32
    fea32 = []
    
    for num,tupl in enumerate(tupleSet):
        ## get count for the biased word to prepair for denominotor of a specfic article
        if tupl[0] != freqArtName:
            # get all the words' count 
            freqArtDict = getCount(tupl[0])
            if -1 == freqArtDict:
                print "did not find article %s" % (tupl[0])
                sys.exit("error: did not find article")
            else:
                freqArtName = tupl[0]
                print "art: %s, done find freq" % (tupl[0])
        else:
            print "still same article %s" % (tupl[0])
        for word in tupl[3]:
            tdict = {}
            tdict['Word'] = word
            f32 = collaborFea(tupl[0],word)
            tdict['Collaborative feature'] = f32
            print num,tdict
            fea32.append(tdict)
        articleNpov(tupl[0],tupl[2])
    with open('../../retryData/test_fea32_nov23.json','w') as r:
        json.dump(fea32,r)
    print len(fea32)
    print len(tupleSet)

    
## input: article name and bw
## output: update artNpovDict,  the numerator
def articleNpov(artName,editWl):
    global artNpovDict
    if not editWl:
        return # if editWl empyty, do nothing
    if artName in artNpovDict:
        
        if editWl in artNpovDict[artName]:
            artNpovDict[artName][editWl] += 1
        else:
            artNpovDict[artName][editWl] = 1
    else:
        artNpovDict[artName] = {}
 
        artNpovDict[artName][editWl] = 1

## input: article name (to find numberator) and word in evalation
## output: f32 value
def collaborFea(artName,w):
    if artName in artNpovDict:
        if w in artNpovDict[artName]:
            num = artNpovDict[artName][w]
            print w + " 's bias freq(num): "+str(num)
            denom = getFreqArt(w)
            if denom == -1:
                print "did not find the word, %s in article, %s" % (w,artName)
                return 0
            else:
                print w+" 's freq in all revisions(denom): "+str(denom)
            # denom could not be zero
                return float(num)/denom
        else:
            return 0
    else:
        return 0

## input: word in evaluation
## output: get Word Count from current freqArtDict
def getFreqArt(w):
    print "len of freqArtDict: ",len(freqArtDict)
    # print freqArtDict['the']
    
    try:
        f = freqArtDict[w]
        print "freq of " + w+" : "+str(freqArtDict[w])
    except KeyError, e:
        print 'I got a Key Error - the word could not found in article is: %s' % w
        ## sys.exit()
        ## editWordNotFoundArticle.append(w)
        return -1
    return f



## input: article name
## output: a list of count of all words in that article
def getCount(artName):
    artLst = []
    #artDict = {}
    for fn in os.listdir(indir):
        if not fn.endswith('.xml'): continue
        if ':' in fn:
            fn = fn.replace(':','/')
        fn = fn.decode('utf-8')
        #fn = unicodedata.normalize("NFC",fn)
        fn_de = unidecode(fn)
        newfn = fn_de[:-4]
        #print 'artName: ',artName, 'eval: ', newfn
        newfn = newfn.lower()
        if newfn == artName:
            # print "found article begin processing"
            #print fn
            if '/' in fn:
                fn = fn.replace('/',':')
            fullname = os.path.join(indir, fn)
            tree = ET.parse(fullname)
            root = tree.getroot()
            page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')

            revisions = page.findall('{http://www.mediawiki.org/xml/export-0.7/}revision')
            for s in revisions:
                txt = s.find('{http://www.mediawiki.org/xml/export-0.7/}text')
                artLst.append(txt.text)
            artLst = filter(None,[one for one in artLst])
            # print "processing done; begin counting"
            vectorizer = CountVectorizer(min_df=1,token_pattern='([^\[\|\]\s\.\!\=\{\}\;\<\>\?\"\'\#\(\)\,\*]+)')
            X = vectorizer.fit_transform(artLst)
            artDict = dict(zip(vectorizer.get_feature_names(),np.asarray(X.sum(axis=0)).ravel()))
        
            return artDict
    return -1

# fea32_generation()
filter_col8_punctuation_number()
