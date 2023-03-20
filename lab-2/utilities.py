import re

pattern_sentences = r'(?<!Mr)[\.|!|?]+\"*\s*(?!$)'
pattern_non_declarative = r'(?<!Mr)[|!|?]+\"*\s*(?!$)'

def sentences_amount(data: str):
    sentences = re.split(pattern_sentences, data)
    
    return (sentences, len(sentences))


def non_declarative_sentecnes(data: str):
    amount = re.search(pattern_non_declarative, data)
    return amount


# def average_length(sentences: list):
    
#     for sentence in sentences:
        
