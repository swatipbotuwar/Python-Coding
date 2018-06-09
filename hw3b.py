#!/usr/bin/python3
import sys
import pickle
from  hw3c import singleton
import operator

# del[X, Y] = Deletion of Y after X
# outer subscript = X
# inner subscript = Y (deleted letter)

del_table = [['a',0,7,58,21,3,5,18,8,61,0,4,43,5,53,0,9,0,98,28,53,62,1,0,0,2,0],
['b',2,2,1,0,22,0,0,0,183,0,0,26,0,0,2,0,0,6,17,0,6,1,0,0,0,0],
['c',37,0,70,0,63,0,0,24,320,0,9,17,0,0,33,0,0,46,6,54,17,0,0,0,1,0],
['d',12,0,7,25,45,0,10,0,62,1,1,8,4,3,3,0,0,11,1,0,3,2,0,0,6,0],
['e',80,1,50,74,89,3,1,1,6,0,0,32,9,76,19,9,1,237,223,34,8,2,1,7,1,0],
['f',4,0,0,0,13,46,0,0,79,0,0,12,0,0,4,0,0,11,0,8,1,0,0,0,1,0],
['g',25,0,0,2,83,1,37,25,39,0,0,3,0,29,4,0,0,52,7,1,22,0,0,0,1,0],
['h',15,12,1,3,20,0,0,25,24,0,0,7,1,9,22,0,0,15,1,26,0,0,1,0,1,0],
['i',26,1,60,26,23,1,9,0,1,0,0,38,14,82,41,7,0,16,71,64,1,1,0,0,1,7],
['j',0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0],
['k',4,0,0,1,15,1,8,1,5,0,1,3,0,17,0,0,0,1,5,0,0,0,1,0,0,0],
['l',24,0,1,6,48,0,0,0,217,0,0,211,2,0,29,0,0,2,12,7,3,2,0,0,11,0],
['m',15,10,0,0,33,0,0,1,42,0,0,0,180,7,7,31,0,0,9,0,4,0,0,0,0,0],
['n',21,0,42,71,68,1,160,0,191,0,0,0,17,144,21,0,0,0,127,87,43,1,1,0,2,0],
['o',11,4,3,6,8,0,5,0,4,1,0,13,9,70,26,20,0,98,20,13,47,2,5,0,1,0],
['p',25,0,0,0,22,0,0,12,15,0,0,28,1,0,30,93,0,58,1,18,2,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,0,0],
['r',63,4,12,19,188,0,11,5,132,0,3,33,7,157,21,2,0,277,103,68,0,10,1,0,27,0],
['s',16,0,27,0,74,1,0,18,231,0,0,2,1,0,30,30,0,4,265,124,21,0,0,0,1,0],
['t',24,1,2,0,76,1,7,49,427,0,0,31,3,3,11,1,0,203,5,137,14,0,4,0,2,0],
['u',26,6,9,10,15,0,1,0,28,0,0,39,2,111,1,0,0,129,31,66,0,0,0,0,1,0],
['v',9,0,0,0,58,0,0,0,31,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,1,0],
['w',40,0,0,1,11,1,0,11,15,0,0,1,0,2,2,0,0,2,24,0,0,0,0,0,0,0],
['x',1,0,17,0,3,0,0,1,0,0,0,0,0,0,0,6,0,0,0,5,0,0,0,0,1,0],
['y',2,1,34,0,2,0,1,0,1,0,0,1,2,1,1,1,0,0,17,1,0,0,1,0,0,0],
['z',1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
['@',20,14,41,31,20,20,7,6,20,3,6,22,16,5,5,17,0,28,26,6,2,1,24,0,0,2]]

# add[X Y] = Insertion of Y after X
# outer subscript = X
# inner subscript = Y (Inserted Letter)

add_table = [['a',15,1,14,7,10,0,1,1,33,1,4,31,2,39,12,4,3,28,134,7,28,0,1,1,4,1],
['b',3,11,0,0,7,0,1,0,50,0,0,15,0,1,1,0,0,5,16,0,0,3,0,0,0,0],
['c',19,0,54,1,13,0,0,18,50,0,3,1,1,1,7,1,0,7,25,7,8,4,0,1,0,0],
['d',18,0,3,17,14,2,0,0,9,0,0,6,1,9,13,0,0,6,119,0,0,0,0,0,5,0],
['e',39,2,8,76,147,2,0,1,4,0,3,4,6,27,5,1,0,83,417,6,4,1,10,2,8,0],
['f',1,0,0,0,2,27,1,0,12,0,0,10,0,0,0,0,0,5,23,0,1,0,0,0,1,0],
['g',8,0,0,0,5,1,5,12,8,0,0,2,0,1,1,0,1,5,69,2,3,0,1,0,0,0],
['h',4,1,0,1,24,0,10,18,17,2,0,1,0,1,4,0,0,16,24,22,1,0,5,0,3,0],
['i',10,3,13,13,25,0,1,1,69,2,1,17,11,33,27,1,0,9,30,29,11,0,0,1,0,1],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['k',2,4,0,1,9,0,0,1,1,0,1,1,0,0,2,1,0,0,95,0,1,0,0,0,4,0],
['l',3,1,0,1,38,0,0,0,79,0,2,128,1,0,7,0,0,0,97,7,3,1,0,0,2,0],
['m',11,1,1,0,17,0,0,1,6,0,1,0,102,44,7,2,0,0,47,1,2,0,1,0,0,0],
['n',15,5,7,13,52,4,17,0,34,0,1,1,26,99,12,0,0,2,156,53,1,1,0,0,1,0],
['o',14,1,1,3,7,2,1,0,28,1,0,6,3,13,64,30,0,16,59,4,19,1,0,0,1,1],
['p',23,0,1,1,10,0,0,20,3,0,0,2,0,0,26,70,0,29,52,9,1,1,1,0,0,0],
['q',0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['r',15,2,1,0,89,1,1,2,64,0,0,5,9,7,10,0,0,132,273,29,7,0,1,0,10,0],
['s',13,1,7,20,41,0,1,50,101,0,2,2,10,7,3,1,0,1,205,49,7,0,1,0,7,0],
['t',39,0,0,3,65,1,10,24,59,1,0,6,3,1,23,1,0,54,264,183,11,0,5,0,6,0],
['u',15,0,3,0,9,0,0,1,24,1,1,3,3,9,1,3,0,49,19,27,26,0,0,2,3,0],
['v',0,2,0,0,36,0,0,0,10,0,0,1,0,1,0,1,0,0,0,0,1,5,1,0,0,0],
['w',0,0,0,1,10,0,0,1,1,0,1,1,0,2,0,0,1,1,8,0,2,0,4,0,0,0],
['x',0,0,18,0,1,0,0,6,1,0,0,0,1,0,3,0,0,0,2,0,0,0,0,1,0,0],
['y',5,1,2,0,3,0,0,0,2,0,0,1,1,6,0,0,0,1,33,1,13,0,1,0,2,0],
['z',2,0,0,0,5,1,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4],
['@',46,8,9,8,26,11,14,3,5,1,17,5,6,2,2,10,0,6,23,2,11,1,2,1,1,2]]

# sub[X Y] = Substitution of X (incorrect) for Y (correct)
# outer subscript = X
# inner subscript = Y (correct)

sub_table = [['a',0,0,7,1,342,0,0,2,118,0,1,0,0,3,76,0,0,1,35,9,9,0,1,0,5,0],
['b',0,0,9,9,2,2,3,1,0,0,0,5,11,5,0,10,0,0,2,1,0,0,8,0,0,0],
['c',6,5,0,16,0,9,5,0,0,0,1,0,7,9,1,10,2,5,39,40,1,3,7,1,1,0],
['d',1,10,13,0,12,0,5,5,0,0,2,3,7,3,0,1,0,43,30,22,0,0,4,0,2,0],
['e',388,0,3,11,0,2,2,0,89,0,0,3,0,5,93,0,0,14,12,6,15,0,1,0,18,0],
['f',0,15,0,3,1,0,5,2,0,0,0,3,4,1,0,0,0,6,4,12,0,0,2,0,0,0],
['g',4,1,11,11,9,2,0,0,0,1,1,3,0,0,2,1,3,5,13,21,0,0,1,0,3,0],
['h',1,8,0,3,0,0,0,0,0,0,2,0,12,14,2,3,0,3,1,11,0,0,2,0,0,0],
['i',103,0,0,0,146,0,1,0,0,0,0,6,0,0,49,0,0,0,2,1,47,0,2,1,15,0],
['j',0,1,1,9,0,0,1,0,0,0,0,2,1,0,0,0,0,0,5,0,0,0,0,0,0,0],
['k',1,2,8,4,1,1,2,5,0,0,0,0,5,0,2,0,0,0,6,0,0,0,.4,0,0,3],
['l',2,10,1,4,0,4,5,6,13,0,1,0,0,14,2,5,0,11,10,2,0,0,0,0,0,0],
['m',1,3,7,8,0,2,0,6,0,0,4,4,0,180,0,6,0,0,9,15,13,3,2,2,3,0],
['n',2,7,6,5,3,0,1,19,1,0,4,35,78,0,0,7,0,28,5,7,0,0,1,2,0,2],
['o',91,1,1,3,116,0,0,0,25,0,2,0,0,0,0,14,0,2,4,14,39,0,0,0,18,0],
['p',0,11,1,2,0,6,5,0,2,9,0,2,7,6,15,0,0,1,3,6,0,4,1,0,0,0],
['q',0,0,1,0,0,0,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',0,14,0,30,12,2,2,8,2,0,5,8,4,20,1,14,0,0,12,22,4,0,0,1,0,0],
['s',11,8,27,33,35,4,0,1,0,1,0,27,0,6,1,7,0,14,0,15,0,0,5,3,20,1],
['t',3,4,9,42,7,5,19,5,0,1,0,14,9,5,5,6,0,11,37,0,0,2,19,0,7,6],
['u',20,0,0,0,44,0,0,0,64,0,0,0,0,2,43,0,0,4,0,0,0,0,2,0,8,0],
['v',0,0,7,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,8,3,0,0,0,0,0,0],
['w',2,2,1,0,1,0,0,2,0,0,1,0,0,0,0,7,0,6,3,3,1,0,0,0,0,0],
['x',0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0],
['y',0,0,2,0,15,0,1,7,15,0,0,0,2,0,6,1,0,7,36,8,5,0,0,1,0,0],
['z',0,0,0,7,0,0,0,0,0,0,0,7,5,0,0,0,0,2,21,3,0,0,0,0,3,0]]

# transpose[X  Y] = Reversal of XY
# outer subscript = X
# inner subscript = Y

transpose_table = [['a',0,0,2,1,1,0,0,0,19,0,1,14,4,25,10,3,0,27,3,5,31,0,0,0,0,0],
['b',0,0,0,0,2,0,0,0,0,0,0,1,1,0,2,0,0,0,2,0,0,0,0,0,0,0],
['c',0,0,0,0,1,0,0,1,85,0,0,15,0,0,13,0,0,0,3,0,7,0,0,0,0,0],
['d',0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0],
['e',1,0,4,5,0,0,0,0,60,0,0,21,6,16,11,2,0,29,5,0,85,0,0,0,2,0],
['f',0,0,0,0,0,0,0,0,12,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['g',4,0,0,0,2,0,0,0,0,0,0,1,0,15,0,0,0,3,0,0,3,0,0,0,0,0],
['h',12,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0],
['i',15,8,31,3,66,1,3,0,0,0,0,9,0,5,11,0,1,13,42,35,0,6,0,0,0,3],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['k',0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['l',11,0,0,12,20,0,1,0,4,0,0,0,0,0,1,3,0,0,1,1,3,9,0,0,7,0],
['m',9,0,0,0,20,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,0,0,0,0,0],
['n',15,0,6,2,12,0,8,0,1,0,0,0,3,0,0,0,0,0,6,4,0,0,0,0,0,0],
['o',5,0,2,0,4,0,0,0,5,0,0,1,0,5,0,1,0,11,1,1,0,0,7,1,0,0],
['p',17,0,0,0,4,0,0,1,0,0,0,0,0,0,1,0,0,5,3,6,0,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',12,0,0,0,24,0,3,0,14,0,2,2,0,7,30,1,0,0,0,2,10,0,0,0,2,0],
['s',4,0,0,0,9,0,0,5,15,0,0,5,2,0,1,22,0,0,0,1,3,0,0,0,16,0],
['t',4,0,3,0,4,0,0,21,49,0,0,4,0,0,3,0,0,5,0,0,11,0,2,0,0,0],
['u',22,0,5,1,1,0,2,0,2,0,0,2,1,0,20,2,0,11,11,2,0,0,0,0,0,0],
['v',0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['w',0,0,0,0,0,0,0,4,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,8,0],
['x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
['y',0,1,2,0,0,0,1,0,0,0,0,3,0,0,0,2,0,1,10,0,0,0,0,0,0,0],
['z',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

correction_list=[]    #list for correction class objects

def create_dict(table_name):
    my_key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    my_dict = {}
    for item in table_name:
        values= item[1:]
        new_l =list(zip(my_key, values))
        my_dict[item[0]] = {new_l[i][0] : new_l[i][1] for i, val in enumerate(new_l)}
    return my_dict

class correction:
    def __init__(self,candidate_correction,correct_letter,error_letter,x_given_w,x_given_word,prob_word,final_val):
        self.candidate_correction = candidate_correction
        self.correct_letter = correct_letter
        self.error_letter = error_letter
        self.x_given_w = x_given_w
        self.x_given_word = x_given_word
        self.prob_word = prob_word
        self.final_val = final_val

def add_letter(input_word, complete_dict, total_count, delete_table_dict):     #create list of possible correction word by adding alphabet to input_word
    add_prune_list=[]
    add_letter_word =[]
    for i in range(len(input_word)+1):
        for j in range(ord('a'), ord('z')+1, 1):
            add_word= input_word[:i]+chr(j)+ input_word[i:]
            add_letter_word.append(add_word)
            if add_word in complete_dict.word_dict:
                add_prune_list.append(add_word)
                candidate_correction = add_word
                correct_letter = add_word[i-1]
                error_letter = "-" 
                if i == 0:
                    x = '@'
                    w = '@'+add_word[i+1]
                    repl= '<'+add_word[i+1]
                    x_given_word= round((delete_table_dict['@'][add_word[i+1]]/complete_dict.bigram[repl]),9)
                else:
                    x=add_word[i-1]
                    w= add_word[i-1]+add_word[i]   #ct is typed as c in training set
                    x_given_word = round((delete_table_dict[x][add_word[i]]/complete_dict.bigram[w]),9)
                x_given_w = x+"|"+w
                prob_word = round(((complete_dict.word_dict[add_word] +0.5)/(total_count + (0.5*len(complete_dict.word_dict)))),9)
                final_val = round(((10**9)* x_given_word * prob_word),6)
                correction_list.append(correction(candidate_correction,correct_letter,error_letter,x_given_w,x_given_word,prob_word,final_val))
    return correction_list, add_letter_word, add_prune_list

def del_letter(input_word, complete_dict, total_count,add_table_dict):      #create list of possible correction by deleting letter from input_word
    delete_prune_list=[] 
    delete_letter_word =[]
    for i in range(len(input_word)):
        del_word = input_word[:i]+input_word[i+1:]
        delete_letter_word.append(del_word)
        if del_word in complete_dict.word_dict:
            delete_prune_list.append(del_word)
            candidate_correction = del_word
            correct_letter = "-"
            error_letter = input_word[i]
            if i == 0:
                x= error_letter
                w= '@'
                x_given_word = round(((add_table_dict['@'][input_word[i]])/(complete_dict.unigram['<'])),9)
            else:
                x= input_word[(i-1):(i-1)+2]
                w= input_word[i-1]
                x_given_word = round(((add_table_dict[input_word[i-1]][input_word[i]])/(complete_dict.unigram[w])),9)
            x_given_w = x + "|" + w
            prob_word = round(((complete_dict.word_dict[del_word]+0.5)/(total_count + (0.5 * len(complete_dict.word_dict)))),9)
            final_val = round(((10**9)* x_given_word * prob_word),6)
            correction_list.append(correction(candidate_correction,correct_letter,error_letter,x_given_w,x_given_word,prob_word,final_val))
    return correction_list, delete_letter_word, delete_prune_list

def sub_letter(input_word, complete_dict, total_count, sub_table_dict):       #create list of word by substituting each character by other alphabet
    sub_prune_list=[]
    sub_letter_word =[]
    for i in range(len(input_word)):
        for j in range(ord('a'), ord('z')+1, 1):
            sub_word = input_word[:i]+chr(j)+ input_word[i+1:]
            sub_letter_word.append(sub_word)
            if sub_word in complete_dict.word_dict:
                sub_prune_list.append(sub_word)
                candidate_correction = sub_word
                correct_letter = sub_word[i]
                error_letter = input_word[i]
                x=error_letter
                w= correct_letter
                x_given_w=x +"|" +w
                x_given_word = round((sub_table_dict[error_letter][correct_letter] /complete_dict.unigram[correct_letter]),9)
                prob_word = round(((complete_dict.word_dict[sub_word] +0.5)/(total_count + (0.5 * len(complete_dict.word_dict)))),9)
                final_val = round(((10**9)* x_given_word * prob_word),6)
                correction_list.append(correction(candidate_correction,correct_letter,error_letter,x_given_w,x_given_word,prob_word,final_val))
    return correction_list, sub_letter_word, sub_prune_list

def trans_letters(input_word, complete_dict, total_count, transpose_table_dict):     # create list of word by swapping two consecutive character in a word
    rev_prune_list=[]
    rev_letter_word =[]
    for i in range(len(input_word)-1):
        rev_word = input_word[:i]+input_word[i+1]+ input_word[i]+input_word[i+2:]
        rev_letter_word.append(rev_word)
        if rev_word in complete_dict.word_dict:
            rev_prune_list.append(rev_word)
            candidate_correction = rev_word
            correct_letter = rev_word[i+1]+rev_word[i]
            error_letter = rev_word[i]+rev_word[i+1]
            x=error_letter
            w= correct_letter 
            x_given_w = x +"|" +w
            x_given_word =round((transpose_table_dict[rev_word[i]][rev_word[i+1]] /complete_dict.bigram[error_letter]),9)
            prob_word = round(((complete_dict.word_dict[rev_word] +0.5)/(total_count + (0.5*len(complete_dict.word_dict)))),9)
            final_val = round(((10**9)* x_given_word * prob_word),6)
            correction_list.append(correction(candidate_correction,correct_letter,error_letter,x_given_w,x_given_word,prob_word,final_val))
    return correction_list, rev_letter_word, rev_prune_list



if len(sys.argv) < 2:
    print("Expected at least one Mispelled word as a argument.")
    sys.exit()

else:
    #create a dictionary from list of table
    delete_table_dict={}
    add_table_dict ={}
    sub_table_dict={}
    transpose_table_dict = {}
    delete_table_dict = create_dict(del_table)
    add_table_dict = create_dict(add_table)
    sub_table_dict = create_dict(sub_table)
    transpose_table_dict = create_dict(transpose_table)
    read_pickle= open("my_data.dat",'rb')         #unpickle the pickle file
    complete_dict = pickle.load(read_pickle)
    total_count = sum(complete_dict.word_dict.values())
    read_pickle.close()
    for i in range(1,len(sys.argv)):      #perform processing for each of the passed mispelled word
        correction_list, add_letter_word, add_prune_list = add_letter(sys.argv[i], complete_dict, total_count, delete_table_dict)
        correction_list, delete_letter_word, delete_prune_list = del_letter(sys.argv[i], complete_dict, total_count, add_table_dict)
        correction_list, sub_letter_word, sub_prune_list = sub_letter(sys.argv[i], complete_dict, total_count, sub_table_dict)
        correction_list, rev_letter_word, rev_prune_list = trans_letters(sys.argv[i], complete_dict, total_count, transpose_table_dict)
        print("Number of possible correction after adding letter {:>10}".format(len(add_letter_word)))
        print("Number of words after prune add letter list       {:>10}".format(len(add_prune_list)))
        
        print("Number of possible correction after deleting letter {:>10}".format(len(delete_letter_word)))
        print("Number of words after prune delete letter list      {:>10}".format(len(delete_prune_list)))
        
        print("Number of possible correction after substitute of letter {:>10}".format(len(sub_letter_word)))
        print("Number of words after prune substitute letter list       {:>10}".format(len(sub_prune_list)))
        
        print("Number of possible correction after transpose of consecutive letter {:>10}".format(len(rev_letter_word)))
        print("Number of words after prune swap letter list                        {:>10}".format(len(rev_prune_list)))

        print("list of possible correction for given mispelled word are :",end ="\n")
        
        print("|------------------------------------------------------------------------------------------------|")
        print("{}{:<20} {} {:<7} {} {:<6} {} {:<8} {} {:<12} {}".format("|", "Candidate ", "|", "Correct", "|", "Error", "|", "x|w", "|", "P(x|w)", "|"), end="")
        print(" {:<12} {} {:<12} {}".format("P(word)", "|", "10**9*(P(x|w)P(w)", "|"))
        print("{}{:<20} {} {:<7} {} {:<6} {} {:<8} {} {:<12} {}".format("|", "Correction", "|", "Letter ", "|", "Letter","|", "   ", "|", "      ", "|"),end="")
        print(" {:<12} {} {:<12} {}".format("       ", "|", "           ", "|"))
        print("|------------------------------------------------------------------------------------------------|")

        correction_list1 = sorted(correction_list, key = operator.attrgetter('final_val'), reverse = True)
        for j in range(len(correction_list1)):
            print("{} {:<20}".format( "|", correction_list1[j].candidate_correction), end ="")
            print("{} {:<7} {} {:<6} {} ".format("|",correction_list1[j].correct_letter,"|", correction_list1[j].error_letter,"|"), end="")
            print("{:<8} {} {:<.9f} {}".format(correction_list1[j].x_given_w,"|",correction_list1[j].x_given_word,"|"), end="")
            print("{:<.9f} {}".format(correction_list1[j].prob_word, "|"),end = "")
            print("{:^.6f}         {}".format(correction_list1[j].final_val,    "|"))
            print("|------------------------------------------------------------------------------------------------|")
        print("\n")
        correction_list.clear()
