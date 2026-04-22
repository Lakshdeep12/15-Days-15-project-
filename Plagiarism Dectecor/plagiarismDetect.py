from difflib import SequenceMatcher


PATH = r"D:\15 Days 15 project\Plagiarism Dectecor"
try:
    with open(f"{PATH}\suspec.txt", 'r') as suspec, open(f"{PATH}\suspec1.txt", 'r') as suspec1:
        text1 = suspec.read()
        text2 = suspec1.read()

    similarity = SequenceMatcher(None, text1, text2).ratio()
    print(f"The Similarity content is: {similarity:.2%}")

except FileNotFoundError:
    print("One or both files were not found.")
except Exception as e:
    print(f"An error occurred: {e}")
