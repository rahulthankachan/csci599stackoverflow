__author__ = 'Rahul Thankachan'

from datetime import datetime
import time
import os

popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")


def get_attribute1():
    attr_str = 'javascript, java, c#, php, python, html, c++, sql, objective-c, c'
    return '{' + attr_str + '}'


def get_attribute3():
    attr_str = 'month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12'
    return '{' + attr_str + '}'

# name of the Relation
relation_name = 'stackoverflow'

# for testing only
if os.path.exists('Output/' + relation_name + '.arff' ):
    os.remove('Output/' + relation_name + '.arff')


weka_f = open("Output/" + relation_name + '.arff', 'a')


weka_f.write('@relation ' + relation_name)
weka_f.write('\n\n')


# ORDER # qid / Question Tags / delta_answer / creation month / bodylength / taglength/

attribute1_name = 'tag'
attribute2_name = 'delta_ans'
attribute3_name = 'creation_month'
attribute4_name = 'body_length'
attribute5_name = 'tag_length'

attribute6_name = 'time_answer'


attribute1 = 'real'
attribute2 = 'real'
attribute3 = 'real'
attribute4 = 'real'
attribute5 = 'real'
attribute6 = 'real'

# generate the non real ones here
attribute1 = get_attribute1()
attribute3 = get_attribute3()
# attribute6 = '{slowest, slow, neutral, fast, fastest}'
attribute6 = '{less6, bet6and20, 20andmore }'

weka_f.write('@attribute ' + attribute1_name + ' ' + attribute1 + '\n')
weka_f.write('@attribute ' + attribute2_name + ' ' + attribute2 + '\n')
weka_f.write('@attribute ' + attribute3_name + ' ' + attribute3 + '\n')
weka_f.write('@attribute ' + attribute4_name + ' ' + attribute4 + '\n')
weka_f.write('@attribute ' + attribute5_name + ' ' + attribute5 + '\n')
weka_f.write('@attribute ' + attribute6_name + ' ' + attribute6 + '\n')



weka_f.write('\n\n')
weka_f.write('@data\n')

# data file reader
# ORDER # 0 qid / 1 Question Tags / 2 delta_answer / 3 creation month / 4 bodylength / 5 taglength/    6---- decision
flag = 1
count = 449000
total_count = 0
counter = 0

# myfile = open('Resources/weka/Map_Questions_Weka_top.txt', 'a')
with open('Resources/weka/Map_Questions_Weka_top.txt') as data_file:
    for line in data_file:
        if total_count % 10 == 0 and counter < count:
            counter += 1
            elements = line.split(' ')
            tags = elements[1].split('||')
            for tag in tags:
                if tag in popular_languages:

                    delta_answer = elements[2]
                    time_answer = ''

                    if float(delta_answer) < 6 * 60:
                        time_answer = 'less6'
                    elif float(delta_answer) < 20 * 60:
                        time_answer = 'bet6and20'
                    else:
                        time_answer = '20andmore'

                    data_str = tag + ' ' + str(delta_answer) + ' ' + str(elements[3]) + ' ' + str(elements[4]) + ' ' +\
                               str(elements[5][:-1]) + ' ' + time_answer
                    weka_f.write(data_str + '\n')
                    break
        total_count += 1



# with open('Resources/weka/Map_Questions_Weka.txt') as data_file:
#     for line in data_file:
#             total_count +=1
#             elements = line.split(' ')
#             tags = elements[1].split('||')
#             for tag in tags:
#
#                 if tag in popular_languages:
#
#                     count += 1
#                     myfile.write(line)
#                     # delta_answer = elements[2]
#                     # time_answer = ''
#                     #
#                     # # if float(delta_answer) < 4 * 60:
#                     # #     time_answer = 'fastest'
#                     # # elif float(delta_answer) < 11 * 60:
#                     # #     time_answer = 'fast'
#                     # # elif float(delta_answer) < 1 * 60 * 60:
#                     # #     time_answer = 'neutral'
#                     # # elif float(delta_answer) < 3 * 60 * 60:
#                     # #     time_answer = 'slow'
#                     # # else:
#                     # #     time_answer = 'slowest'
#                     #
#                     # if float(delta_answer) < 5 * 60:
#                     #     time_answer = 'fast'
#                     # elif float(delta_answer) < 15 * 60:
#                     #     time_answer = 'Neutral'
#                     # else:
#                     #     time_answer = 'slow'
#                     #
#                     #
#                     #
#                     # data_str = tag + ' ' + str(delta_answer) + ' ' + str(elements[3]) + ' ' + str(elements[4]) + ' ' +\
#                     #            str(elements[5][:-1]) + ' ' + time_answer
#                     # weka_f.write(data_str + '\n')
#                     # count -= 1
#                     # if count < 0:
#                     #     flag = 0
#                     #     break
#
#         # if flag == 0 or count1 >= 986136:
#         #     break
print(count)
print(total_count)
print(counter)




































