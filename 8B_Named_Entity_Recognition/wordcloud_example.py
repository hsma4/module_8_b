#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:00:48 2020

@author: dan
"""

# You need to pip install wordcloud
from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt

# Read text in for which we want to generate word cloud
with open("wordcloud_example_text.txt", "r") as f:
    full_text = f.read()
    
# Establish a set of stopwords (words such as "the", "and" etc that we're
# probably not interested in).  We can refer to this later to ignore them.
stopwords = set(STOPWORDS)

# Tokenize the text (split into individual words)
tokens = full_text.split()

###

# Set up a translation table that maps punctuation characters (stored in
# string.punctuation) to 'None'.  Ignore the first two entries in the
# maketrans() function - these just create an empty mapping table that maps
# nothing to nothing.  But by having a three input call, the third input is
# automatically mapped to 'None' which is what we need.
punctuation_mapping_table = str.maketrans('', '', string.punctuation)

# The translate() function maps one set of characters to another.  Here, we
# use that to translate tokens with punctuation to ones without punctuation
# by using the mapping table we specified above.
tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]

###

# Convert all tokens to lowercase (so we don't count capitalised words
# differently)
lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

###

# We need to put everything back into a single string of text for the word
# cloud to be generated.  Here, we just use the join function to join our
# list of cleansed words with spaces, and put them in a single string.
joined_string = (" ").join(lower_tokens)

###

# Generate a wordcloud - specify the size, background colour, and the minimum
# font size.  We also specify the set of stopwords we want excluded that we
# set up earlier.  Specify that the word cloud should be generated on our text
# string.  Note that the minimum font size specified will exclude words that
# would appear smaller than this (as they are too uncommon)
wordcloud = WordCloud(width=1800,
                      height=1800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(joined_string)

# Now we plot the wordcloud using matplotlib

# Then set the size of the figure
plt.figure(figsize=(30,40))

# First turn off axes
plt.axis("off")

# Then use imshow to plot an image (here, our wordcloud)
plt.imshow(wordcloud)

# Then save the image as a png
plt.savefig("wordcloud.png")

