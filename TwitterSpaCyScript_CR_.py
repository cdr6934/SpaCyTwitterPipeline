# Import the necessary methods from tweepy library

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import spacy

nlp = spacy.load('en_core_web_sm')
consumer_key = "QDrsiY9CHd5MgWxTtJB7BUJ9K"
consumer_secret = "dnllP0FFBlbFGdV29h6dJH4Ov9q3Nr3EOFuyaikvEstPlKoLk1"
access_token = "6627802-UMhQ6mesD8pDiCMUVDGXsk3hO3ct03KXtVPpMT7lSP"
access_token_secret = "NayOyGdPmHzfMceVDD5ZoXlk500DoNXRQT4tG3QuTpCj0"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        parsed_json = json.loads(data)
        doc = nlp(parsed_json['text'])
        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)

        #print(parsed_json['text'])
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])