from flask import Flask, render_template, jsonify, redirect, request, url_for
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

import bs4 as bs
import urllib.request
import re

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/summarize-text-online")
def summarizer_page():
    return render_template("summarizer.html")


@app.route('/summarize', methods=['POST'])
def summarize_text():
    inp = request.form['textinp']
    print(request.form['percent'])
    print(type(request.form['percent']))
    no_of_words = int(request.form['percent'])
    print(no_of_words)

    #scraped_data = urllib.request.urlopen("https://en.wikipedia.org/wiki/Kerala")
    #article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(inp, 'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text += p.text
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'[[0-9]*]', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)

    # Convert text to sentences

    sentence_list = nltk.sent_tokenize(article_text)

    # Finding weighted frequencies of occurrence
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # To find the weighted frequency, divide the frequency of the word by the frequency of the most occurring word.
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    # Calculate sentence scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # Summary of the article
    import heapq
    summary_sentences = heapq.nlargest(
        no_of_words, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    print(summary)

    # return jsonify('', render_template("index.html", summary=summary, inp=inp))
    return render_template("summarizer.html", summary=summary, inp=inp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
