from ngramfrequencies import NgramFrequencies


def test_constructor():
    """Test the constructor"""
    ngf = NgramFrequencies()
    assert ngf.gram_counts == {}
    assert ngf.total_count == 0


def test_add_item():
    """Test the add item method"""
    ngf1 = NgramFrequencies()
    gram_list = 'Hello World.'
    ngf1.add_item(gram_list, 1)
    assert ngf1.total_count == 2


def test_top_n_counts():
    """Test the top_n_counts constructor"""
    ngf2 = NgramFrequencies()
    gram_list = 'Hello World Hello Hello World'
    ngf2.add_item(gram_list, 1)
    ngf2.top_n_counts
    assert ngf2.top_n_counts[0][0] == 'hello'
    assert ngf2.top_n_counts[0][1] == 3
    assert len(ngf2.top_n_counts) == 2


def test_frequency():
    """Test the frequency constructor"""
    ngf3 = NgramFrequencies()
    gram_list = 'Hello World Hello Hello World'
    ngf3.add_item(gram_list, 1)
    assert ngf3.frequency[0][1] == round(3/5, 3)
    ngf4 = NgramFrequencies()
    ngf4.add_item(gram_list, 2)
    assert ngf4.frequency[0][1] == round(2/4, 3)
