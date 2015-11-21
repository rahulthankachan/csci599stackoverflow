# CSCI599 - Social Media Analytics
# Fall 2015
# Class Project - What StackOverflow Tells about Programming Languages
# Nada Aldarrab		naldarra@usc.edu
# -------------------------------------------
# To run this program, run this command: python3 trendAnalysis.py
# Follow the directory structure of the GIT repository
# -------------------------------------------


from datetime import datetime
import statistics


# Compute the trend of the language based on the post count
# Return a list of post counts per month over the years 08 to 15
def countTrend(ipfile):
    trend = [0 for i in range(0,8*12)]
    with open(ipfile,"r") as ipfile:
        for line in ipfile:
            postDate = datetime.strptime(eval(line)['CreationDate'], "%Y-%m-%dT%H:%M:%S.%f")
            index = ((int(str(postDate.year)[2:])-8)*12) + (postDate.month-1)
            trend[index] += 1
    return trend


if __name__ == '__main__':
    popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")
    # Keep a dictionary of trends
    allTrends = dict()
    # Count Trends
    for lang in popular_languages:
        with open("Output/Trends/QuestionCount.txt", "a") as opfile:
            trend = countTrend("Resources/Questions/"+lang+".txt")
            opfile.write(lang+' '+str(trend)+'\n')
            allTrends.update({lang:trend})
