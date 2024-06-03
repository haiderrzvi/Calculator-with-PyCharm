import difflib

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio() * 100

def main():
    file1_path = input("Enter the file path of the first document: ")
    file2_path = input("Enter the file path of the second document: ")

    text1 = load_text(file1_path)
    text2 = load_text(file2_path)

    similarity = calculate_similarity(text1, text2)
    print("Similarity between the two documents: {:.2f}%".format(similarity))

if __name__ == "__main__":
    main()
