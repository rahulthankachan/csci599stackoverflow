# CSCI599 - Social Media Analytics
# Fall 2015
# Class Project - What StackOverflow Tells about Programming Languages
# Nada Aldarrab		naldarra@usc.edu
# -------------------------------------------
# To run this program, run this command: python3 trendAnalysis.py
# Follow the directory structure of the GIT repository
# -------------------------------------------


questionTrends={'java':[0,2,3],'c':[0,5,6]}
trendSum = [sum([questionTrends[l][i] for l in questionTrends]) for i in range(0,3)]
for l in questionTrends:
    questionTrends[l] = [questionTrends[l][i]/trendSum[i] if trendSum[i]!=0 else 0 for i in range(0,3)]

print(questionTrends)

#allTrends[l] = [([allTrends[l][i]/trendSum[i] for l in allTrends]) for i in range(0,3)]


#print(allTrends.items())
#####