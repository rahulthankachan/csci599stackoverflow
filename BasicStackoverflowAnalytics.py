import xml.etree.ElementTree as XMLParser


def create_TagList_ProgrammingLanguage():
    TagsCountDictionary = dict()
    for event, elem in XMLParser.iterparse('Resources\Posts.xml'):
        tags = elem.get('Tags')
        if tags:
            tags = tags.replace('<',' ')
            tags = tags.replace('>',' ')
            tags = tags.split()
            for item in tags:
                if item in TagsCountDictionary.keys():
                    TagsCountDictionary[item] = TagsCountDictionary[item] + 1
                else:
                    TagsCountDictionary[item] = 1

        elem.clear()

    TagsCountDictionary_sorted_list = sorted(TagsCountDictionary.items(), key=lambda x:x[1],reverse=True)

    fp = open('Output/TagsCountDictionary_sorted_list.txt','w')
    fp.write(str(TagsCountDictionary_sorted_list))
    fp.close()

    return TagsCountDictionary_sorted_list

def Calculate_TopTenProgrammingLanguages():

    fp = open('Output/TagsCountDictionary_sorted_list.txt','r')
    TagsCountDictionary_sorted_list = eval(fp.read())
    fp.close()

    fp = open('Output/ListProgrammingLanguagesFinal2.txt','r')
    ProgrammingLanguages_list = eval(fp.read())
    fp.close()

    count = 0
    TopTenLanguagesDict = dict()
    TopTenLanguagesNumberOfQuestionsDict = dict()

    for item in TagsCountDictionary_sorted_list:

        if item[0] in ProgrammingLanguages_list:
            TopTenLanguagesDict[item[0]] = item[1]
            TopTenLanguagesNumberOfQuestionsDict[item[0]] = 0
            count=count+1

        if count==10:
            break

    TopTenProgrammingLanguages_sorted_list = sorted(TopTenLanguagesDict.items(), key=lambda x:x[1],reverse=True)

    fp = open('Output/TopTenProgrammingLanguages_sorted_list.txt','w')
    fp.write(str(TopTenProgrammingLanguages_sorted_list))
    fp.close()

    return TopTenProgrammingLanguages_sorted_list

def Calculate_Questions_Post_List():

    fp = open('Output/ListProgrammingLanguagesFinal2.txt','r')
    ProgrammingLanguages_list = eval(fp.read())
    fp.close()

    fp = open('Output/Questions_Post_Dictionary.txt','w')
    for event, elem in XMLParser.iterparse('Resources\Posts.xml'):
        if elem.get('PostTypeId') == "1":
            templist = list()
            tags = elem.get('Tags')
            if tags:
                tags = tags.replace('<',' ')
                tags = tags.replace('>',' ')
                tags = tags.split()
                tags1 = list()
                for item1 in tags:
                    if item1 in ProgrammingLanguages_list:
                        tags1.append(item1)
                templist.append(tags1)
                templist.append(elem.get('OwnerUserId'))
                templist.append(elem.get('Id'))
                fp.write(str(templist)+"\n")

        elem.clear()

    fp.close()

def Calculate_Questioner_Per_Language_List():

    fp = open('Output/TopTenProgrammingLanguages_sorted_list.txt','r')
    ProgrammingLanguages_list = eval(fp.read())
    fp.close()

    Data_Per_Language = dict()

    for item in ProgrammingLanguages_list:
        Number_of_questions = 0
        Data_Per_Language[item[0]] = dict()
        fp = open('Resources/Questions/' + item[0] +'.txt','r')
        tempQuestionerList = list()
        for line in fp:
            tempDict= eval(line.rstrip('\n'))
            if tempDict['OwnerUserId']:
                if int(tempDict['OwnerUserId']) not in tempQuestionerList:
                    tempQuestionerList.append(int(tempDict['OwnerUserId']))

            Number_of_questions = Number_of_questions + 1

        Data_Per_Language[item[0]]["QuestionsCount"] = Number_of_questions
        Data_Per_Language[item[0]]["QuestionerCount"] = len(tempQuestionerList)
        # Data_Per_Language[item[0]]["QuestionerList"] = tempQuestionerList
        fp.close()

    print(Data_Per_Language)


def Calculate_Answerer_Per_Language_List():

    fp = open('Output/TopTenProgrammingLanguages_sorted_list.txt','r')
    fo = open('Output/Question1_Answers.txt', 'w');
    ProgrammingLanguages_list = eval(fp.read())
    fp.close()

    Data_Per_Language = dict()

    for item in ProgrammingLanguages_list:
        Number_of_Answers = 0
        Data_Per_Language[item[0]] = dict()
        fp = open('Resources/Answers/' + 'ans_' + item[0] +'.txt','r')
        tempAnswererList = list()
        for line in fp:
            tempDict= eval(line.rstrip('\n'))
            if tempDict['OwnerUserId']:
                if int(tempDict['OwnerUserId']) not in tempAnswererList:
                    tempAnswererList.append(int(tempDict['OwnerUserId']))

            Number_of_Answers += 1

        Data_Per_Language[item[0]]["AnswersCount"] = Number_of_Answers
        Data_Per_Language[item[0]]["AnswerersCount"] = len(tempAnswererList)
        # Data_Per_Language[item[0]]["QuestionerList"] = tempQuestionerList

    print("Done")
    fo.write(str(Data_Per_Language))
    fo.close()
    fp.close()

# Calculate_Questioner_Per_Language_List()
Calculate_Answerer_Per_Language_List()





