import xml.etree.ElementTree as XMLParser


TagsCountDictionary = dict()


XMLTagsDoc = XMLParser.parse('stackoverflow\stackoverflow.com-Tags\Tags.xml').getroot()

TagsRows = XMLTagsDoc.findall('row')

for row in TagsRows:
    if row.get('TagName') == ".net":
        if "ASP.NET" in TagsCountDictionary.keys():
            TagsCountDictionary["ASP.NET"] = TagsCountDictionary["ASP.NET"] + int(row.get('Count'))
        else:
            TagsCountDictionary["ASP.NET"] = int(row.get('Count'))

    if row.get('TagName') == "asp.net":
        if "ASP.NET" in TagsCountDictionary.keys():
            TagsCountDictionary["ASP.NET"] = TagsCountDictionary["ASP.NET"] + int(row.get('Count'))
        else:
            TagsCountDictionary["asp.net"] = int(row.get('Count'))

    TagsCountDictionary[row.get('TagName')] = int(row.get('Count'))


TagsCountDictionary_sorted_list = sorted(TagsCountDictionary.items(), key=lambda x:x[1],reverse=True)
#print(TagsCountDictionary_sorted_list)

count = 1
for item in TagsCountDictionary_sorted_list:
    print(item)
    count = count + 1
    if count == 11:
        break


