# -*- coding: utf-8 -*-
__author__ = 'wxbks'
from HTMLParser import HTMLParser
import re
import json
from unidecode import unidecode
from corenlp import StanfordCoreNLP


# import sys
#
# sys.path.append("/Users/wxbks/stanford-corenlp-python")


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def strip_http(str):
    str = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', str)
    # re.sub(r'^https?:\/\/.*[\r\n]*', '', str)
    return str

def strippedNoSquBrac(test_str):
    ret = ''
    # skip1c = 0 #[
    skip2c = 0 #<
    skip3c = 0 #{
    for i in test_str:
        if i == '<':
            skip2c += 1
        elif i == '{':
            skip3c += 1
        elif i == '>'and skip2c > 0:
            skip2c -= 1
        elif i == '>' and skip2c == 0:
            continue
        elif i == '}' and skip3c > 0:
            skip3c -= 1
        elif i == '}' and skip3c == 0:
            continue
        elif skip2c == 0 and skip3c == 0:
            ret += i
    return ret

def squrBracParse(str):
    if '[' in str and ']' in str:

        slist = re.findall('\[.*?\]\]?',str)


    elif '[' in str and ']' not in str:
        slist = re.findall('\[.*',str)
    else:
        return str
    print 'slist: ', slist
    for ins, sl in enumerate(slist):
        if '|' in sl:

            res1 = sl.split('|')
            if '-[' in str:
                str = str.replace(sl,res1[-1].strip(']'))
            else:
                str = str.replace(sl,' '+res1[-1].strip(']'))
        else:

            nsl = sl.strip('[]')
            str = str.replace(sl,' ' +nsl)

    return str

## input: full tuples of set (data-cleaned set without modifying each tuple)
## output: original sentence in col 9 is modified after cleaning. modified full tuples of set
def dataReduce_afterdataclean1975():
    ## test sent
    # str = "you are <h1> pig <img src='myPicture.png' alt=''> but http://www.g.com#jlsdfj*jlkdjf?ekjr! this is a snake, that is a [Chinese giant panda | panda]{data = 2015 | modified}. "
    tupleSet =  open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npovTrail2/Nov5data/testdataclean_col4True_col7singleBiaW_col9NotEmp_biasWordNotinTit_col7col8NotdifHyperL_col8within5_col7col8editDisGreat4_noStopWord_ProcBrack_Nov5.txt','r')
    newTupSet = []
    file = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npovTrail2/test_afterdataclean_modifiedcleanedTupleNov8.txt','w')
    for num,eachT in enumerate(tupleSet):

        print num,'  '+eachT
        line = eachT.decode('utf8')
        line = unidecode(line)
        line = line.lower()
        nline = line.rstrip('\n').split('\t')
        # print 'nline orin: ',nline
        str = nline[8]
        ## get rid of html tag,<h1>
        rid_htag = strip_tags(str)

        ## get rid of html hyperlink
        rid_htag_hlink = strip_http(rid_htag)
        ## get rid of {}, <>
        rid_htag_hlink_NonSqu = strippedNoSquBrac(rid_htag_hlink)
        ## deal with []
        finalStr = squrBracParse(rid_htag_hlink_NonSqu)
        nline[8] = finalStr
        ## save modified tuple to json
        newTupSet.append(nline)
        ## save modified tuple to file
        nl = '\t'.join(nline)
        file.write(nl+'\n')


    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npovTrail2/test_afterdataclean_modifiedcleanedTupleNov8.json','w') as o:
        json.dump(newTupSet,o)
    file.close()

## input: full tuple of set
## output: a split up of col8 original sent using stanford corenlp save to a file and a json
def afterModifyCol8_splitCol8():
    col8_splitup = []
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npovTrail2/Nov8data/train_afterdataclean_modifiedcleanedTupleNov8.json') as t:
        trainTup = json.load(t)
    corenlp_dir = "stanford-corenlp-full-2014-08-27V3.4.1"
    # corenlp_dir = "stanford-corenlp-full-2015-01-29"
    # corenlp_dir = "stanford-corenlp-full-2013-06-20"
    corenlp = StanfordCoreNLP(corenlp_dir)
    # res = corenlp.parse("Bell, a company which is based in LA, makes and distributes computer products. I hate you.")
    # par = json.loads(res)
    # for i in  par["sentences"][0]['dependencies']:
    #     print i
    for num, tup in enumerate([trainTup[1853]]):
        print 'No.',num
        print 'orin: ',tup[8]
        res = corenlp.parse(tup[8])
        par = json.loads(res)
        # print par
        slist =  par["sentences"][0]['words']
        # print slist
        temp = []
        for s in slist:
            temp.append(s[0])
        col8_splitup.append(temp)
        print temp
        ## check dependencies split
        dlist = par['sentences'][0]['dependencies']
        demp = []
        for d in dlist:
            demp.append(d)
        print demp
        if num == 4:
            break
    # for c in col8_splitup:
    #     print c




afterModifyCol8_splitCol8()