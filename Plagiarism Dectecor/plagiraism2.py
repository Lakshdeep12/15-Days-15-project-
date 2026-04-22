import os
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


PATH = r"D:\15 Days 15 project\Plagiarism Dectecor"


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def load_files(file_paths):
    documents = []
    raw_documents = []
    file_names = []

    for file_path in file_paths:
        full_path = os.path.join(PATH, file_path)

        if not os.path.exists(full_path):
            print(f"File not found: {file_path}")
            continue

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            raw_documents.append(content)
            documents.append(preprocess(content))
            file_names.append(file_path)

    return documents, raw_documents, file_names


def tfidf_similarity(docs):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    return cosine_similarity(tfidf_matrix)

def ngram_similarity(text1, text2, n=3):
    def get_ngrams(text, n):
        tokens = text.split()
        if len(tokens) < n:
            return set()
        return set(zip(*[tokens[i:] for i in range(n)]))

    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)

    if not ngrams1 or not ngrams2:
        return 0

    return len(ngrams1 & ngrams2) / len(ngrams1 | ngrams2)


def sentence_similarity(text1, text2, threshold=0.7):
    sentences1 = nltk.sent_tokenize(text1)
    sentences2 = nltk.sent_tokenize(text2)

    matches = []

    for s1 in sentences1[:50]:
        for s2 in sentences2[:50]:

            if len(s1.split()) < 5 or len(s2.split()) < 5:
                continue

            # Preprocess sentences for comparison
            s1_proc = preprocess(s1)
            s2_proc = preprocess(s2)

            ratio = SequenceMatcher(None, s1_proc, s2_proc).ratio()

            if ratio > threshold:
                matches.append((s1, s2, ratio))

    return matches


def check_plagiarism():

    
    files = ["suspec.txt", "suspec1.txt"]

    docs, raw_docs, names = load_files(files)

    if len(docs) < 2:
        print("Need at least 2 valid files.")
        return

    print("\nTF-IDF Similarity Matrix:\n")
    sim_matrix = tfidf_similarity(docs)

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            print(f"{names[i]} vs {names[j]}: {sim_matrix[i][j]:.2%}")

    print("\nDetailed Analysis:\n")

    for i in range(len(docs)):
        for j in range(i + 1, len(docs)):

            print(f"\nComparing {names[i]} and {names[j]}")

            ngram_sim = ngram_similarity(docs[i], docs[j])
            print(f"N-gram similarity: {ngram_sim:.2%}")

            matches = sentence_similarity(raw_docs[i], raw_docs[j])

            if matches:
                print("Suspicious Sentences Found:")
                for m in matches[:5]:
                    print(f"\n {m[0]}")
                    print(f" {m[1]}")
                    print(f"Similarity: {m[2]:.2%}")
            else:
                print("No strong sentence matches found.")


if __name__ == "__main__":
    check_plagiarism()