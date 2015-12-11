# -*- coding: utf-8 -*-
__author__ = 'wxbks'
import json
import string
from unidecode import unidecode
from corenlp import *
import sys
from nltk.corpus import stopwords

def trainProcess():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainGoodSentenceAfterDataCleanSep30V1.json') as f:
        trainSent = json.load(f)

    for t in trainSent:
        print t
        for v,i in enumerate(t):
            old = i
            new = i.strip(string.punctuation)
            denew = unidecode(new)
            denew = denew.strip()
            lnew = denew.lower()
            if lnew != old:
                t[v] = lnew


    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainGoodSentenceAfterDataCleanSep30V1_wordDeunicodeLowerPunc.json','w') as g:
        json.dump(trainSent,g)



def trainRemoveEmptyString_withPunc():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainGoodSentenceAfterDataCleanSep30V1_wordDeunicodeLowerPunc.json') as g:
        trainsent = json.load(g)
    asum=0
    for  a in trainsent:
        asum+=len(a)
    print 'len of current trainsent: ',asum
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/stripPunc_listSep10_training.json') as s:
        stripPuncLst = json.load(s)
        s.close()
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/emptyWordInTraining_Sep10.json') as e:
        emptyLst = json.load(e)
        e.close()

    # merge all to delLst
    delLst = stripPuncLst + emptyLst
    print delLst


    for i in delLst:
        #find the index in trainsent
        find = 0

        for ind,t in enumerate(trainsent):
            find+=len(t)
            if find >=(i[0]+1):
                break
        offset = i[0]+1 - (find - len(t))

        # if statement not necessary
        if i[1] == trainsent[ind][offset-1]:
            print "ok"
        else:
            print '**************************'
            print 'original sent: ', trainsent[ind]
            print "offset: ", offset-1
            print 'trainsent: ',trainsent[ind][offset-1]
            print 'dellist: ',i
            trainsent[ind].remove(trainsent[ind][offset-1])
            print 'modified sent: ', trainsent[ind]

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainGoodSentenceAfterDataCleanSep30V1_wordDeunicodeLowerPunc_remove5_oct4.json','w') as g:
        json.dump(trainsent,g)


def pos_sentwholesent():
    reload(sys)
    sys.setdefaultencoding('utf8')
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainGoodSentenceAfterDataCleanSep30V1_wordDeunicodeLowerPunc_remove5_oct4.json') as g:
        trainsent = json.load(g)
    sum=0
    for i in trainsent:
        sum+=len(i)
    print sum

    corenlp = StanfordCoreNLP()
    u=1
    allPos = []
    for s in trainsent:
        print u
        print s
        if not s:
            continue

        str = ' '.join(s)
        print str
        re = corenlp.parse(str)
        par = json.loads(re)
        poslist =  par["sentences"][0]['words']
        print poslist


        newPos = []
        for i in poslist:
            tmpPos = {}
            tmpPos['Word'] = i[0]
            tmpPos['POS'] = i[1]['PartOfSpeech']
            newPos.append(tmpPos)

        # add pos-1 pos-2
        slen = len(newPos)
        for ind,val in enumerate(newPos):
            if (ind-1) >= 0 and (ind-1) <= slen-1:
                val['POS-1'] = newPos[ind-1]['POS']
            else:
                val['POS-1'] = "NA"

            if (ind+1) >= 0 and (ind+1) <= slen -1:
                val['POS+1'] = newPos[ind+1]['POS']
            else:
                val['POS+1'] = "NA"

            if (ind-2) >= 0 and (ind-2) <= slen -1:
                val['POS-2'] = newPos[ind-2]['POS']
            else:
                val['POS-2'] = "NA"

            if (ind+2) >=0 and (ind+2) <= slen -1:
                val['POS+2'] = newPos[ind+2]['POS']
            else:
                val['POS+2'] = "NA"
        allPos.append(newPos)
        # if u==1:
        #     break
        u+=1
    # print allPos

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/train_word_POS_POS1_POS2_OCT4.json','w') as f:
        json.dump(allPos,f)



def testPOS_singleSent():
    reload(sys)
    sys.setdefaultencoding('utf8')
    s = "hilda toledano also known by some as maria pia of braganca march 13 1907 1995 began claiming in the 1930s to be an illegitimate child of king carlos of portugal by amelia laredo e murca"
    # text = s.decode("utf8")
    corenlp = StanfordCoreNLP()
    re = corenlp.parse(s)
    print re


