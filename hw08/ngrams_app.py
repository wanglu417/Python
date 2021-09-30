import sys
from ngramfrequencies import NgramFrequencies


def main(file_name):
    """Handle the ngrams-counts-related work"""
    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return
    f1 = f.read()
    unigf = NgramFrequencies()
    bigf = NgramFrequencies()
    trigf = NgramFrequencies()
    unigf.add_item(f1, 1)
    bigf.add_item(f1, 2)
    trigf.add_item(f1, 3)
    print("Top 10 unigrams: ")
    for i in unigf.frequency:
        print(' '*2, i)
    print("Top 10 biigrams: ")
    for i in bigf.frequency:
        print(' '*2, i)
    print("Top 10 trigrams: ")
    for i in trigf.frequency:
        print(' '*2, i)


main(sys.argv[1])
