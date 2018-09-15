from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import pandas as pd
import numpy as np


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += ", ".join([feature_names[i]
                              for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()


class LDAModel:

    def __init__(self, training_samples, num_topics):

        clean_samples = training_samples # TODO: self.clean_docs(training_samples)

        self.vectorizer = CountVectorizer(ngram_range=(1, 2),
                                          max_df=0.95, min_df=2,
                                          max_features=1000,
                                          stop_words='english')

        tf = self.vectorizer.fit_transform(clean_samples)

        self.lda = LatentDirichletAllocation(n_components=num_topics, max_iter=5,
                                             learning_method='online',
                                             learning_offset=50.,
                                             random_state=0)
        self.lda.fit(tf)

        self.tf = tf

        #print("\nTopics in LDA model:")
        tf_feature_names = self.vectorizer.get_feature_names()
        print_top_words(self.lda, tf_feature_names, 15)

    def clean_docs(self, docs):
        """
        Remove stop words, punctuation, etc. and lemmatize words in docs
        """
        # clean docs
        clean_docs = []
        for doc in docs:
            clean_doc = []
            for t in doc:
                if t.text != '\n' and not t.is_stop and not t.is_punct and not t.like_num:
                    clean_doc.append(t.lemma_)
            clean_docs.append(" ".join(clean_doc))

        return clean_docs

    def transform(self, item):
        """
        Transform given item in probability distribution across set topics
        """
        vec = self.vectorizer.transform(item)
        return self.lda.transform(vec)

    def visualise(self):
        import pyLDAvis
        import pyLDAvis.sklearn
        pyLDAvis.enable_notebook()

        pyLDAvis.sklearn.prepare(self.lda, self.tf, self.vectorizer)
