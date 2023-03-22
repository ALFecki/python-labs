from utilities import sentences_amount
from utilities import non_declarative_sentecnes
from utilities import split_to_words
from utilities import average_length
from utilities import words_and_char_amount
from utilities import average_words_len
from utilities import words_top



def test_sentences_amount():
    text = "Power is lived means oh every in we quiet. Mr. Johnson provision an in intention. Saw supported too joy promotion engrossed propriety."

    expected_sentences = ["Power is lived means oh every in we quiet", "Mr. Johnson provision an in intention", "Saw supported too joy promotion engrossed propriety"]
    expected_amount = len(expected_sentences)

    assert((expected_sentences, expected_amount)) == sentences_amount(text)


def test_non_declarative_sentecnes():
    text = "Power is lived means oh every in we quiet! Mr. Johnson provision an in intention. Saw supported too joy promotion engrossed propriety."

    expected_amount = 1

    assert(expected_amount) == non_declarative_sentecnes(text)

def test_split_to_words():
    text = "Power is lived means oh every in we quiet."

    expected_words = ["Power", "is", "lived", "means", "oh", "every", "in", "we", "quiet"]

    assert(expected_words) == split_to_words(text)

def test_average_length():
    text = "Power is lived means oh every in we quiet! Mr. Johnson provision an in intention."
    expected_average = 32

    assert(expected_average) == average_length(sentences_amount(text)[0])

def test_words_and_char_amount():
    text = "Power is lived means oh every in we quiet! Mr. Johnson provision an in intention."
    expected_word_num = 15
    expected_char_num = 64

    assert((expected_word_num, expected_char_num)) == words_and_char_amount(sentences_amount(text)[0])

def test_average_words_len():
    text = "Power is lived meeans oh every in we quietly!"

    expected_amount = 4
    assert(expected_amount) == average_words_len(sentences_amount(text)[0])

def test_words_top():
    text = "Power is lived means oh every in we quiet! Mr. Johnson provision an in intention."

    expected_top = {'in': 2, 'is': 1}

    assert(expected_top) == words_top(sentences_amount(text)[0], 2, 2)