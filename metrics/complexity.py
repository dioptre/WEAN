import math
from textstat import syllable_count, dale_chall_readability_score, gunning_fog
import numpy as np

# The Flesch Reading Ease Readability Formula 
# http://www.readabilityformulas.com/flesch-reading-ease-readability-formula.php

# The specific mathematical formula is: 

# RE = 206.835 – (1.015 x ASL) – (84.6 x ASW) 
# RE = Readability Ease 
# ASL = Average Sentence Length (i.e., the number of words divided by the number of sentences) 
# ASW = Average number of syllables per word (i.e., the number of syllables divided by the number of words) 

# The output, i.e., RE is a number ranging from 0 to 100. The higher the number, the easier the text is to read. 
# • Scores between 90.0 and 100.0 are considered easily understandable by an average 5th grader.
# • Scores between 60.0 and 70.0 are considered easily understood by 8th and 9th graders.
# • Scores between 0.0 and 30.0 are considered easily understood by college graduates.

def calc_complexity_scores(input_sentences):

    # return calc_complexity_scores_dale_chall(input_sentences)

    complexity_scores = []

    for sentence in input_sentences:
        asl = len(sentence.split())
        syllables_count = syllable_count(sentence, lang='en_US')
        asw = syllables_count/asl

        RE = 206.835 - (1.015 * asl) - (84.6 * asw)

        complexity_scores.append(RE)

    return complexity_scores

def calc_complexity_scores_dale_chall(input_sentences):
    complexity_scores = []

    for sentence in input_sentences:
        score = dale_chall_readability_score(sentence)
        complexity_scores.append(score)

    return complexity_scores

def calc_complexity_scores_gunning_fog(input_sentences):
    complexity_scores = []

    for sentence in input_sentences:
        score = gunning_fog(sentence)
        complexity_scores.append(score)

    return complexity_scores


# sentences = []

# f = open("output_saved_wikialigned/pred.txt", "r")
# for s in f:
#   sentences.append(s)

# scores = calc_complexity_scores(sentences)
# scores = np.array(scores)
# avg_score = np.mean(scores)

# print(avg_score)



