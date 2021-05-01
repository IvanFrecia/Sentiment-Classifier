TwitterData = open("project_twitter_data.csv","r")
ResultingData = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str_wrd):
    for chars in punctuation_chars:
        str_wrd = str_wrd.replace(chars, "")
    return str_wrd

def get_neg(str_s):
    str_sentance = strip_punctuation(str_s)
    str_lower = str_sentance.lower()
    string = str_lower.split()
    counter = 0
    for word in string:
        if word in negative_words:
            counter += 1
    return counter

def get_pos(str_s):
    str_sentance = strip_punctuation(str_s)
    str_lower = str_sentance.lower()
    string = str_lower.split()
    counter = 0
    for word in string:
        if word in positive_words:
            counter += 1
    return counter

def writeInDataFile(resultingDataFile):
    ResultingData.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    ResultingData.write("\n")

    linesPTDF =  TwitterData.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        ResultingData.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        ResultingData.write("\n")
        

writeInDataFile(ResultingData)
TwitterData.close()
ResultingData.close()