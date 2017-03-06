import text_analyzer
import cProfile

cProfile.run('text_analyzer.analyze_file("../test_files/bible.txt", 10, 50000)')