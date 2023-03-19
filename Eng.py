from textblob import TextBlob
with open("erlkingGT.txt", encoding="utf-8") as f:
    sentences = f.readlines()

total_polarity = 0

for sentence in sentences:
    blob = TextBlob(sentence.strip())
    sentiment = blob.sentiment
    print(blob)
    print(sentiment)
    total_polarity += sentiment.polarity

average_polarity = total_polarity / len(sentences)

print("Average polarity:", average_polarity)
