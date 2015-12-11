import json
from corenlp import StanfordCoreNLP
## all features from tupleSet Nov16 version (not reduce [8666:8678], the tuple split unequal in depent with corenlp)
def mergeFullfeature_notIncludeF30():
    ## f1~f7 f31
    with open('../../retryData/test_f1f2f3f4f5f6f7f31_noPuncNum_Nov30.json') as a:
        f1f7f31 = json.load(a)
    with open('../../retryData/test_fea8_noPuncNum_Nov27.json') as b:
        f8 = json.load(b)
    with open('../../retryData/test_fea9_noPuncNum_Nov27.json') as c:
        f9 = json.load(c)
    with open('../../retryData/test_fea10_hedgeInContext_noPuncNum_Nov28.json') as d:
        f10 = json.load(d)
    with open('../../retryData/test_fea11_factiveVerb_noPuncNum_Nov27.json') as e:
        f11 = json.load(e)
    with open('../../retryData/test_fea12_factiveVerbInContext_noPuncNum_Nov28.json') as f:
        f12 = json.load(f)
    with open('../../retryData/test_fea13_assertiveVerb_noPuncNum_Nov28.json') as g:
        f13 = json.load(g)
    with open('../../retryData/test_fea14_assertiveVerbInContext_noPuncNum_Nov28.json') as h:
        f14 = json.load(h)
    with open('../../retryData/test_fea15_implicativeVerb_noPuncNum_Nov28.json') as i:
        f15 = json.load(i)
    with open('../../retryData/test_fea16_implicativeVerbInContext_noPuncNum_Nov28.json') as j:
        f16 = json.load(j)
    with open('../../retryData/test_fea17_reportVerb_noPuncNum_Nov28.json') as k:
        f17 = json.load(k)
    with open('../../retryData/test_fea18_reportVerbInContext_noPuncNum_Nov28.json') as l:
        f18 = json.load(l)
    with open('../../retryData/test_fea19_entailment_noPuncNum_Nov28.json') as m:
        f19 = json.load(m)
    with open('../../retryData/test_fea20_entailmentInContext_noPuncNum_Nov28.json') as n:
        f20 = json.load(n)
    with open('../../retryData/test_fea21_strongSubjective_noPuncNum_Nov28.json') as o:
        f21 = json.load(o)
    with open('../../retryData/test_fea22_strongSubjectiveInContext_noPuncNum_Nov28.json') as p:
        f22 = json.load(p)
    with open('../../retryData/test_fea23_weakSubjective_noPuncNum_Nov28.json') as q:
        f23 = json.load(q)
    with open('../../retryData/test_fea24_weakSubjectiveInContext_noPuncNum_Nov28.json') as r:
        f24 = json.load(r)
    with open('../../retryData/test_fea25_polarity_noPuncNum_Nov28.json') as s:
        f25 = json.load(s)
    with open('../../retryData/test_fea26_positiveWord_noPuncNum_Nov28.json') as t:
        f26 = json.load(t)
    with open('../../retryData/test_fea27_positiveWordInContext_noPuncNum_Nov28.json') as u:
        f27 = json.load(u)
    with open('../../retryData/test_fea28_negativeWord_noPuncNum_Nov28.json') as v:
        f28 = json.load(v)
    with open('../../retryData/test_fea29_negativeWordInContext_noPuncNum_Nov28.json') as w:
        f29 = json.load(w)
    with open('../../retryData/test_fea32_nov23.json') as x:
        f32 = json.load(x)
    
    for ai,bi,ci,di,ei,fi,gi,hi,ii,ji,ki,li,mi,ni,oi,pi,qi,ri,si,ti,ui,vi,wi,xi in zip(f1f7f31,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f32):
        if ai['Word'] == bi['Word'] == ci['Word'] == di['Word'] == ei['Word'] == fi['Word'] == gi['Word'] == hi['Word'] == ii['Word'] == ji['Word'] == ki['Word'] == li['Word'] == mi['Word'] == ni['Word'] == oi['Word'] == pi['Word'] == qi['Word'] == ri['Word'] == si['Word'] == ti['Word'] == ui['Word'] == vi['Word'] == wi['Word'] == xi['Word']:
            ai['Position in sentence'] = bi['Position in sentence']
            ai['Hedge'] = ci['Hedge']
            ai['Hedge in context'] = di['Hedge in context']
            ai['Factive verb'] = ei['Factive verb']
            ai['Factive verb in context'] = fi['Factive verb in context']
            ai['Assertive verb'] = gi['Assertive verb'] 
            ai['Assertive verb in context'] = hi['Assertive verb in context'] 
            ai['Implicative verb'] = ii['Implicative verb'] 
            ai['Implicative verb in context'] = ji['Implicative verb in context'] 
            ai['Report verb'] = ki['Report verb'] 
            ai['Report verb in context'] = li['Report verb in context']
            ai['Entailment'] = mi['Entailment']
            ai['Entailment in context'] = ni['Entailment in context'] 
            ai['Strong subjective'] = oi['Strong subjective'] 
            ai['Strong subjective in context'] = pi['Strong subjective in context'] 
            ai['Weak subjective'] = qi['Weak subjective'] 
            ai['Weak subjective in context'] = ri['Weak subjective in context'] 
            ai['Polarity'] = si['Polarity']
            ai['Positive word'] = ti['Positive word'] 
            ai['Positive word in context'] = ui['Positive word in context'] 
            ai['Negative word'] = vi['Negative word'] 
            ai['Negative word in context'] = wi['Negative word in context']
            ai['Collaborative feature'] = xi['Collaborative feature'] 

        else:
            print 'no'
            break
    with open('../../retryData/testfullFea_Nov16Ver_nof30_noreduce_Dec2.json','w') as ku:
        json.dump(f1f7f31,ku)



