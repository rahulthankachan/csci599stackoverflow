import xml.etree.ElementTree as XMLParser


def create_TagList_ProgrammingLanguage():
    TagsCountDictionary = dict()
    for event, elem in XMLParser.iterparse('resourses\stackoverflow\stackoverflow.com-Posts\Posts.xml'):
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
    for event, elem in XMLParser.iterparse('resourses\stackoverflow\stackoverflow.com-Posts\Posts.xml'):
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

def Calculate_Questionaries_Per_Language_List():

    Questionaries_Per_Language = dict()
    Number_Of_Questionaries_Per_Language = dict()
    fp = open('Output/Questions_Post_Dictionary.txt','r')

    for line in fp:
        tempList = eval(line.rstrip('\n'))
        if len(tempList[0])>0:
            for item in tempList[0]:
                if item in Questionaries_Per_Language.keys():
                    if(tempList[1] not in Questionaries_Per_Language[item]):
                        Questionaries_Per_Language[item].append(tempList[1])
                else:
                    Questionaries_Per_Language[item] = list()
                    Questionaries_Per_Language[item].append(tempList[1])

    fp.close()

    fp = open('Output/Questionaries_Per_Language_Dict.txt','w')
    fp.write(str(Questionaries_Per_Language))
    fp.close()

    for item in Questionaries_Per_Language.keys():
        Number_Of_Questionaries_Per_Language[item] = len(Questionaries_Per_Language[item])

    return Number_Of_Questionaries_Per_Language


# print("Top Ten Programming languages::")
# print(Calculate_Questionaries_Per_Language_List())

# QuestionCount = 0
# AnswerCount = 0
# TotalPosts=0
#
# for event, elem in XMLParser.iterparse('resourses\stackoverflow\stackoverflow.com-Posts\Posts.xml'):
#     if elem.get('PostTypeId') == "1":
#         QuestionCount = QuestionCount +1
#     if elem.get('PostTypeId') == "2":
#         AnswerCount = AnswerCount +1
#
#     TotalPosts = TotalPosts + 1
#     elem.clear()
#
# print("Question Count::"+str(QuestionCount))
# print("Answer Count::"+str(AnswerCount))
# print("Total Posts::"+str(TotalPosts))

fp = open('Output/TagsCountDictionary_sorted_list.txt','r')
TagsCountDictionary_sorted_list = eval(fp.read())
fp.close()

Tags =list()

for item in TagsCountDictionary_sorted_list:
    Tags.append(item[0])

fp = open('Output/ListProgrammingLanguagesFinal2.txt','r')
PL_list = eval(fp.read())
fp.close()

IntersectionList = set(PL_list) & set (Tags)
print(IntersectionList)
print("Intersection::"+str(len(PL_list)))
# fp = open('Output/TopTenLanguagesNumberOfQuestionsDict.txt','w')
# fp.write(str(TopTenLanguagesNumberOfQuestionsDict))
# fp.close()




