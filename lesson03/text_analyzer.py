from os.path import basename, getsize
from itertools import islice
from time import time
import re

# regular expression to detect word by presence of any unicode character
word_regex = re.compile(r'[\w\d]', re.UNICODE)

# regular expression to detect unicode character
char_regex = re.compile(r'^\w$', re.UNICODE)

# regular expression to detect digit or _
digit_regex = re.compile(r'[0-9_]', re.UNICODE)


def is_word(token):
    return word_regex.search(token)

def is_char(token):
    # TODO use single regular expression
    return char_regex.search(token) and not digit_regex.search(token)

def count_words(line):
    return sum(1 for word in line.split() if is_word(word))

def count_chars(line):
    return sum(1 for char in line if is_char(char))

def process_unique_words(line, word_dict):
    for word in line.split():
        if (is_word(word)):
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

def process_unique_chars(line, char_dict):
    for char in line:
        if (is_char(char)):
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

def print_top_words(word_dict, count):
    for word in islice(sorted(word_dict, key=word_dict.get, reverse=True), count):
        print("{}: {}".format(word, word_dict[word]))

# any object enumerable as string collection can be passed as filestream
def analyze_stream(filestream):
    word_count = 0
    char_count = 0
    word_dict = {}
    char_dict = {}

    for line in filestream:
        word_count += count_words(line)
        char_count += count_chars(line)
        process_unique_words(line, word_dict)
        process_unique_chars(line, char_dict)

    print("word count: {0}".format(word_count))
    print("character count: {0}".format(char_count))
    print("unique word count: {0}".format(len(word_dict)))
    print("unique character count: {0}".format(len(char_dict)))
    # print(sorted(char_set))
    print("10 most used words:")
    print_top_words(word_dict, 10)
    print("10 most used characters:")
    print_top_words(char_dict, 10)

# open the file using context manager and analyze its contents
def analyze_file(filename):
    with open(filename) as filestream:
        analyze_stream(filestream)

def benchmark_file(filename):
    print("analyzing {0} ({1:.1f}M)".format(
        basename(filename),
        getsize(filename) / 1024 / 1024))
    t0 = time()
    analyze_file(filename)
    t1 = time()
    print("Time taken: {0:.2f}s".format(t1 - t0))
    print()

if __name__ == "__main__":
    benchmark_file("../test_files/test.txt")
    benchmark_file("../test_files/bible.txt")
    benchmark_file("../test_files/quran-simple.txt")
