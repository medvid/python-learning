from os.path import basename, getsize
from itertools import islice
from time import time
import re
import threading

NUM_THREADS = 10
LINES_PER_THREAD = 200000


class StreamParser(object):
    def __init__(self, filestream):
        self.__fileiter = iter(filestream)
        # lock to sync with parser threads
        self.__lock = threading.Lock()
        # event to sync with main thread
        self.__event = threading.Event()
        self.__eof = False

    # DOESN'T WORK
    def getlines_async(self, count):
        with self.__lock:
            if not self.__eof:
                for i in range(count):
                    try:
                        yield next(self.__fileiter)
                    except StopIteration:
                        self.__eof = True
                        self.__event.set()
                        raise StopIteration

    def getlines(self, count):
        lines = []
        with self.__lock:
            if not self.__eof:
                for i in range(count):
                    try:
                        lines.append(next(self.__fileiter))
                    except StopIteration:
                        lines.append(None)
                        self.__eof = True
                        self.__event.set()
                        break
        return lines

    def wait(self):
        self.__event.wait()


class DataCollector(object):
    def __init__(self):
        self.__word_dict = {}
        self.__char_dict = {}

    def add_word(self, word):
        if word in self.__word_dict:
            self.__word_dict[word] += 1
        else:
            self.__word_dict[word] = 1

    def add_char(self, char):
        if char in self.__char_dict:
            self.__char_dict[char] += 1
        else:
            self.__char_dict[char] = 1

    @property
    def word_count(self):
        return len(self.__word_dict)

    @property
    def char_count(self):
        return len(self.__char_dict)

    def merge(collectors):
        total = DataCollector()
        for collector in collectors:
            total.__word_dict.update(collector.__word_dict.copy())
            total.__char_dict.update(collector.__char_dict.copy())
        return total

    def print_top_words(dict, count):
        for word in islice(sorted(dict, key=dict.get, reverse=True), count):
            print("{}: {}".format(word, dict[word]))
            
    def print_stats(self):
        print("word count: {0}".format(self.word_count))
        print("character count: {0}".format(self.char_count))
        print("10 most used words:")
        DataCollector.print_top_words(self.__word_dict, 10)
        print("10 most used characters:")
        DataCollector.print_top_words(self.__char_dict, 10)


class TextAnalyzer(object):
    # regular expression to detect word by presence of any unicode character
    word_regex = re.compile(r'[\w\d]', re.UNICODE)

    def __init__(self, data):
        self.__data = data

    def analyze_words(self, words):
        for word in words:
            if self.word_regex.search(word):
                self.__data.add_word(word)

    def analyze_chars(self, chars):
        for char in chars:
            if char.isalpha():
                self.__data.add_char(char)

    def analyze_line(self, line):
        self.analyze_words(line.split())
        self.analyze_chars(line)


class TextAnalyzerThread(threading.Thread):
    def __init__(self, parser, analyzer, line_count, name=None):
        super().__init__(name=name)
        self.__parser = parser
        self.__analyzer = analyzer
        self.__line_count = line_count

    def run(self):
        while True:
            lines = self.__parser.getlines(self.__line_count)
            if not lines:
                break;
            for line in lines:
                if line is None:
                    break
                #print("{}: {}".format(self.name, line))
                self.__analyzer.analyze_line(line)
        #print("{} exited".format(self.name))

def analyze_file(filename, thread_num, line_count):
    with open(filename) as filestream:
        parser = StreamParser(filestream)
        collectors = []

        # prepare analyzer threads
        for i in range(thread_num):            
            collector = DataCollector()
            collectors.append(collector)
            analyzer = TextAnalyzer(collector)
            thread = TextAnalyzerThread(parser, analyzer, line_count, name="Thread {}".format(i))
            thread.start()

        parser.wait()
        total = DataCollector.merge(collectors)
        total.print_stats()


def benchmark_file(filename):
    print("analyzing {0} ({1:.1f}M)".format(
        basename(filename),
        getsize(filename) / 1024 / 1024))
    t0 = time()
    analyze_file(filename, NUM_THREADS, LINES_PER_THREAD)
    t1 = time()
    print("Time taken: {0:.2f}s".format(t1 - t0))
    print()


if __name__ == "__main__":
    benchmark_file("../test_files/test.txt")
    benchmark_file("../test_files/bible.txt")
    benchmark_file("../test_files/quran-simple.txt")