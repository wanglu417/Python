from textcleaner import TextCleaner


class NgramFrequencies:
    """Handle counts and frequency calculation of words"""
    # Initialize internal attributes to their start values

    def __init__(self):
        self.gram_counts = {}
        self.total_count = 0

    def add_item(self, gram_list, n_gram):
        """Add an item to the count"""
        list0 = TextCleaner()
        list1 = list0.clean(gram_list)
        if n_gram == 1:
            for gram in list1:
                if gram[-1] == '.' and gram != 'mr.' and gram != 'dr.':
                    if gram[0:-1] in self.gram_counts.keys():
                        self.gram_counts[gram[0:-1]] += 1
                    else:
                        self.gram_counts[gram[0:-1]] = 1
                else:
                    if gram in self.gram_counts.keys():
                        self.gram_counts[gram] += 1
                    else:
                        self.gram_counts[gram] = 1
                self.total_count += 1
        else:
            list2 = []
            i = 0
            while i < len(list1)-n_gram+1:
                temp = ''
                flag1 = 0
                flag2 = 0
                for j in range(n_gram):
                    if list1[i+j][-1] != '.' or list1[i+j] == 'mr.' or\
                            list1[i+j] == 'dr.':
                        temp = temp+'_'+list1[i+j]
                    else:
                        if j != n_gram-1:
                            flag1 = 1
                            break
                        else:
                            flag2 = 1
                            temp = temp+'_'+list1[i+j][0:-1]
                if flag1 != 1:
                    list2.append(temp[1:])
                    if flag2 != 1:
                        i += 1
                    else:
                        i = i+j+1
                else:
                    i = i+j+1
            for gram in list2:
                if gram in self.gram_counts.keys():
                    self.gram_counts[gram] += 1
                else:
                    self.gram_counts[gram] = 1
                self.total_count += 1

    @property
    def top_n_counts(self):
        """Return a list of items sorted on the count"""
        return sorted(
            self.gram_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @property
    def frequency(self):
        """Takes an item and returns its frequency"""
        return sorted({key: round(self.gram_counts[key]/self.total_count, 3)
                       for key in self.gram_counts.keys()}.items(),
                      key=lambda x: x[1], reverse=True)[0:10]
