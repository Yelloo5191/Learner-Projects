#! python3
# mclip.py - A program to store and use easily accessible clipped text

TEXT = {'agree': "Yes, I agree. That sounds fine to me.", 
        'busy': "Sorry, can we do this later this week or next week?",
        'upsell': "Would you consider making this a monthly donation?",
        'greet': "Barev dzez, im anun@ hovhannes e"}

import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: python mclip.py <keyphrase> - copy phrase text')

keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)