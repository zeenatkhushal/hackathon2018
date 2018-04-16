f1 = open("Cleaned_tweets1_opoid_drugs.txt",'r')
writer = open("Cleaned1_tweets1_opoid_drugs.txt", 'a')
tweet = set()
index = 15
for row in f1:
    if row[6:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()