def addf30tofullFea():
    ## load f30
    with open('../../retryData/test_fea_f30_reduceUnequalSplit_Dec2.json') as f:
        f30 = json.load(f)
    ## load all other features
    with open('../../retryData/testfullFea_Nov16Ver_nof30_noreduce_Dec2.json') as a:
        others = json.load(a)
    ## delete the unequal split sentence from full feature set (no need for test set)
    # newOther = others[:8666] + others[8678:]
    newOther = others
    for b,c in zip(f30,newOther):
        if b['Word'] == c['Word']:
            c['Grammatical relation'] = b['Grammatical relation']
        else:
            print 'no'
            break
    with open('../../retryData/testFullFea32_reduceUnequalSplitNone_Dec2.json','w') as u:
        json.dump(newOther,u)


def label_reproduce_reduceUnequalSplit():
    with open('../../retryData/train_labels_fullNov16Ver_Dec1.json') as f:
        oldLabel = json.load(f)
    newLabel = oldLabel[:8666] + oldLabel[8678:]
    with open('../../retryData/trainFullFea32_reduceUnequalSplit_Dec2.json') as u:
        full = json.load(u)
    for i,j in zip(newLabel,full):
        if i[0] == j['Word']:
            pass
        else:
            print 'no'
            break

    with open('../../retryData/train_labels_reduceUnequalSplit_dec2.json','w') as b:
        json.dump(newLabel,b)


def label_noWord():
    with open('../../retryData/test_labels_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec2.json') as b: 
        label = json.load(b)
    res = []
    for i in label:
        res.append(i[1])
    with open('../../retryData/test_Onlylabels_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec2.json','w') as c:
        json.dump(res,c)

def findOriginSentenceContainMultipleBiasWord():
    ## load dataset
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_Dec9.json') as f:
        data = json.load(f)
    howmany = 0
    # fil = open('../../devDataclean_Dec8_2015/dev_biasWordNoOrMoreThanOnceInOriginalSentenceCol8_Dec8.json','w')
    for nu,tupl in enumerate(data):
        print nu
        num = tupl[3].count(tupl[2])
        if num != 1:
            print tupl
            print 'howmanytimes:',num
            # fil.write(str(tupl)+'\n')
            howmany+=1
        else:
            pass
    print howmany
    # fil.close()


## find the sentence number and index range of those sentence which has no bias word or more that one bias word in them
def findSentNumberIndexRange():
    ## load dataset
    with open('../../stripPuncNumber_Nov16_2015/train_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Nov16.json') as f:
        data = json.load(f)
    res = []
    cou = 0
    for nu,tupl in enumerate(data):
        num = tupl[3].count(tupl[2])
        cou += len(tupl[3])
        if num != 1:
            res.append((tupl[0],tupl[1],len(tupl[3]),nu,(cou-len(tupl[3])),cou,tupl[3]))
        else:
            pass
    with open('../../retryData/train_indexRange_biasWordNoOrMoreThanOnceInOriginalSentenceCol8_title_reviNum_lenSent_index_beginEnd_sent_Dec2.json','w') as u:
        json.dump(res,u)
    

