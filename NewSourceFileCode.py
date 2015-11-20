import xml.etree.ElementTree as XMLParser
import json

popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")

# This function is used to create proper Questions data file
def create_subset_files():

    # fileq.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    # fileq.write("\n<questions>")

    count = 0
    for event, elem in XMLParser.iterparse('Resources/Posts.xml'):
        tags = elem.get('Tags')
        if tags:
            tags = tags.replace("<", " ")
            tags = tags.replace(">", " ")
            tags = tags[1:-1]
            mdict = tags.split(" ")
            #print(mdict)
            for key in mdict:
                if key in popular_languages:
                    tuple_post = [elem.get('Id'), elem.get('PostTypeId'),
                                      elem.get('AcceptedAnswerId'), elem.get('ParentId'),
                                      elem.get('CreationDate'), elem.get('Score'),
                                      elem.get('ViewCount'), elem.get('Body'),
                                      elem.get('OwnerUserId'), elem.get('OwnerDisplayName'),
                                      elem.get('LastEditDate'), elem.get('LastActivityDate'),
                                      elem.get('Title'), elem.get('Tags'),
                                      elem.get('AnswerCount'), elem.get('CommentCount'), key
                                    ]
                    language = key
                    filel = open("Resources/Questions/"+language+".txt", "a")
                    filel.write(str(tuple_post)+"\n")
                    filel.close()

                    tuple_all_questions = [tuple_post[0], key]

                    fileq = open("Resources/Questions/"+"allquestions.txt", "a")
                    fileq.write(str(tuple_all_questions)+"\n")
                    fileq.close()
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

# This function is used to create proper Answers data file
def create_subset_files_ans():

    # fileq.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    # fileq.write("\n<questions>")
    myQuestions = read_all_question()
    print(myQuestions[16])

    count = 0
    for event, elem in XMLParser.iterparse('Resources/Posts.xml'):
        if elem.get('PostTypeId') == '2' and elem.get("ParentId") != "None":
            if int(elem.get("ParentId")) in myQuestions:  # check if its in top prog lang ques
                pl = myQuestions[int(elem.get("ParentId"))]
                tuple_post = [elem.get('Id'), elem.get('PostTypeId'),
                                      elem.get('AcceptedAnswerId'), elem.get('ParentId'),
                                      elem.get('CreationDate'), elem.get('Score'),
                                      elem.get('ViewCount'), elem.get('Body'),
                                      elem.get('OwnerUserId'), elem.get('OwnerDisplayName'),
                                      elem.get('LastEditDate'), elem.get('LastActivityDate'),
                                      elem.get('Title'), elem.get('Tags'),
                                      elem.get('AnswerCount'), elem.get('CommentCount'), pl
                                    ]
                language = pl
                filel = open("Resources/Answers/"+"ans_"+language+".txt", "a")
                filel.write(str(tuple_post)+"\n")
                filel.close()

                tuple_all_questions = [tuple_post[0], pl]

                fileq = open("Resources/Answers/"+"allanswers.txt", "a")
                fileq.write(str(tuple_all_questions)+"\n")
                fileq.close()

    print("Done")

########################## EXECUTION ##########################

# create_subset_files_ans()
