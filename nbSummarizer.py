import nltk
import codecs
import re
import operator
import math

from tokenizer import *
from collections import OrderedDict
#1. Get Sentence list with Sentid
sentenceDict = {}
sentenceDictLen = {}
sentenceDictTest = {}
featureVec = {}
sentenceDictLabel = {}
def print_dict(contentDIct,filename):
    fileName = "C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\NBNewSummarizer\\" + filename
    f = open(fileName, "w+", encoding="utf8")

    for sentence in contentDIct:
        #if (len(sentence.strip()) > 0):
        f.write(sentence + " " + contentDIct[sentence]+"\n")
    f.close()

def read_from_file(filename):
    f = codecs.open(filename, encoding='utf-8')
    data = f.read()
    f.close()
    return data

if __name__ == "__main__":
    no_of_inputs = 20          #No. of training files
    no_of_testSet = 8         #No. of Test files
    for x in range(1, no_of_inputs+1):
        fileContent = ''
        sentenceList = ''
        sentenceListSum = ''
        fileName = 'complete_corpus\\machine_output\\tokenized' + str(x) + ".txt"
        fileNameSummary = 'complete_corpus\\machine_output\\tokenizedSummary' + str(x) + ".txt"
        fileContent = read_from_file(fileName)
        fileContentSummary = read_from_file(fileNameSummary)
        #print("\n"+str(x) +":"+str(len(fileContent)))
        sentenceList = fileContent.split((u"।"))
        sentenceList = sentenceList[0:-1]
        sentenceListSum = fileContentSummary.split((u"।"))
        sentenceListSum = sentenceListSum[0:-1]
        no_of_sentence = len(sentenceList)
        for y in range(0,no_of_sentence):

            sentId = str(x)+'.'+str(y)
            sentenceDict[sentId] = sentenceList[y]
            if (sentenceDict[sentId] in sentenceListSum):
                sentenceDictLabel[sentId] = 'Y'# '+ sentenceDict[sentId]

            else:
                sentenceDictLabel[sentId] = 'N'
            sentenceDictLen[sentId] = len(sentenceDict[sentId].split())
    #print labels with ids
    print_dict(sentenceDict,"train-text.txt")
    print_dict(sentenceDictLabel,"train-labels.txt")

    for i in range(1,no_of_testSet+1):

        no_of_sentence_test = 0

        fileNameTest = 'complete_corpus\\testFile\\input' + str(i) + ".txt"
        fileContentTest = tokenize_testFile(fileNameTest)
        for q,flt in enumerate(fileContentTest):
            fileContentTest[q] = flt.replace(u"।",'')
        no_of_sentence_test = len(fileContentTest)
        for y in range(0, no_of_sentence_test):
            multi = str(i)+'.'+str(y)
            sentenceDictTest[multi] = fileContentTest[y]


    print_dict(sentenceDictTest, "test-text.txt")
