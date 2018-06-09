#!/usr/bin/python3
import re
import sys
from collections import defaultdict
import operator
import time
import pickle
from hw3c import singleton

def prepare_data(filename):
    f= open(filename,'r')
    word_dict= defaultdict(int)
    unigram = defaultdict(int)
    bigram = defaultdict(int)
    start_time=time.perf_counter() 
    start_cpu_time=time.process_time()
    count = 0
    for line in f:
        new_line= re.sub('(AP[0-9]+\-[0-9]+)|([^a-zA-Z])'," ", line).lower()
        word_list= new_line.split()                                 #task_Number 1
        for words in word_list:
            word_dict[words] += 1
            token = "<" + words +">"
            unigram_list = [i for i in token]
            bigram_list = [ token[i] + token[i+1] for i in range(len(token)-1)]
            for val in unigram_list:
                unigram[val] += 1
            for val in bigram_list:
                bigram[val] += 1
    f.close()
    end_time= time.perf_counter() 
    end_cpu_time=time.process_time()
    print("start at elapsed time           {0:>.4f}, cpu time  {0:>.4f}".format(start_time,start_cpu_time))
    print("finish reading at elapsed time  {0:>.4f}, cpu time  {0:>.4f}".format(end_time,end_cpu_time ))
    print("total elapsed time              {:10.4f}, cpu time  {:>10.4f}".format(end_time-start_time,end_cpu_time - start_cpu_time))
    print("Number Of Words:    ",sum(word_dict.values()))
    print("Number Of Types (Distinct Words):    ",len(word_dict), end="\n")
    print("Frequency of word a : {:>10}".format(word_dict['a']))
    print("Frequency of word The: {:>10}".format(word_dict['the'], end="\n"))

    sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse = True)
    print("List of first 10 words with higher frequency in corpus", end="\n")
    for i in range(len(sorted_word_dict)):
        if count == 10:
            break
        else:
            print("{:<10s} {:>15d}".format(sorted_word_dict[i][0] , sorted_word_dict[i][1]))
            count += 1
    print("\n")

    sorted_unigram=  sorted(unigram.keys())
    print("Unigram counts:")
    for keyv in sorted_unigram:
        print("{:<1s} {:>15d}".format(keyv, unigram[keyv]))
    print("\n")
    print("Bigram counts:")
    sorted_bigram = sorted(bigram.keys())
    for keyb in sorted_bigram:
        print("{:<1s} {:>15d}".format(keyb, bigram[keyb]))
    return word_dict, unigram , bigram

if len(sys.argv)!= 2:
    print("Expecting File Name as a argument")
    sys.exit()
else:
    word_dict, unigram , bigram = prepare_data(sys.argv[1])
    #word_dict, unigram , bigram = prepare_data("/home/turing/t90rkf1/dnl/dhw/data/ap88.txt")
    my_data = singleton(word_dict, unigram , bigram)               #create object of Singleton class
    my_file = open("my_data.dat", 'wb')
    pickle.dump(my_data, my_file)                                  #store singleton class object in pickle file
    my_file.close()
