# CSCI599 - Social Media Analytics
# Fall 2015
# Class Project - What StackOverflow Tells about Programming Languages
# Nada Aldarrab		naldarra@usc.edu
# -------------------------------------------
# To run this program, run this command: python3 popularTopics.py
# Follow the directory structure of the GIT repository
# -------------------------------------------


# Compute the popular topics of a language based on the tag count
# @args: an input file containing post data, formatted as a dictionary for each post per line
# Return a dictionary of {tag:count} for the programming language
def countTags(ipfile):
    tags = dict()
    with open(ipfile,"r") as ipfile:
        for line in ipfile:
            tagList = eval(line)['Tags'].replace("<", "").replace(">", " ")[:-1].split()
            for tag in tagList:
                tags[tag] = tags.get(tag,0)+1
    return tags


if __name__ == '__main__':
    popular_languages = ("javascript", "java", "c#", "php", "python", "html", "c++", "sql", "objective-c", "c")
    # Count Tags
    for lang in popular_languages:
        with open("Output/PopularTopics.txt", "a") as opfile:
            tags = countTags("Resources/Questions/"+lang+".txt")
            # Sort the tag list in descending order of counts
            tags = sorted(tags.items(), key=lambda x:-x[1])
            opfile.write(lang+' '+str(tags[:30])+'\n')
