import sys
from data_analysis import DataAnalysis


def main(file_name):
    print_output(file_name)


def print_output(file_name):
    data1 = DataAnalysis()
    data2 = DataAnalysis()
    list1 = data1.read_data(file_name)
    data1.add_lang_item(list1)
    f = open('users.csv')
    f1 = f.readlines()
    data2.add_tlds_item(f1)
    """Report top ten languages by frequency"""
    print("Languages:")
    for i in data1.top_n_lang_freqs(10):
        print(i[0]+":  \t", i[1])
    """Report top ten country (2 letter) top level domains by frequency"""
    print("Top level country domains:")
    for i in data2.top_n_email_freqs(10):
        print(i[0]+":  \t", i[1])


main(sys.argv[1])
