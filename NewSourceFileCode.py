import xml.etree.ElementTree as XMLParser
from datetime import datetime
import time
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


# This function will create a subset of all the answers which shall be used while making the Weka source file questions

def source_answers_timestamps():

    count = 1
    file1 = open("Resources/Map_Answers.txt", 'a')
    for event, elem in XMLParser.iterparse("Resources/Posts.xml"):
        if elem.get("PostTypeId") == '2':
            answer_dectionary = {}
            answer_dectionary['aid'] = elem.get('Id')
            answer_dectionary['qid'] = elem.get('ParentId')
            answer_dectionary['CDate'] = elem.get('CreationDate')

            if count > 10:
                break
            else:
                print(str(elem)+'\n')
            count += 1

            # file1.write(str(answer_dectionary) + '\n')
        elem.clear()

    print('Done')
    file1.close()




def source_answers_weka():


    questions = {}
    file_name = "Map_Answers2.txt"
    count = 0
    with open("Resources/"+file_name, "r") as allQuestion:
        for line in allQuestion:
            ques = {}
            ques = eval(line)
            if int(ques['qid']) in questions:
                # questions[int(ques[0])] = ques[1]
                stored_timestamp = questions[int(ques['qid'])]
                stored_date = datetime.strptime(stored_timestamp, "%Y-%m-%dT%H:%M:%S.%f")

                current_row_date = ques['CDate']
                stored_current_row_date = datetime.strptime(current_row_date, "%Y-%m-%dT%H:%M:%S.%f")

                # print('Clash')
                if stored_date > stored_current_row_date:
                    questions[int(ques['qid'])] = current_row_date

            else:
                questions[int(ques['qid'])] = ques['CDate']
    print("Questions Returned")
    return questions




def source_questions_timestamps_weka():

    count = 1

    ques_ans_map = source_answers_weka()


    file1 = open("Resources/Map_Questions.txt", 'a')
    for event, elem in XMLParser.iterparse("Resources/Posts.xml"):
        if elem.get("PostTypeId") == '1':

            ques = {}

            if int(elem.get('Id')) in ques_ans_map:
                stored_timestamp = ques_ans_map[int(elem.get('Id'))]
                stored_date = datetime.strptime(stored_timestamp, "%Y-%m-%dT%H:%M:%S.%f")

                current_row_date = elem.get('CreationDate')
                stored_current_row_date = datetime.strptime(current_row_date, "%Y-%m-%dT%H:%M:%S.%f")



                if stored_timestamp > current_row_date:

                    d1_ts = time.mktime(stored_date.timetuple())
                    d2_ts = time.mktime(stored_current_row_date.timetuple())
                    time_elapsed = d1_ts - d2_ts
                    ques['qid'] = elem.get('Id')
                    ques['time_elapsed'] = time_elapsed


                    ques['Tags'] = 'None'

                    tags = elem.get('Tags')
                    if tags:
                        tags = tags.replace("><", " ")
                        # tags = tags.replace(">", "")
                        tags = tags[1:-1]
                        mdict = tags.split(" ")
                        mdict.sort()

                        ques['Tags'] = mdict
                        ques['taglength'] = len(mdict)

                    ques['month_of_year'] = 'month' + str(stored_current_row_date.month)
                    ques['bodylength'] = len(elem.get('Body'))
                    print(str(ques))

                # qid / Question Tags / delta_answer / creation month / bodylength / taglength/

                    if count > 10:
                        break
                else:
                    print(elem.get('Tags'))

                count += 1

            #file1.write(str(answer_dectionary) + '\n')
        elem.clear()

    print('Done')
    file1.close()







########### Implementation #############

# create_subset_files()
#create_subset_files_ans()
# count = 0
# with open("Resources/Posts.xml") as f:
#     for line in f:
#         count += 1
# print(count)


#source_answers_timestamps()

# source_answers_weka()
source_questions_timestamps_weka()




