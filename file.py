import string
import re


def my_sort(words):
    ukr_letters = "абвгґдежзийіїклмнопрстуфхцчшщьюяє"
    eng_letters = "abcdefghijklmnopqrstuvwxyz"

    ukr_words = [word for word in words if word[0].lower() in ukr_letters]
    eng_words = [word for word in words if word[0].lower() in eng_letters]

    ukr_words_sorted = sorted(ukr_words, key=lambda x: x.lower())
    eng_words_sorted = sorted(eng_words, key=lambda x: x.lower())

    return ukr_words_sorted + eng_words_sorted


def remove_punctuation(text: str):
    return text.translate(str.maketrans("", "", string.punctuation))


def extract_first_sentence(text: str):
    sentences = re.search(r"([^.?!]*[.?!]+)", text)
    if sentences:
        return sentences.group()
    return text


def read_and_sort_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

            first_sentence = extract_first_sentence(text)
            print("Перше речення:")
            print(first_sentence)

            cleaned_text = "".join(
                char for char in text if char not in string.punctuation
            )
            words = cleaned_text.split()

            sorted_words = my_sort(words)

            print(f"\nКiлькiсть слiв: {len(sorted_words)}")
            print("Вiдсотрованi слова:")
            print(sorted_words)

    except Exception as e:
        print(f"Error: {e}")


file_path = "text.txt"
read_and_sort_file(file_path)
