from asyncore import read
import csv
from collections import Counter
from collections import defaultdict
import string

#import matplotlib.pyplot as plt
#from wordcloud import WordCloud

words = []

with open('data/test.csv', 'rt') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for col in reader:
        csv_words = col[1].split()
        
        for i in csv_words:
            out = i.translate(string.punctuation)
            words.append(out)

with open('data/AfricansinPoland.csv', 'rt') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for col in reader:
        csv_words = col[1].split()
        
        for i in csv_words:
            out = i.translate( string.punctuation)
            words.append(out)

with open('data/SaveSumyStudents.csv', 'rt') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for col in reader:
        csv_words = col[1].split()
        
        for i in csv_words:
            out = i.translate(string.punctuation)
            words.append(out)
#print(words)

f = open("data/frequency_results.csv", "w")
f.truncate()
f.close()
words_counted=[]

with open('data/frequency_results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for i in words:
        if i == 'RT' or '@' in i or  '-' in i or ':' in i or '...' in i:
            continue
        else:
            x=words.count(i)
            if (i,x) in words_counted:
                continue
            else:
                i = i.lower()
                words_counted.append((i,x))
    set(words_counted)
    writer.writerow(["Words", "Frequency"])
    writer.writerows(words_counted)

#wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(words_counted)

#plt.figure(figsize=(15,8))
#plt.imshow(wordcloud)