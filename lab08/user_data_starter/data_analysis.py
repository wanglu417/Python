import re


class DataAnalysis:

    def __init__(self):
        """set up the necessary instance variables"""
        self.lang_counts = {}
        self.email_counts = {}
        self.total_lang_counts = 0
        self.total_email_counts = 0

    def read_data(self, file_name):
        """read the data and generate a list comprehension"""
        f = open(file_name)
        f1 = f.readlines()
        result = []
        for line in f1:
            result.append(list(line.strip('\n').split(',')))
        return result

    def add_lang_item(self, list):
        """Add an item to the language counts"""
        for item in list:
            if item[6] in self.lang_counts.keys():
                self.lang_counts[item[6]] += 1
            else:
                self.lang_counts[item[6]] = 1
            self.total_lang_counts += 1

    def top_n_lang(self, N):
        """return a list of tuples of top N languages"""
        return sorted(self.lang_counts.items(),
                      key=lambda x: x[1],
                      reverse=True
                      )[0:N]

    def top_n_lang_freqs(self, N):
        """Return frequencies of top languages in the data"""
        return sorted(
            {key: round(self.lang_counts[key]/self.total_lang_counts, 3)
             for key in self.lang_counts.keys()}.items(),
            key=lambda x: x[1], reverse=True)[0:N]

    def add_tlds_item(self, f1):
        """Add tlds item to the country counts"""
        result = []
        result2 = []
        for line in f1:
            result.append(list(line.strip('\n').split(',')))
        email_list = []
        for i in range(len(result)):
            email_list.append(result[i][3])
        for i in email_list:
            tlds = re.findall(r"\.\w{2}(?!\.)\b", i)
            self.total_email_counts += 1
            if len(tlds) != 0:
                result2.append(tlds)
        for item in result2:
            if item[0][1:3] in self.email_counts.keys():
                self.email_counts[item[0][1:3]] += 1
            else:
                self.email_counts[item[0][1:3]] = 1

    def top_n_email(self, N):
        """Return top N emails with tlds"""
        return sorted(self.email_counts.items(),
                      key=lambda x: x[1],
                      reverse=True
                      )[0:N]

    def top_n_email_freqs(self, N):
        """Return frequencies of top N emails with tlds"""
        return sorted(
            {key: round(self.email_counts[key]/self.total_email_counts, 3)
             for key in self.email_counts.keys()}.items(),
            key=lambda x: x[1], reverse=True)[0:N]
