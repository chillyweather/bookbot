def main() -> str:
    file_contents = get_text_content("./books/Frankenstein.txt")
    word_count = get_word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    char_dic = char_counter(file_contents)
    for element in char_dic:
        print(f"The {element} character was found {char_dic[element]} times")
    print("--- End report ---")


def get_text_content(path):
    """
    Reads the content of a text file.

    Args:
      path (str): The path to the text file.

    Returns:
      str: The content of the text file.
    """
    with open(path, encoding="utf-8") as f:
        return f.read()


def get_word_count(string) -> int:
    """
    Calculates the number of words in a given string.

    Args:
      string (str): The input string.

    Returns:
      int: The number of words in the string.
    """
    arr = string.split()
    return len(arr)


def char_counter(string):
    """
    Counts the occurrences of each alphabetic character in a given string.

    Args:
      string (str): The input string to count the characters from.

    Returns:
      dict: A dictionary containing the count of each alphabetic character in the string.
          The keys are the characters and the values are the counts.

    Example:
      >>> char_counter("Hello, World!")
      {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
    """
    lowered_string = string.lower()
    result = {}
    for character in lowered_string:
        if character.isalpha():
            if character in result:
                result[character] += 1
            else:
                result[character] = 1
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result


main()
