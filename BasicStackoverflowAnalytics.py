import xml.etree.ElementTree as XMLParser

TagsCountDictionary = dict()

for event, elem in XMLParser.iterparse('stackoverflow\stackoverflow.com-Posts\Posts.xml'):
    tags = elem.get('Tags')
    if tags:
        tags = tags.replace('<',' ')
        tags = tags.replace('>',' ')
        tags = tags.split()
        for item in tags:
            if item in TagsCountDictionary.keys():
                TagsCountDictionary[item] = TagsCountDictionary[item] + 1
            else:
                TagsCountDictionary[item] = 1

    elem.clear()


TagsCountDictionary_sorted_list = sorted(TagsCountDictionary.items(), key=lambda x:x[1],reverse=True)
fp = open('TagsCountDictionary_sorted_list.txt','w')
fp.write(str(TagsCountDictionary_sorted_list))

count = 0
TopTenLanguagesDict = dict()
for item in TagsCountDictionary_sorted_list:
    count=count+1
    TopTenLanguagesDict[item[0]] = item[1]
    if count==10:
        break

print("Top Ten Programming languages::")
print(TopTenLanguagesDict)






