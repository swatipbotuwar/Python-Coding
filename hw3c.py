#!/usr/bin/python3
class singleton(object):
    def __init__(self, word_dict, unigram, bigram):
        self.word_dict= word_dict
        self.unigram= unigram
        self.bigram= bigram
        def __str__(self):
            return "%s" % self.__dict__
        instance = None
        def __new__(self, *args, **kwargs):
            if not singleton.instance:
                singleton.instance = object.__new__(singleton)
            return singleton.instance
