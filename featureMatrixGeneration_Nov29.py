import json
import string


def trimPuncNum_f30(path,newPath):
    with open(path) as f:
        tupleSet = json.load(f)

    ## new list to store result without punc and num
    res = []
    for num,val in enumerate(tupleSet):
        print 'No.',num
        print 'orignal: ',str(val['Word'])
        
        ## remove ( -LRB-, ) -RRB-, [ -LSB-, ] -RSB-
        if val['Word'] == '-LRB-' or val['Word'] == '-RRB-' or val['Word'] == '-LSB-' or val['Word'] == '-RSB-':
            continue
        temp = filter(None,[i.strip(string.punctuation) for i in [val['Word']] if not str(i).isdigit()])
        newWordLst = filter(None,[i.strip(string.punctuation) for i in temp if not str(i).isdigit()])
        print 'new: ',str(newWordLst)
        if newWordLst:
            val['Word'] = newWordLst[0]
            res.append(val)
    print len(res)


    with open(newPath,'w') as o:
        json.dump(res,o)

trimPuncNum_f30('../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7_stripPuncNum_Dec12.json','../../devDataclean_Dec8_2015/dev_f1f2f3f4f5f6f7_stripPuncNum_Dec12Ver2.json')


# def compare(file1,file2):
    
#     with open(file1) as f1:
#         wlst1 = json.load(f1)
#     with open(file2) as f2:
#         wlst2 = json.load(f2)
#     print file1,len(wlst1)
#     print file2,len(wlst2)
#     h1 = open('f30WordsLst6014.txt','w')
#     h2 = open('f32WordsLst5874.txt','w')
#     for i,j in zip(wlst1,wlst2):
#         h1.write(i['Word']+'\n')
#         h2.write(j['Word']+'\n')
#     h1.close()
#     h2.close()
            
    
# compare('../../retryData/test_f30_noPuncNum_Nov30.json','../../retryData/test_fea32_nov23.json')


def temp(fpth):
    with open(fpth) as f:
        data = json.load(f)
    l = 0
    for i in data:
        l+=len(i[3])
    print len(data)
    print l



temp('../../devDataclean_Dec8_2015/dev_afterdataclean_modifiedcleanedTuple_splitTitleNumBW_stripPuncNum_elimBiasWord0orMoreThanOne_Dec9.json')
