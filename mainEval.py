import fileinput
ref_folder_location = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\NBNewSummarizer\\complete_corpus\\human_evaluation\\'
machine_folder_location = 'C:\\Users\\amitjha\\Google Drive\\Spring\\NLP\\\\NBNewSummarizer\\'
scoreList = []
#create class to hold counters
class Score:
    def __init__(self,id):
        self.id = id
        self.pre = 0
        self.rec = 0
        self.f1 = 0
        self.match = 0

l = []

def buildList(fileN):
    filePointer = open(fileN, 'r', encoding='utf-8')
    s = '$'
    for refSumLine in filePointer:
        refSumLine = refSumLine.strip()
        s = s + refSumLine
    s = s.strip('$')
    s = s.strip('')
    listVal = s.split(u'\u0964')
    for i,value in enumerate(listVal):
        listVal[i] = listVal[i].strip()
    return listVal


inputCountS = input("Enter No. of Input files: ")
inputCount = int(inputCountS)
for i in range(1,inputCount+1,1):
    machinFile = 'article' + str(i)+'_system1.txt'
    refFile = 'article' + str(i) + '_reference1.txt'
    machinFile = machine_folder_location + machinFile
    refFile = ref_folder_location + refFile
    #open ref
    refList = buildList(refFile)
    machineList = buildList(machinFile)
    if refList[-1] == '':
        refList = refList[0:-1]
    if machineList[-1] == '':
        machineList = machineList[0:-1]

    if len(machineList) <= 0 or len(refList) <= 0:
        continue
    sref = set(refList)
    smac = set(machineList)
    if i == 3:
        for sr in sref:
            print(sr)
        print("Machine")
        for sm in smac:
            print(sm)
    matchSet = set(refList) & set(machineList)
    matchCount = len(matchSet)
    print(matchCount)
    #create object
    o = Score(i)
    o.match = matchCount
    o.pre =  o.match / len(machineList)
    o.rec = o.match / len(refList)
    deno = (o.pre + o.rec)
    if deno <= 0:
        continue
    o.f1 = 2 * ((o.pre * o.rec) / deno)
    scoreList.append(o)
s = 0
print("ID  =>  F1 Score")
for i in scoreList:
    s += i.f1
    strO = str(i.id) +' =>  ' + str(i.f1)
    print(strO)
if len(scoreList)<=0:
    avgFScore = 0
else:
    avgFScore = s/len(scoreList)
print("\n\nTotal Avg. F1 Score => " + str(avgFScore))


