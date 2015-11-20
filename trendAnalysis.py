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

# Keep min and max dates
#minDate = '9999'
#maxDate = '0000'


# Compute the trend of the language based on the post count
# Return a dictionary: {'YYMM': count}
def countTrend(ipfile):
    #global minDate
    #global maxDate
    trend = dict()
    with open(ipfile,"r") as ipfile:
        for line in ipfile:
            postDate = datetime.strptime(eval(line)[4], "%Y-%m-%dT%H:%M:%S.%f")
            key = str(postDate.year)[2:]+'{:02d}'.format(postDate.month)
            trend[key] = trend.get(key,0)+1
            #if key < minDate: minDate=key
            #if key > maxDate: maxDate=key
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

#    print("minDate= " + minDate)
#    print("maxDate= " + maxDate)
