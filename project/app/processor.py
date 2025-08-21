import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import fetcher


nltk.download('vader_lexicon')

class TextProcessor:
    def __init__(self, data):
        self.procesdb = []
        self.df = pd.DataFrame(data)

    def rare_word(self):
        # found the rarest word in each text
        rare_words = []
        for text in self.df['Text']:
            words = text.lower().split()
            counts = Counter(words)
            rare_word = min(counts, key=counts.get) if counts else None
            rare_words.append(rare_word)
        return rare_words

    def sentiment(self):
        # Perform sentiment analysis on each text
        sentiments = []
        for text in self.df['Text']:
            score=SentimentIntensityAnalyzer().polarity_scores(text)
            compound = score['compound']
            if compound >= 0.05:
                sentiment = 'positive'
            elif compound <= -0.05:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            sentiments.append(sentiment)
        return sentiments

    def weapon_detection(self, blacklist_file):
        # Detect weapons in the text based on a blacklist
        with open(blacklist_file, 'r') as f:
            blacklist = [line.strip() for line in f.readlines()]

        weapons = []
        for text in self.df['Text']:
            found_weapon = None
            text_lower = text.lower()

            for weapon in blacklist:
                if weapon.lower() in text_lower:
                    found_weapon = weapon
                    break
            weapons.append(found_weapon )
        return weapons

    def get_df(self):
        # Process the DataFrame and return the processed items

        rare_words = self.rare_word()
        sentiments = self.sentiment()
        weapons = self.weapon_detection("C:/pycharm/hostile-tweets-ex/project/data/weapons.txt")

        for i in range(len(self.df)):
            processed_item = {
                "id": str(self.df.iloc[i]['_id']),
                "original_text": self.df.iloc[i]['Text'],
                "rarest_word": rare_words[i],
                "sentiment": sentiments[i],
                "weapons_detected": weapons[i] if weapons[i] else None}
            self.procesdb.append(processed_item)
        return self.procesdb


mongodb = fetcher.Connection()
tweets = mongodb.get_data_frame()
processor = TextProcessor(tweets)
result = processor.get_df()
for item in result:
    print(item)
    print("-------------------------")
