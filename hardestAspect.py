# CSCI599 - Social Media Analytics
# Fall 2015
# Class Project - What StackOverflow Tells about Programming Languages
# Nada Aldarrab		naldarra@usc.edu
# -------------------------------------------
# To run this program, run this command: python3 hardestAspect.py
# Follow the directory structure of the GIT repository
# -------------------------------------------


from datetime import datetime
import statistics


# Compute the trend of the language based on the post count
# @args: an input file containing post data, formatted as a dictionary for each post per line
# Return a list of post counts per month over the years 08 to 15
def countTrend(ipfile):
    trend = [0 for i in range(0,8*12)]
    with open(ipfile,"r") as ipfile:
        for line in ipfile:
            postDate = datetime.strptime(eval(line)['CreationDate'], "%Y-%m-%dT%H:%M:%S.%f")
            index = ((int(str(postDate.year)[2:])-8)*12) + (postDate.month-1)
            trend[index] += 1
    return trend

# Compute the trend of the language based on the fraction of the posts
# @args: a dictionary of trend counts: {language:count_list}
# Return a dictionary of trend fractions: {language:fraction_list}
def fractionTrend(questionTrends):
    trendSum = [sum([questionTrends[l][i] for l in questionTrends]) for i in range(0,8*12)]
    for l in questionTrends:
        questionTrends[l] = [questionTrends[l][i]/trendSum[i] if trendSum[i]!=0 else 0 for i in range(0,8*12)]
    return questionTrends


if __name__ == '__main__':
    popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")
    # Keep a dictionary of trends
    questionTrends = dict()
    # Count Trends
    for lang in popular_languages:
        with open("Output/Trends/QuestionCount.txt", "a") as opfile:
            trend = countTrend("Resources/Questions/"+lang+".txt")
            opfile.write(lang+' '+str(trend)+'\n')
            questionTrends.update({lang:trend})

    # Fraction Trends
    questionTrends = fractionTrend(questionTrends)
    with open("Output/Trends/QuestionFractions.txt", "a") as opfile:
        for lang in questionTrends:
            opfile.write(lang+' '+str(questionTrends[lang])+'\n')
