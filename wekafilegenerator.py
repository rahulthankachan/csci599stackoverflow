__author__ = 'Rahul Thankachan'

from datetime import datetime
import time
import os


def get_attribute1():
    attr_str = 'javascript, java, c#, php, python, html, c++, sql, objective-c, c'
    return '{' + attr_str + '}'


def get_attribute3():
    attr_str = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12'
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
attribute6 = '{slowest, slow, neutral, fast, fastest}'

weka_f.write('@attribute ' + attribute1_name + ' ' + attribute1 + '\n')
weka_f.write('@attribute ' + attribute2_name + ' ' + attribute2 + '\n')
weka_f.write('@attribute ' + attribute3_name + ' ' + attribute3 + '\n')
weka_f.write('@attribute ' + attribute4_name + ' ' + attribute4 + '\n')
weka_f.write('@attribute ' + attribute5_name + ' ' + attribute5 + '\n')
weka_f.write('@attribute ' + attribute6_name + ' ' + attribute6 + '\n')



weka_f.write('\n\n')
weka_f.write('@data\n')

#data file reader



