def updatefullFea_reduceBiasWordNoneMorethanOne():
    with open('../../retryData/testFullFea32_reduceUnequalSplitNone_Dec2.json') as f:
        full = json.load(f)
    with open('../../retryData/test_indexRange_biasWordNoOrMoreThanOnceInOriginalSentenceCol8_title_reviNum_lenSent_index_beginEnd_sent_Dec2.json') as a:
        delSet = json.load(a)
    res_fullfea = []
    delIndex = []
    for num,dtupl in enumerate(delSet):
        delIndex = delIndex + range(dtupl[4],dtupl[5])
    # delIndex = delIndex + range(8666,8678)
    for ind,val in enumerate(full):
        if ind in delIndex:
            print val['Word']

        else:
            res_fullfea.append(val)
    with open('../../retryData/testFullFea32_reduceUnequalSplit_reduceBiasWordsNoneMoreThanOne_dec3.json','w') as t:
        json.dump(res_fullfea,t)


def updateLabel_reduceBiasWordNoneMorethanOne():
    with open('../../retryData/train_labels_fullNov16Ver_Dec1.json') as f:
        labl = json.load(f)
    with open('../../retryData/train_indexRange_biasWordNoOrMoreThanOnceInOriginalSentenceCol8_title_reviNum_lenSent_index_beginEnd_sent_Dec2.json') as a:
        delSet = json.load(a)
    res_labl = []
    delIndex = []
    for num,dtupl in enumerate(delSet):
        delIndex = delIndex + range(dtupl[4],dtupl[5])
    delIndex = delIndex + range(8666,8678)
    for ind, val in enumerate(labl):
        if ind in delIndex:
            print val[0]
        else:
            res_labl.append(val)
    with open('../../retryData/train_labels_reduceUnequalSplit_reduceBiasWordNoneMorethanOne_dec2.json','w') as t:
        json.dump(res_labl,t)


def updateSentLenFile_reduceBiasWordNoneMorethanOne():
    with open('../../retryData/test_indexRange_biasWordNoOrMoreThanOnceInOriginalSentenceCol8_title_reviNum_lenSent_index_beginEnd_sent_Dec2.json') as a:
        delSet = json.load(a)
    with open('../../retryData/test_sentLength_Nov30.json') as b:
        sentLen = json.load(b)
    delIndex = []
    res = []
    for d in delSet:
        delIndex.append(d[3])
    for num,val in enumerate(sentLen):
        if num in delIndex:
            print val
        else:
            res.append(val)

    with open('../../retryData/test_sentLength_reduceBiasWordNoOrMoreThanOnceInOriginalSentenceCol8.json','w') as c:
        json.dump(res,c)


def remove_tuples0MoreThan1BiasedWord():

## load dataset
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_Dec9.json') as f:
        data = json.load(f)
    res = []
    
    for nu,tupl in enumerate(data):
        num = tupl[3].count(tupl[2])
    
        if num != 1:
            pass
        else:
            res.append(tupl)
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json','w') as u:
        json.dump(res,u)
    


def remove_tuples0MoreThan1BiasedWord_fromOriginalTuple():
    ## using corenlp to do split up job
    ## corenlp setting
    corenlp_dir = "stanford-corenlp-full-2014-08-27/"
    corenlp = StanfordCoreNLP(corenlp_dir)
    
    ## load dataset
    with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTupleDec9.json') as t:
        trainTup = json.load(t)

    res2 = []
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
        print "good"
        ## count of biased word
        num = temp.count(tup[6])
        if num == 1:
            res2.append(tup)
    # with open('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTupleDec10.json','w') as f:
        # json.dump()
            
# remove_tuples0MoreThan1BiasedWord()


# updateSentLenFile_reduceBiasWordNoneMorethanOne()

# findOriginSentenceContainMultipleBiasWord()
# updatefullFea_reduceBiasWordNoneMorethanOne()
remove_tuples0MoreThan1BiasedWord_fromOriginalTuple()
