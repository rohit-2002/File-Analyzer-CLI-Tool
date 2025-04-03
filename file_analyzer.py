import sys
import re
from collections import Counter

# Define a set of common stop words
STOP_WORDS = {'the', 'is', 'and', 'a', 'an', 'of', 'to', 'in', 'for', 'on', 'with'}

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Remove punctuation (except sentence end markers)
    text_no_punct = re.sub(r'[^\w\s\.\?!]', '', text)
    
    # Split text into sentences (assuming sentences end with ., ? or !)
    sentences = re.split(r'[\.?!]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    num_sentences = len(sentences)
    
    # Split text into words
    words = re.findall(r'\w+', text.lower())
    total_words = len(words)
    
    # Filter out stop words for frequency analysis
    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_counts = Counter(filtered_words)
    top_5 = word_counts.most_common(5)
    
    # Calculate average word length (using all words)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Print summary report
    print("Summary Report:")
    print(f"Total number of words: {total_words}")
    print("Top 5 most frequent words (ignoring common stop words):")
    for word, count in top_5:
        print(f"  {word}: {count}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Number of sentences: {num_sentences}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <path_to_text_file>")
        sys.exit(1)
    analyze_file(sys.argv[1])
