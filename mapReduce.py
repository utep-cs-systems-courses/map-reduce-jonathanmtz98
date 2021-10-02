#Jonathan Martinez
import pymp
import time

def mapReduce(files, words):
    dictRet = pymp.shared.dict()
    #dictRect = pymp.shared.list([0])
    with pymp.Parallel() as p:#Parallelize process
        sumLock = p.lock#Call sumlock
        for wordsf in p.iterate(files):#Iterate files in order to be traversed
            for everyword in wordsf:
                for word in words:
                    if word in everyword.lower():
                        sumLock.acquire()
                        if word not in dictRet:#If there is no word already...
                            dictRet[word] = 0
                        dictRet[word] +=1
                        #if everyword.replace('\n').lower() == words:
                         #   dictRet[listWord] = dictRet[listWord] + 1
                        sumLock.release()
    return dictRet

def appendFiles(openFiles):
    filestorage = []#Words will be stored here
    for readingFiles in openFiles:
        traversing = []#Dummy opened to get the words. Tried without it and ran forever
        for everyline in readingFiles:
            for everyword in everyline.split(' '):#Splitting file words
                traversing.append(everyword)#Store words by traversing
        filestorage.append(traversing) #Store words in a list
    return filestorage#Return words

def main():
#hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest
    wordList = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet",
                "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]

    readNew = []#Empty list to traverse by each file
    for i in range(1, 9):#Range of 1 to 9 since we have 8 files
        n = str(i)#Transform into string in order to be able to read files correctly
        file = readNew.append(open('shakespeare'+n+'.txt','r'))#Read file by file
    fileTime = time.monotonic()#Initialized time to count while going through files
    fileList = appendFiles(readNew)#Store list of files read
    fileTimeEnd = time.monotonic()#End of time
    finalTimeFile = fileTimeEnd - fileTime#Time it took to store the list of files into new list
    wordsTime = time.monotonic()#Initialized time to count words
    reducingProcess = mapReduce(fileList, wordList)#called function to map words
    wordsEnd = time.monotonic()#end of time
    wordCountFinalTime = wordsEnd - wordsTime#
    print(reducingProcess)
    print("Time took to count words: " + str(wordCountFinalTime)+ " secs.")
    print("Time took to read files: " + str(finalTimeFile)+ " secs.")

if __name__ == '__main__':
    main()
