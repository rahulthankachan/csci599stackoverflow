import xml.etree.ElementTree as XMLParser
import datetime
import json

def create_mapping_question_oldest_answer():
    f1 = open("Resources/Question_Oldest_Answer.txt", 'a')

    dictionary_mapping = {}

    for event, elem in XMLParser.iterparse("Resources/Posts.xml"):

        is_answer = elem.get("PostTypeId")
        if int(is_answer) == 1:
            parent_id = elem.get('ParentId')
            x = dictionary_mapping["hey"]
            print(x)
            if (x)
                datetime.timedelta()






