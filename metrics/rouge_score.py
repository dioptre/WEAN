import math
from rouge import Rouge
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

def calc_rouge_scores(ref_sentences, pred_sentences):

    rouge = Rouge()
    scores = rouge.get_scores(pred_sentences, ref_sentences, avg=True)

    return scores

references = []

f = open("output_saved_wikialigned/ref.txt", "r")
for s in f:
    references.append(s)

predictions = []

f = open("output_saved_wikialigned/pred.txt", "r")
for s in f:
    predictions.append(s)

scores = calc_rouge_scores(references, predictions)
print(scores)



