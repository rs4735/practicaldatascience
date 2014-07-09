# Python Assignment: Etsy Ecommerce
# Group: Richard Saito, Thiago Teodoro, Grace Peng, Ajeshkumar Vijayadas 
# Data definition by column
# Assignment Reference https://github.com/jattenberg/PDS-Spring-2014/blob/master/homework/project.md
# API Key qg7ajp0cxlqjmubu9j2tfxr1

#declare variablesGET https://openapi.etsy.com/v2/listings/active?api_key={YOUR_API_KEY}
#https://openapi.etsy.com/v2/users/etsystore?api_key=your_api_key
#https://openapi.etsy.com/v2/private/shops?api_key=qg7ajp0cxlqjmubu9j2tfxr1

from urllib2 import Request, urlopen, URLError
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
import io
import json

#part 1 retrieve data via api
#Write a script which finds 5000 different shops on Etsy using the API (info below), and
# returns a sample of those shops listings. Store this shop/listing info in file in sensible structure using json format (info below).
request = Request('https://openapi.etsy.com/v2/private/shops?api_key=qg7ajp0cxlqjmubu9j2tfxr1')

try:
    response = urlopen(request)
    etsyjson = response.read()
    with io.open('/Users/richardsaito/Documents/Education/nyu/module 1/practical data science/data/etsydata.txt', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(etsyjson, ensure_ascii=False)))    
    #print etsystores[559:1000]
    #print etsystores
except URLError, e:
    print 'No Etsy Stores. Got an error code:', e

#part 2
# for each shop, return the five shops that are most similar. Output should be in the following format: shop_name: similar_shop_1, ...
# using cosine similarity http://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity/12128777#12128777
#print etsystores
#print etsystores['stop_name'] 

etsydata = json.load(etsyjson)
print etsydata["stop_name"] 

"""
stopWords = stopwords.words('english')

vectorizer = CountVectorizer(stop_words = stopWords)
print vectorizer
transformer = TfidfTransformer()
print transformer

trainVectorizerArray = vectorizer.fit_transform(etsystores).toarray()
#testVectorizerArray = vectorizer.transform(test_set).toarray()

#tfidf = vectorizer.fit_transform(etsystores)

#tfidf = TfidfVectorizer().fit_transform(etsystores)
#print tfidf.shape
#tfidf[0:1]

from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
cosine_similarities

related_docs_indices = cosine_similarities.argsort()[:-5:-1]
related_docs_indices

cosine_similarities[related_docs_indices]

#print twenty.data[0]
#print twenty.data[958]
"""