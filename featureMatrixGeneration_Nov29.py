import json
import string

## input: path of a feature json file(not apply for fea30,since it has f30 use '-LRB-' to represent '(')
## output: save a new feature json file filtering out the tuples which punctuation and number as 'Word' value
def trimPuncNum(path,newPath):
    with open(path) as f:
        tupleSet = json.load(f)
    puncSet = set(string.punctuation)
    ## new list to store result without punc and num
    res = []
    for num,val in enumerate(tupleSet):
        print 'No.',num
        print 'orignal: '.rjust(10),str(val['Word']).rjust(80)
        temp = filter(None,[i.strip(string.punctuation) for i in [val['Word']] if not str(i).isdigit()])
        newWordLst = filter(None,[i.strip(string.punctuation) for i in temp if not str(i).isdigit()])
        print 'new: '.rjust(10),str(newWordLst).rjust(80)
        if newWordLst:
            res.append(val)
    print len(res)


    with open(newPath,'w') as o:
        json.dump(res,o)


# trimPuncNum('../../retryData/test_f30_wPunNum_Nov25.json','../../retryData/test_f30_noPuncNum_Nov30.json')


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

# trimPuncNum_f30('../../retryData/test_f1f2f3f4f5f6f7f31_Nov26.json','../../retryData/test_f1f2f3f4f5f6f7f31_noPuncNum_Nov30.json')


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


def temp():
    with open('../../retryData/train_fea32_nov23.json') as f1:
        f32 = json.load(f1)
    with open('../../retryData/train_f1f2f3f4f5f6f7f31_noPuncNum_Nov30.json') as f2:
        f1f31 = json.load(f2)
    with open('../../retryData/train_fea20_entailmentInContext_noPuncNum_Nov28.json') as f3:
        f20 = json.load(f3)
    for i,j,v in zip(f32,f1f31,f20):
        if i['Word'] == j['Word'] == v['Word']:
            
            pass
        else:
            print i['Word']
            print j['Word']
            print v['Word']
            print 'oh no'
            break
    print 'ok'
    print len(f1f31)
# temp()
