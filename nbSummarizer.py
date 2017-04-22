import nltk
import codecs
import re
import operator
import math
#from tf_idf import tf_idf
#from tf_isf import tf_isf
from tokenizer import *
from collections import OrderedDict
#1. Get Sentence list with Sentid
sentenceDict = {}
sentenceDictLen = {}
sentenceDictTest = {}
#sentenceDictLenTest = {}
featureVec = {}
#featureVecTest = {}
sentenceDictLabel = {}
#sentenceDictTest = {}
def print_dict(contentDIct,filename):
    fileName = "C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\"+filename
    f = open(fileName, "w+", encoding="utf8")

    for sentence in contentDIct:
        #if (len(sentence.strip()) > 0):
        f.write(sentence + " " + contentDIct[sentence]+"\n")
    f.close()

def print_summary(fileName,contentList):
    fileName = 'complete_corpus\\candidate_summary\\'+fileName
    f = open(fileName, "w+", encoding="utf8")

    for sentence in contentList:
        if (len(sentence.strip()) > 0):
            f.write(sentence.strip() + " " + u"\u0964" + " ")
    f.close()

def read_from_file(filename):
    f = codecs.open(filename, encoding='utf-8')
    data = f.read()
    f.close()
    return data
def merge(dict,res_idf_v,res_isf_v,sentenceDictLen_v,id):
    LocalfeatureVec = {}
    for key in dict.keys():
        #d = {"tfIsf": 0}
        d = {"length": 0}  # , "label":'N'}

        #if key in res_idf_v.keys():
            #d["tfIdf"] = res_idf_v[key]
       # if key in res_isf_v.keys():
            #d["tfIsf"] = res_isf_v[key]
        if key in sentenceDictLen_v.keys():
            d["length"] = sentenceDictLen_v[key]

        LocalfeatureVec[key] = d
    return LocalfeatureVec

if __name__ == "__main__":
    no_of_inputs = 20          #No. of training files
    no_of_testSet = 8         #No. of Test files
    for x in range(1, no_of_inputs+1):
        fileContent = ''
        sentenceList = ''
        sentenceListSum = ''
        fileName = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\complete_corpus\\machine_output\\tokenized' + str(x) + ".txt"
        fileNameSummary = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\complete_corpus\\machine_output\\tokenizedSummary' + str(x) + ".txt"
        fileContent = read_from_file(fileName)
        fileContentSummary = read_from_file(fileNameSummary)
        #print("\n"+str(x) +":"+str(len(fileContent)))
        sentenceList = fileContent.split((u"।"))
        sentenceList = sentenceList[0:-1]
        sentenceListSum = fileContentSummary.split((u"।"))
        sentenceListSum = sentenceListSum[0:-1]
        no_of_sentence = len(sentenceList)
        for y in range(0,no_of_sentence):
            #multi = math.pow(10,len(str(y)))
            #sentId = str(((x * multi) + y ) / multi)
            sentId = str(x)+'.'+str(y)
            sentenceDict[sentId] = sentenceList[y]
            #sentenceDict[((x * multi) + y ) / multi] = sentenceList[y]
            if (sentenceDict[sentId] in sentenceListSum):
                sentenceDictLabel[sentId] = 'Y'# '+ sentenceDict[sentId]

            else:
                sentenceDictLabel[sentId] = 'N'
            sentenceDictLen[sentId] = len(sentenceDict[sentId].split())
    #print labels with ids
    print_dict(sentenceDict,"train-text.txt")
    print_dict(sentenceDictLabel,"train-labels.txt")
    #classifier = nltk.classify.NaiveBayesClassifier.train(train)


    #--**--TestData Set-------------------------------------
    #---**-read test data ------------------------------
    for i in range(1,no_of_testSet+1):
        testIter = 0
        count = 0
        ans = []
        test = []
        ansWithSent = {}

        no_of_sentence_test = 0
        sentenceDictLenTest = {}
        featureVecTest = {}
        totalCountofSum = 0
        sorted_ans = []
        summary_list_sentids = []
        summary_list = []
        summaryFn = ''

        fileNameTest = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\Project\\NBNewSummarizer\\complete_corpus\\testFile\\input' + str(i) + ".txt"
        fileContentTest = tokenize_testFile(fileNameTest)
        for q,flt in enumerate(fileContentTest):
            fileContentTest[q] = flt.replace(u"।",'')
        no_of_sentence_test = len(fileContentTest)
        for y in range(0, no_of_sentence_test):
            multi = str(i)+'.'+str(y)
            sentenceDictTest[multi] = fileContentTest[y]


    print_dict(sentenceDictTest, "test-text.txt")
