# CSCI599 - Social Media Analytics
# Fall 2015
# Class Project - What StackOverflow Tells about Programming Languages
# Nada Aldarrab		naldarra@usc.edu
# -------------------------------------------
# To run this program, run this command: python3 trendAnalysis.py
# Follow the directory structure of the GIT repository
# -------------------------------------------


popular_languages = {"javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c"}
lis = dict()
tags= '<c++><c><sockets><mainframe><zos>'
tags = tags.replace("<", " ")
tags = tags.replace(">", " ")
tags = tags[1:-1]
mdict = tags.split(" ")
print(len(mdict))
tags= '<c++><c++><c++><c><c><sockets><mainframe><zos>'
tags = tags.replace("<", "").replace(">", " ")[:-1].split()
print(len(tags))
#tags = tags[1:-1]
for key in tags:
    lis[key] = lis.get(key,0)+1

lis = sorted(lis.items(), key=lambda x:-x[1])
print(lis[:2])
print(str(lis))
'''
print(s.replace('<',' ').replace('>',' '))
l = "java "
if l in popular_languages:
    print(l)


questionTrends={'java':[0,2,3],'c':[0,5,6]}
trendSum = [sum([questionTrends[l][i] for l in questionTrends]) for i in range(0,3)]
for l in questionTrends:
    questionTrends[l] = [questionTrends[l][i]/trendSum[i] if trendSum[i]!=0 else 0 for i in range(0,3)]

print(questionTrends)

#allTrends[l] = [([allTrends[l][i]/trendSum[i] for l in allTrends]) for i in range(0,3)]


#print(allTrends.items())
#####
###
'''