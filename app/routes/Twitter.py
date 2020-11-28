import uuid
from app import app, db
import requests
import json
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from tweepy import OAuthHandler
import tweepy
import spacy
from ..models.tweet import Tweet, TweetSchema

nlp = spacy.load('es_core_news_sm')

consumer_key = '[KEY_PROPIA]'
consumer_secret = '[SECRET_PROPIO]'
access_token = '[TOKEN_PROPIO]'
token_secret = '[TOKEN_SECRET_PROPIO]'


def newTweet(data):
    return {
        'created_at': data["created_at"],
        'id': data["id"],
        'text': data['text'],
        'entities': {
            'hashtags': data["entities"]["hashtags"],
            'user_mentions': data["entities"]["user_mentions"],
            'urls': data["entities"]["urls"]
        },
        'user': {
            'created_at': data["user"]["created_at"],
            'id': data["user"]["id"],
            'name': data["user"]["name"],
            'location': data["user"]["location"],
            'followers_count': data["user"]["followers_count"]
        },
        'coordinates': data["coordinates"],
        'place': data["place"],
        'retweet_count': data["retweet_count"],
        'favorite_count': data["favorite_count"],
        'lang': data["lang"]
    }


cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/twitter/get-tweets', methods=['POST'])
def getTweets():
    if not request.json:
        return jsonify({"Message": "Nothing came"}), 400
    if not 'latitude' in request.json:
        return jsonify({"Message": "latitude is needed"}), 400
    if not 'longitude' in request.json:
        return jsonify({"Message": "longitude is needed"}), 400
    if not 'query' in request.json:
        return jsonify({"Message": "query is needed"}), 400
    latitude = request.get_json()['latitude']
    longitude = request.get_json()['longitude']
    query = request.get_json()['query']
    coordinates = str(latitude)+','+str(longitude)+',200km'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    new_tweets = api.search(q=query, geocode=coordinates, count=100)

    tweetData = new_tweets["statuses"]
    if(len(tweetData) > 1):

        tweetsInfo = []

        for tweet in tweetData:
            tweetsInfo.append(newTweet(tweet))

        tweetsObject = []

        for tweet in tweetsInfo:
            doc = nlp(tweet['text'])
            words = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
            lexical_tokens = [t.lower()
                              for t in words if len(t) > 3 and t.isalpha()]
            lemmas = [tok.lemma_.lower() for tok in doc]

            existingTweet = Tweet(
                Id=str(uuid.uuid4()),
                TweetInfo=tweet,
                TweetTokenization=lexical_tokens,
                TweetLemma=lemmas
            )

            db.session.add(existingTweet)
            db.session.commit()
            responseTweet = {
                'id': existingTweet.Id,
                'TweetInfo': tweet,
                'TweetTokenization': lexical_tokens,
                'TweetLemma': lemmas
            }
            tweetsObject.append(responseTweet)

    print(new_tweets)
    return jsonify({'data': tweetsObject})
