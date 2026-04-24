import random
import time


def calculate_errors(reference: str, typed: str) -> int:
    """Calculate the number of character mismatches."""
    errors = abs(len(reference) - len(typed))
    for ref_char, typed_char in zip(reference, typed):
        if ref_char != typed_char:
            errors += 1
    return errors


def calculate_speed(start_time: float, end_time: float, text: str) -> float:
    """Calculate typing speed in characters per second."""
    elapsed_time = end_time - start_time
    if elapsed_time <= 0:
        return 0.0
    return round(len(text) / elapsed_time, 2)


def run_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "Python programming is fun and rewarding",
        "Typing speed can be improved with practice",
        "The rain in Spain stays mainly in the plain"
    ]

    test_sentence = random.choice(sentences)

    print("\n====== Typing Speed Test ======")
    print("Type the following sentence as fast and accurately as you can:\n")
    print(f" {test_sentence}\n")

    input("Press Enter when you're ready...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    errors = calculate_errors(test_sentence, user_input)
    speed = calculate_speed(start_time, end_time, user_input)

    print("\n====== Results ======")
    print(f" Time taken: {round(end_time - start_time, 2)} seconds")
    print(f" Speed: {speed} characters/second")
    print(f" Errors: {errors}")
    print("=============================\n")


def main():
    while True:
        choice = input("Start typing test? (yes/no): ").strip().lower()

        if choice == "yes":
            run_test()
        elif choice == "no":
            print("Goodbye! Thanks for using the Typing Speed Calculator.")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()