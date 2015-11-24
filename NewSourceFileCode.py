import xml.etree.ElementTree as XMLParser
import json

popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")

# This function is used to create proper Questions data file


def create_subset_files():
    count = 0
    for event, elem in XMLParser.iterparse('Resources/Posts.xml'):
        tags = elem.get('Tags')
        if tags:
            tags = tags.replace("<", " ")
            tags = tags.replace(">", " ")
            tags = tags[1:-1]
            mdict = tags.split(" ")
            for key in mdict:
                if key in popular_languages:
                    dict_tuple_post = {"Id": elem.get("Id"),
                                       "PostTypeId": elem.get("PostTypeId"),
                                       "AcceptedAnswerId": elem.get('AcceptedAnswerId'),
                                       "ParentId": elem.get("ParentId"),
                                       "CreationDate": elem.get('CreationDate'),
                                       "Score": elem.get('Score'),
                                       "ViewCount": elem.get('ViewCount'),
                                       "Body": elem.get('Body'),
                                       "OwnerUserId":elem.get('OwnerUserId'),
                                       "OwnerDisplayName": elem.get('OwnerDisplayName'),
                                       "LastEditDate": elem.get('LastEditDate'),
                                       "LastActivityDate": elem.get('LastActivityDate'),
                                       "Title": elem.get('Title'),
                                       "Tags": elem.get('Tags'),
                                       "AnswerCount": elem.get('AnswerCount'),
                                       "CommentCount": elem.get('CommentCount'),
                                       "PGLanguage": key}

                    language = key
                    filel = open("Resources/Questions/"+language+".txt", "a")
                    filel.write(str(dict_tuple_post)+"\n")
                    filel.close()
                    tuple_all_questions = [dict_tuple_post["Id"], key]
                    fileq = open("Resources/Questions/"+"allquestions.txt", "a")
                    fileq.write(str(tuple_all_questions)+"\n")
                    fileq.close()
                    break
        # count += 1
        # if count > 20:
        #     break
    print("Done")

# This function is used to read all the question id and associated tags into memory
def read_all_question():

    questions = {}
    file_name = "allquestions.txt"
    count = 0
    with open("Resources/Questions/"+file_name, "r") as allQuestion:
        for line in allQuestion:
            ques = eval(line)
            #print(questions)
            questions[int(ques[0])] = ques[1]
            count += 1
            # if count > 10:
            #     break
    return questions


def create_subset_files_ans():

    # fileq.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    # fileq.write("\n<questions>")
    myQuestions = read_all_question()
    print(myQuestions[16])

    count = 0
    for event, elem in XMLParser.iterparse('Resources/Posts.xml'):
        if elem.get('PostTypeId') == '2' and elem.get("ParentId") != "None":
            if int(elem.get("ParentId")) in myQuestions:  # check if its in top prog lang ques
                key = myQuestions[int(elem.get("ParentId"))]
                dict_tuple_post = {"Id": elem.get("Id"),
                                       "PostTypeId": elem.get("PostTypeId"),
                                       "AcceptedAnswerId": elem.get('AcceptedAnswerId'),
                                       "ParentId": elem.get("ParentId"),
                                       "CreationDate": elem.get('CreationDate'),
                                       "Score": elem.get('Score'),
                                       "ViewCount": elem.get('ViewCount'),
                                       "Body": elem.get('Body'),
                                       "OwnerUserId":elem.get('OwnerUserId'),
                                       "OwnerDisplayName": elem.get('OwnerDisplayName'),
                                       "LastEditDate": elem.get('LastEditDate'),
                                       "LastActivityDate": elem.get('LastActivityDate'),
                                       "Title": elem.get('Title'),
                                       "Tags": elem.get('Tags'),
                                       "AnswerCount": elem.get('AnswerCount'),
                                       "CommentCount": elem.get('CommentCount'),
                                       "PGLanguage": key}

                language = key
                filel = open("Resources/Answers/"+"ans_"+language+".txt", "a")
                filel.write(str(dict_tuple_post)+"\n")
                filel.close()

                tuple_all_questions = [dict_tuple_post["Id"], key]
                fileq = open("Resources/Answers/"+"allanswers.txt", "a")
                fileq.write(str(tuple_all_questions)+"\n")
                fileq.close()

        # count += 1
        # if count > 20:
        #     break

    print("Done")


########### Implementation #############

# create_subset_files()
#create_subset_files_ans()
# count = 0
# with open("Resources/Posts.xml") as f:
#     for line in f:
#         count += 1
# print(count)