def verifyPOStrain_removstopwordsMatch():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/train_word_POS_POS1_POS2_OCT5.json') as f:
        beforestop = json.load(f)

    # remove stopwords & char<=2
    noStop = []
    stops = set(stopwords.words('english'))
    for sen in beforestop:
        # print sen
        tmp = [x for x in sen if x['Word'] not in stops and len(x['Word']) > 2]
        # print tmp
        # break
        noStop.append(tmp)

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_removStopWord_char2_sep17.json') as p:
        trueTrain = json.load(p)

    noStopAllWord = []
    for l in noStop:
        for g in l:
            noStopAllWord.append(g)

    print len(trueTrain)
    print len(noStopAllWord)
    u=1
    for i,j in zip(noStopAllWord,trueTrain):

        print u
        if i['Word']==j['Word']:
            print "ok"
        else:
            print "nostop:",i['Word']
            print "trueTrain:",j['Word']
        if u==2000:
            break
        u+=1
        # if i['Word'] != j['Word']:
        #     print 'noStopAllWord: ', i
        #     print 'trueTrain: ', j



    # with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/train_word_POS_POS1_POS2_OCT5_noStopWords_char2.json','w') as t:
    #     json.dump(noStop,t)

def lenthInfoVerify():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/senWlLen_lst.json') as f:
        trainLen = json.load(f)

    sum=0
    for i in trainLen:
        sum+=i

    print sum

    print len(trainLen)

    # multiple to del
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/stripPunc_listSep10_training.json') as s:
        stripPuncLst = json.load(s)
        s.close()
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/emptyWordInTraining_Sep10.json') as e:
        emptyLst = json.load(e)
        e.close()
    newTrain75 = list(trainLen)
    # merge all to delLst
    delLst = stripPuncLst + emptyLst
    delIndex = []
    for u in delLst:
        delIndex.append(u[0])
    print delIndex

    for i in delIndex:
        lsum = 0
        n=0
        while (i+1) >= lsum:
            lsum+=trainLen[n]
            n+=1
        if trainLen[n-1] == 1:
            newTrain75[n-1]=-1
        else:
            newTrain75[n-1] = newTrain75[n-1]-1

    finalTrain75 = [i for i in newTrain75 if i != -1]

    fsum=0
    for i in finalTrain75:
        fsum+=i

    print fsum

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/finalTrain75_senLenth.json','w') as t:
        json.dump(finalTrain75,t)



def index_stopwords_char2_training_toDelete():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_removStopWord_char2_sep17.json') as f:
        fullFea = json.load(f)
    print len(fullFea)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_sep14.json') as j:
        beforeRemove = json.load(j)

    stops = set(stopwords.words('english'))
    indexRemove = []

    for i,j in enumerate(beforeRemove):
        if j['Word'] in stops or len(j['Word']) <= 2:
            indexRemove.append(i)

    print len(fullFea)
    print len(beforeRemove)
    print len(beforeRemove) - len(indexRemove)

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainAfterRemoveEmpty_RemovPunc_indextoremove_stopWordsChar2_OCT6.json','w') as t:
        json.dump(indexRemove,t)



def getSenLen_afterRemoveStopWords_Char2():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainAfterRemoveEmpty_RemovPunc_indextoremove_stopWordsChar2_OCT6.json') as f:
        indexRemove = json.load(f)

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/finalTrain75_senLenth.json') as t:
        train75senLen = json.load(t)

    finalSenLen = list(train75senLen)

    for i in indexRemove:
        sum = 0
        n=0
        while (i+1) > sum:
            sum+=train75senLen[n]
            n+=1
        if train75senLen[n-1] == 1:
            finalSenLen[n-1] = -1
        else:
            finalSenLen[n-1] = finalSenLen[n-1] - 1

    f_senlen = [i for i in finalSenLen if i != -1]
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/finalTrain157072_senLength_removeStopWordsChar2.json','w') as o:
        json.dump(f_senlen,o)

    # lsum = 0
    # for i in f_senlen:
    #     lsum+=i
    # print lsum
    # with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_removStopWord_char2_sep17.json') as f:
    #     fullFea = json.load(f)
    # print len(fullFea)




def testGetSentLen_removeIndex():
    train75senLen = [5,1,3,0]
    indexRemove = [4,5,6,7,8]
    finalSenLen = list(train75senLen)

    for i in indexRemove:
        sum = 0
        n=0
        while (i+1) > sum:

            sum+=train75senLen[n]
            n+=1
        print n-1
        if train75senLen[n-1] == 1:
            finalSenLen[n-1] = -1
        else:
            finalSenLen[n-1] = finalSenLen[n-1] - 1
        print 'index to remove: ',i
        print 'after remove: ',finalSenLen

    f_senlen = [i for i in finalSenLen if i != -1]
    print f_senlen


