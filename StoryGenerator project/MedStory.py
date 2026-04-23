import random

def get_user_inputs():
    print("\n--- Enter some words ---")
    words = {
        "noun1": input("Enter a noun: "),
        "noun2": input("Enter another noun: "),
        "verb1": input("Enter a verb: "),
        "verb2": input("Enter another verb: "),
        "adjective1": input("Enter an adjective: "),
        "adjective2": input("Enter another adjective: "),
        "place": input("Enter a place: "),
        "person": input("Enter a person's name: ")
    }
    return words


def generate_story(words):
    stories = [
        f"Today I went to {words['place']} and saw a {words['adjective1']} {words['noun1']}. "
        f"It suddenly started to {words['verb1']}! Out of nowhere, {words['person']} appeared and saved the day.",

        f"{words['person']} was wandering in {words['place']} with a {words['adjective2']} {words['noun2']}. "
        f"They decided to {words['verb2']} together and it became the most unforgettable day ever.",

        f"In a {words['adjective1']} land, a {words['noun1']} learned how to {words['verb1']}. "
        f"But when it met {words['person']} at {words['place']}, everything changed.",

        f"At {words['place']}, there was a {words['adjective2']} {words['noun2']} that loved to {words['verb2']}. "
        f"One day, it bumped into {words['person']} and they became best friends.",

        f"{words['person']} found a {words['adjective1']} {words['noun1']} in {words['place']}. "
        f"Together, they started to {words['verb1']} and accidentally created a {words['adjective2']} {words['noun2']}!"
    ]

    return random.choice(stories)


def save_story(story):
    choice = input("\nDo you want to save this story to a file? (yes/no): ").lower()
    if choice == "yes":
        with open("stories.txt", "a") as file:
            file.write(story + "\n\n")
        print(" Story saved to 'stories.txt'")


def main():
    print(" Welcome to the Story Generator!")

    while True:
        words = get_user_inputs()
        story = generate_story(words)

        print("\n Your Generated Story:\n")
        print(story)

        save_story(story)

        again = input("\nDo you want to create another story? (yes/no): ").lower()
        if again != "yes":
            print("\n Goodbye! Thanks for using the Story Generator.")
            break

# print ("You have to enter field such as noun, verb, adjective, place and person to generate a story. You can also save the generated story to a file if you wish.")
if __name__ == "__main__":
    main()