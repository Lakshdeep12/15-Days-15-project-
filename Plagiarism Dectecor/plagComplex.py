import os
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PATH = r"D:\15 Days 15 project\Plagiarism Dectecor"

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().lower()

def difflib_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

# Full paths
file1 = os.path.join(PATH, "suspec.txt")
file2 = os.path.join(PATH, "suspec1.txt")

text1 = read_file(file1)
text2 = read_file(file2)

sim1 = difflib_similarity(text1, text2)
sim2 = tfidf_similarity(text1, text2)

final_score = (sim1 + sim2) / 2

print(f"Difflib Similarity : {sim1:.2%}")
print(f"TF-IDF Similarity  : {sim2:.2%}")
print(f"\nFinal Plagiarism Score: {final_score:.2%}")

if final_score > 0.7:
    print(" High Plagiarism Detected")
elif final_score > 0.4:
    print(" Moderate Similarity")
else:
    print(" Low or No Plagiarism")