def beforeRemoveStopWords_getPOS():
    reload(sys)
    sys.setdefaultencoding('utf8')
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/finalTrain75_senLenth.json') as t:
        train75senLen = json.load(t)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_sep14.json') as j:
        beforeRemove = json.load(j)
    # updatePos = list(beforeRemove)
    corenlp = StanfordCoreNLP()
    v = 1 # sentence number
    b = 0
    for i in train75senLen:
        if i==0:
            continue
        tmp = beforeRemove[b:b+i]
        sen = []
        for t in tmp:
            sen.append(t['Lemma'])
        str=' '.join(sen)
        re=corenlp.parse(str)
        par = json.loads(re)
        poslist =  par["sentences"][0]['words']

        newPos = []
        for p in poslist:
            tmpPos = {}
            tmpPos['Lemma'] = p[0]
            tmpPos['POS'] = p[1]['PartOfSpeech']
            newPos.append(tmpPos)

        # if len(newPos) == i:
        #     pass
        # else:
        #     print

        # add pos-1 pos-2
        slen = len(newPos)
        for ind,val in enumerate(newPos):
            if (ind-1) >= 0 and (ind-1) <= slen-1:
                val['POS-1'] = newPos[ind-1]['POS']
            else:
                val['POS-1'] = "NA"

            if (ind+1) >= 0 and (ind+1) <= slen -1:
                val['POS+1'] = newPos[ind+1]['POS']
            else:
                val['POS+1'] = "NA"

            if (ind-2) >= 0 and (ind-2) <= slen -1:
                val['POS-2'] = newPos[ind-2]['POS']
            else:
                val['POS-2'] = "NA"

            if (ind+2) >=0 and (ind+2) <= slen -1:
                val['POS+2'] = newPos[ind+2]['POS']
            else:
                val['POS+2'] = "NA"
        # print newPos

        # update the fullFea


        if len(newPos) == i:
            for indf,indn in zip(beforeRemove[b:b+i],newPos):
                print "number of sent:",v
                print "original word in the fullFea: ", indf['Lemma']
                print "word after pos parser: ",indn['Lemma']
                print "orignal Word: ",indf['Lemma'], ": original POS: ", indf['POS'], "; POS-1: ",indf['POS-1'], "; POS+1: ",indf['POS+1'], "; POS-2: ",indf['POS-2'], "; POS+2: ",indf['POS+2']
                print "word after parser: ",indn['Lemma'], ": new POS: ", indn['POS'], "; nPOS-1: ",indn['POS-1'], "; nPOS+1: ",indn['POS+1'], "; nPOS-2: ",indn['POS-2'], "; nPOS+2: ",indn['POS+2']
                # print "original sent: ", indf['Word']
                if indf['Lemma'] == indn['Lemma']:
                    indf['POS'] = indn['POS']
                    indf['POS-1'] = indn['POS-1']
                    indf['POS+1'] = indn['POS+1']
                    indf['POS-2'] = indn['POS-2']
                    indf['POS+2'] = indn['POS+2']
                else:
                    print "problem!"
                    # print "word in newPos: ", indn['Word']
                    exit()
                # print "modified sent: ", indf
        else:
            print "*************************number of sentence: ",v
            pass

        v+=1
        b=b+i
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_sep14_POS1POS2INputSentenceCorenlp_OCT7.json','w') as s:
        json.dump(beforeRemove,s)


    # sum=0
    # for i in train75senLen:
    #     sum+=i
    # print sum
    # print len(beforeRemove)

def afterUpdatePOS_removeStopwordsChar2():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_sep14_POS1POS2INputSentenceCorenlp_OCT7.json') as f:
        fullFea = json.load(f)

    print len(fullFea)

    stops = set(stopwords.words('english'))

    index = []
    for i,j in enumerate(fullFea):
        if j['Word'] in stops or len(j['Word']) <=2:
            index.append(i)

    # newfullFea = [t for x,t in enumerate(fullFea) if x not in index]
    #
    # print len(newfullFea)

    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/train75_indextoRemove_forStopWordsChar2_Oct8.json','w') as v:
        json.dump(index,v)

    # with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/trainfullFea_WordLowerUnidecode_LemmaCorenlp_removeEmpty_removStripPunc_biasLex2art_sep14_POS1POS2INputSentenceCorenlp_RemovStopWordsChar2_OCT7.json','w') as n:
    #     json.dump(newfullFea, n)


def afterUpdatePOS_removeStopwordsChar_testset():
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/fullFea_testset_UPdateMyBiasLex_downCase_lemma_2edit_2article_updateWordLowerUnidecode_corenlpLemmaSep11_POS1POS2InputSentCorenlp_Oct7.json') as f:
        testFullFea = json.load(f)
    print len(testFullFea)
    stops = set(stopwords.words('english'))
    index = []
    for i,j in enumerate(testFullFea):
        if j['Word'] in stops or len(j['Word']) <=2:
            index.append(i)
    newfullFea = [t for x,t in enumerate(testFullFea) if x not in index]
    print len(newfullFea)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/fullFea_testset_UPdateMyBiasLex_downCase_lemma_2edit_2article_updateWordLowerUnidecode_corenlpLemmaSep11_POS1POS2InputSentCorenlp_Oct7_RemovStopWordsChar2_Oct7.json','w') as l:
        json.dump(newfullFea,l)

# beforeRemoveStopWords_getPOS()
afterUpdatePOS_removeStopwordsChar2()
# afterUpdatePOS_removeStopwordsChar_testset()
# getSenLen_afterRemoveStopWords_Char2()
# testGetSentLen_removeIndex()
# trainRemoveEmptyString_withPunc()
# trainProcess()
# pos_sentwholesent()
# testPOS_singleSent()
# verifyPOStrain_removstopwordsMatch()
# lenthInfoVerify()
# index_stopwords_char2_training_toDelete()