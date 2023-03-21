import re
from collections import defaultdict

pattern_sentences = r'(?<!Mr)[\.|!|?]+[\"|\“|\”]*\s*(?!$)'
pattern_non_declarative = r'(?<!Mr)[|!|?]+\"*\s*(?!$)'
pattern_to_words = r"(\w+)"

def sentences_amount(data: str):
    sentences = re.split(pattern_sentences, data)
    
    return (sentences, len(sentences))


def non_declarative_sentecnes(data: str):
    amount = re.search(pattern_non_declarative, data)
    return amount


def split_to_words(sentence: str):
    words = re.findall(pattern_to_words, sentence)
    for word in words:
        if word.isdigit():
            words.remove(word)
    return words
    

def average_length(sentences: list):
    (_, character_count) = words_and_char_amount(sentences)
    return character_count / len(sentences)

def words_and_char_amount(sentences: list):
    character_count = 0
    words_count = 0
    for sentence in sentences:
        words = split_to_words(sentence)
        words_count += len(words)
        character_count += sum([len(word) for word in words])
    return (words_count, character_count)
    

def average_words_len(sentences: list):
    (words_count, char_count) = words_and_char_amount(sentences)
    return char_count / words_count

        
def words_top(sentences: list, top_len = 10, word_len = 4):
    top = defaultdict(int)
    for sentence in sentences:
        words = split_to_words(sentence)
        for word in words:
            if len(word) == word_len:
                top[word] += 1
    sorted_top = dict(sorted(top.items(),key=lambda item:item[1], reverse=True))
    while len(sorted_top) > top_len:
        sorted_top.popitem()

    return sorted_top

