from textblob_de import TextBlobDE
from textblob_de import PatternAnalyzer

# Initialize TextBlob with German language support
tb = TextBlobDE('', analyzer=PatternAnalyzer())

# Open the file for reading
with open('erlkingPT.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total_polarity = 0.0
num_lines = 0

# Loop through each line in the file
for line in lines:
    # Get the sentiment analysis for the line
    blob = TextBlobDE(line, analyzer=PatternAnalyzer())
    polarity = blob.sentiment[0]
    total_polarity += polarity
    num_lines += 1

    # Print the sentence and its polarity
    print(f"Sentence: {line}")
    print(f"Polarity: {polarity}")
    print()

if num_lines > 0:
    avg_polarity = total_polarity / num_lines
    print(f"Average polarity: {avg_polarity}")
else:
    print("No lines in file.")