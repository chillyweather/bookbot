def main() -> str:
    file_contents = get_text_content("./books/Frankenstein.txt")
    print(word_count(file_contents))
    print(char_counter(file_contents))


def get_text_content(path):
    with open(path) as f:
        return f.read()


def word_count(string) -> int:
    arr = string.split()
    return len(arr)


def char_counter(string):
    lowered_string = string.lower()
    result = {}
    for character in lowered_string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result


main()
