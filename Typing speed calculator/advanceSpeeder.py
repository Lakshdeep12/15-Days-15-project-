import random
import time


def calculate_errors(reference: str, typed: str) -> int:
    errors = abs(len(reference) - len(typed))
    for r, t in zip(reference, typed):
        if r != t:
            errors += 1
    return errors


def calculate_accuracy(reference: str, typed: str) -> float:
    errors = calculate_errors(reference, typed)
    total_chars = len(reference)
    if total_chars == 0:
        return 0.0
    accuracy = ((total_chars - errors) / total_chars) * 100
    return round(max(0, accuracy), 2)


def calculate_wpm(typed: str, elapsed_time: float) -> float:
    words = len(typed.split())
    minutes = elapsed_time / 60
    if minutes == 0:
        return 0.0
    return round(words / minutes, 2)


EASY = [
    "The cat sat on the mat",
    "Python is easy to learn",
    "Practice makes perfect"
]

MEDIUM = [
    "Typing speed improves with regular practice",
    "Consistency is the key to mastery",
    "Focus on accuracy before speed"
]

HARD = [
    "The quick brown fox jumps over the lazy dog",
    "Lorem ipsum dolor sit amet consectetur adipiscing elit",
    "Sphinx of black quartz judge my vow"
]


def countdown(seconds: int):
    print("\nGet ready!")
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...", end="\r")
        time.sleep(1)
    print("Go!            ")


def run_test(level: str):
    if level == "easy":
        sentence = random.choice(EASY)
    elif level == "medium":
        sentence = random.choice(MEDIUM)
    else:
        sentence = random.choice(HARD)

    print("\n====== Typing Speed Test ======")
    print(f"Difficulty: {level.upper()}")
    print("\nType this:\n")
    print(sentence)

    input("Press Enter when ready...")
    countdown(3)

    start_time = time.time()
    user_input = input("\nStart typing:\n")
    end_time = time.time()

    elapsed = end_time - start_time
    errors = calculate_errors(sentence, user_input)
    accuracy = calculate_accuracy(sentence, user_input)
    wpm = calculate_wpm(user_input, elapsed)

    print("\n========== RESULTS ==========")
    print(f"Time Taken : {round(elapsed, 2)} sec")
    print(f"Speed      : {wpm} WPM")
    print(f"Accuracy   : {accuracy}%")
    print(f"Errors     : {errors}")
    print("=============================\n")


def main():
    print("===== Advanced Typing Speed Tester =====")

    while True:
        print("\nSelect Difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            run_test("easy")
        elif choice == "2":
            run_test("medium")
        elif choice == "3":
            run_test("hard")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()