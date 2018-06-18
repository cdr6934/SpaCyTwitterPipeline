# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import CRUD.DatabaseOperations as do
import CRUD.FileOperations as fo
import json
import spacy
import keys

#Need to be checked to ensure there are certain
nlp = spacy.load('en_core_web_sm')

auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    """
    Generates the standard out listener
    ----------
    StreamListener : DataFrame object
        ts Series object

    """
    def on_data(self, data):
        """
        Generates SpaCy Analysis and outputs the data into the format
        Parameters
        ----------
        self : DataFrame object
            upon itself

        data : string
            Twitter JSON feed
        """
        parsed_json = json.loads(data)

        fo.WriteToFile(data, "data/workfile")
        do.WriteToDatabase(data)

        doc = nlp(parsed_json['text'])
        # Find named entities, phrases and concepts
        #for entity in doc.ents:
        #    print(entity.text, entity.label_)

        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)

        #print(parsed_json['text'])
        return True

    def on_error(self, status):
        print(status)




if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])