import re
from collections import Counter

def extract_text_from_rtf(file_path):
    # Try different encodings
    for encoding in ['utf-8', 'latin1', 'cp1252']:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                rtf_content = file.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("Failed to decode the file with available encodings.")
    
    # Remove RTF formatting using regex
    text = re.sub(r'{\\.*?}', '', rtf_content)  # Remove RTF control words
    text = re.sub(r'\\[a-z]+\d*', '', text)    # Remove other RTF commands
    text = re.sub(r'[{}]', '', text)           # Remove braces
    return text

def get_most_common_words(text, top_n=100):
    # Normalize text to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

def main():
    file_path = input("Enter the path to your RTF file: ")
    try:
        text = extract_text_from_rtf(file_path)
        common_words = get_most_common_words(text)
        print("Top 50 Most Common Words:")
        for word, count in common_words:
            print(f"{word}: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
