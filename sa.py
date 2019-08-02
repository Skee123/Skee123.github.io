from textblob import TextBlob
import matplotlib.pyplot as plt
import json

def read_file(filename):
    with open(filename, 'r') as f:
        responses_read = json.load(f)
    return responses_read

filename = "tweets_small.json"
twitter_data = read_file(filename) #twitter_data is a list of dictionaries

polarities = []
subjectivities =  []

for tweet in twitter_data:
        text = TextBlob(tweet["text"])
        polarities.append(text.sentiment.polarity)
        subjectivities.append (text.sentiment.subjectivity )

plt.hist(polarities)
plt.title("Polarities")
plt.xlabel("Polarity")
plt.ylabel("Density")
plt.show()
