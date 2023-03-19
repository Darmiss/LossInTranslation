from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

# Initialize TextBlob with French language support
tb = TextBlob('', pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

# Open the file for reading
with open('demFR.txt', 'r') as f:
    lines = f.readlines()

total_polarity = 0.0
num_lines = 0

# Loop through each line in the file
for line in lines:
    # Get the sentiment analysis for the line
    blob = TextBlob(line, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    polarity, subjectivity = blob.sentiment
    total_polarity += polarity
    num_lines += 1

    # Print the sentence and its polarity
    print(f"Sentence: {line}")
    print(f"Polarity: {polarity}")
    print()

# Calculate the average polarity
if num_lines > 0:
    avg_polarity = total_polarity / num_lines
    print(f"Average polarity: {avg_polarity}")
else:
    print("No lines in file.")
