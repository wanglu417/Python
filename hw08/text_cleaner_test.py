from textcleaner import TextCleaner


def test_clean():
    """Test the clean method"""
    tc = TextCleaner()
    s = ' '
    assert s.join(tc.clean('Hello "WORLD", My name is (ADA).')
                  ) == 'hello world COMMA my name is ada.'
