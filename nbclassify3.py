import sys
import math
import codecs
import operator
from tokenizer import *
#testtextfile = open(sys.argv[1])
testtextfile = codecs.open("test-text.txt",encoding="utf-8")
nbmodeltext = codecs.open("nbmodel.txt",encoding="utf-8")
learnList = []
priorDict = {}
conditionalProbDict = {}
reviewsDict = {}
finalMap = {}


vocabDict = {}
count = 0
no_of_test = 8


def read_from_file(filename):
    f = codecs.open(filename, encoding='utf-8')
    filetext = f.read()
    return filetext


def generate_sentences(content):
    '''generates a list of sentences'''
    text = content
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    text = text.replace(u'?', u'।')
    newContent = text.split(u"।")
    return newContent

def print_summary(fileName,contentList):
    #fileName = 'C:\Users\amitjha\Google Drive\Spring\NLP\Project\\NBNewSummarizer\\'+fileName
    f = codecs.open(fileName, "w+", encoding="utf-8")

    for sentence in contentList:
        #if (len(sentence.strip()) > 0):
        f.write(contentList[sentence] + " " + u"\u0964" + " ")
    f.close()

for line in nbmodeltext:
    if count in [1 , 2 ]:
        li = line.split('\t')
        priorDict[li[0]] = li[1].strip('\n')
    if count > 5:
        li = line.split('\t')
        probabList = [li[1],li[2].strip('\n')]
        conditionalProbDict[li[0]]= probabList
        vocabDict.setdefault(li[0])
    count += 1

for line in testtextfile:
    words = line.split(' ', 1)
    reviewsDict[words[0]] = words[1] #.lower()
testtextfile.close()

#Output File
f = codecs.open("nboutput.txt" , "w+",encoding="utf-8")
classes = ["Y" , "N"]
for l in reviewsDict.items():

    score = []
    W = []
    line = l[1]
    #line = line.replace('.', ' ')
    #line = line.replace(',', ' ')
    #line = line.replace('/', ' ')
    words = line.split()
    for word in words:
        #word = word.strip('?:!.,\'<>;-_@ %$&"()#*')
        if word in vocabDict:
            W.append(word)
    i = 0
    for c1 in classes:
        scoreValue = (math.log(float(priorDict[c1]) , 10))
        for word in W:
            tempList = conditionalProbDict[word]
            scoreValue += math.log(float(tempList[i]) , 10)
        score.append(scoreValue)
        i += 1
    f.write(l[0])
    #finalMap[l[0]] = score[0]
    if score[0] > score[1]:
        finalMap[l[0]] = 'Y'
        f.write("Y ")
    else:
        f.write("N ")
    f.write("\n")


orderMap = {}
j=1
while j <= no_of_test:
    summary_list_sentids = []
    #sorted_ans = {}
    orderMap = {}
    fileNameTest = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\complete_corpus\\testFile\\input' + str(j) + ".txt"
    #fileContentTest = tokenize_testFile(fileNameTest)
    originalTestFileList1 = read_from_file(fileNameTest)
    originalTestFileList = generate_sentences(originalTestFileList1)
    # for k,v in finalMap.items():
    #    if str(k).startswith(str(j)+'.'):
    #        orderMap[k] = v
    #sorted_ans = sorted(orderMap.items(), key=operator.itemgetter(1), reverse=True)
    #for i in sorted_ans:
    #    print(orderMap[i])
    # totalCountofSum = math.ceil(len(sorted_ans) * 0.3)
    # countV=0
    # sidList = []
    # finalSum = {}
    # for sr in sorted_ans:
    #     summary_list_sentids.append(sr[0])
    #     countV += 1
    #     if countV >= int(totalCountofSum):
    #         break
   # summary_list_sentids.sort()
   #  for sls in summary_list_sentids:
    #    sidList.append(int(sls.split(".")[1]))
    #sidList.sort()
    #z=0
    #for ss in sidList:
    #    idx = int(ss)
    #    finalSum[z]=originalTestFileList[idx]
    #    z+=1
    finalSum = {}
    z=0
    for k,v in finalMap.items():
       if str(k).startswith(str(j)+'.'):
           orderMap[k] = v

    for k1 in orderMap:
        t1 = int(k1.split('.')[1])
        finalSum[z] = originalTestFileList[t1]
        z+=1
    summaryFn = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\article' + str(j) + '_system1.txt'
    print_summary(summaryFn, finalSum)
    print(str(len(originalTestFileList))+":-"+str(len(finalSum))+":-"+str(math.ceil(0.3*len(originalTestFileList))))
    j+=1
    # for sentidSorted in summary_list_sentids:





