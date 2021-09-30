from word_ladder import WordLadder

# Write appropriate unit tests


def test_constructor():
    """Test the constructor"""
    w1 = "aliened"
    w2 = "alienee"
    wordlist = {"aaaaaaa", "bbbbbbb", "aliened", "ccccccc", "alienee"}
    wl = WordLadder(w1, w2, wordlist)
    assert wl.wordlist == {"aaaaaaa", "bbbbbbb", "ccccccc", "alienee"}
    assert wl.beginWord == "aliened"
    assert wl.endWord == "alienee"
    assert wl.queue.items == [wl.stack]
    assert wl.stack.items == [w1]


def test_make_ladder():
    """Test the make_ladder method"""
    x1 = "aliened"
    x2 = "alienee"
    wordlist = {"aaaaaaa", "bbbbbbb", "aliened", "ccccccc", "alienee"}
    wl = WordLadder(x1, x2, wordlist)
    assert wl.make_ladder() == [x1, x2]
