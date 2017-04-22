import sys
import codecs
import math
#textfile  = open(sys.argv[1])
#labelfile = open(sys.argv[2])
textfile  = codecs.open("train-text.txt",encoding="utf-8")
labelfile = codecs.open("train-labels.txt",encoding="utf-8")
reviewsDict = {}
labels = {}
stopDict = {}
vocabDict = {}
priorDict = {}

for line in textfile:
    words = line.split(' ', 1)
    #words[1] = words[1].replace('.', ' ')
    #words[1] = words[1].replace(',', ' ')
    #words[1] = words[1].replace('/', ' ')
    review = words[1].split()
    li = " "
    for word in review:
        #word = word.strip('?:!.,\'<+[]=>;-_@%$&"()#*').lower()
        if word!='': #and word.isdigit() == False:
            vocabDict[word] = 0
        li += word + " "
    reviewsDict[words[0]] = li

textfile.close()


for line in labelfile:
    line = line.split()
    labelList = [line[1]]
    labels[line[0]] = labelList
labelfile.close()

#deceptive = 0
#truthful = 0
positive = 0
negative = 0
N = len(reviewsDict)
for label in labels.items():
    if label[1][0] == 'Y':
        positive += 1
    else:
        negative += 1

priorDict["Y"] = positive/N
priorDict["N"] = negative/N

classes = ["Y" , "N"]
probabilityDict = {}
for cl in classes:
    countTotal = 0
    reviewIds = [key for key,value in labels.items() if cl in value]
    for vocab in vocabDict.items():
        vocabDict[vocab[0]] = 0
        for id in reviewIds:
            ll=(reviewsDict[id])
            countWord = reviewsDict[id].count(" "+vocab[0]+" ")
            vocabDict[vocab[0]] += countWord
            countTotal += countWord

    for vocab in vocabDict.items():
        if vocab[0] not in probabilityDict:
            probabilityList = []
            probabilityList.append((vocab[1]+1)/(countTotal+ len(vocabDict)))
            probabilityDict[vocab[0]] = probabilityList
        else:
            prob = probabilityDict[vocab[0]]
            prob.append((vocab[1]+1)/(countTotal + len(vocabDict)))
            probabilityDict[vocab[0]] = prob

f = codecs.open("nbmodel.txt" , "w+", encoding="utf-8")
f.write("Prior Probabilities \n")
for line in priorDict.items():
    f.write(line[0]+"\t")
    f.write("%f\n" % line[1])
f.write("\n")
f.write("Conditional Probabilities \n")
f.write("TERM \t\t POSITIVE \t\t\t NEGATIVE \n")
for line in probabilityDict.items():
   f.write(line[0])
   for i in line[1]:
       f.write("\t %.15f" % i)
   f.write("\n")

