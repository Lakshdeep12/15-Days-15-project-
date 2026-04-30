import pywhatkit as pw
import os

def text_to_handwriting():
    try:
        # Take multi-line input
        print("Enter your text (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)

        text = "\n".join(lines)

        if not text.strip():
            print("No text entered. Exiting...")
            return

        # Custom file name
        file_name = input("Enter output file name (default: handwriting.png): ").strip()
        if not file_name:
            file_name = "handwriting.png"

        # Ensure correct extension
        if not file_name.endswith(".png"):
            file_name += ".png"

        # Convert text to handwriting
        pw.text_to_handwriting(text, save_to=file_name)

        # Confirm file saved
        if os.path.exists(file_name):
            print(f" Handwriting image successfully saved as '{file_name}'")
        else:
            print("Something went wrong. File not found.")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    text_to_handwriting()