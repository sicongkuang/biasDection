import os
import json
import string
import unicodedata
from unidecode import unidecode
import sys
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
## input: article name
## output: a list of count of all words in that article
def getCount(artName):
    artLst = []

    for fn in os.listdir(indir):
        if not fn.endswith('.xml'): continue
        if ':' in fn:
            fn = fn.replace(':','/')
        fn = fn.decode('utf-8')
        fn_de = unidecode(fn)
        #fn = unicodedata.normalize("NFC",fn)
        newfn = fn_de[:-4]
        print 'artName: ',artName, 'eval: ', newfn
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

indir = "/home/sik211/dusk/npov-data/npov-train"
tes = getCount('semir osmanagic')
print tes['the']
