from utilities import sentences_amount
from utilities import non_declarative_sentecnes
from utilities import split_to_words
from utilities import average_length
from utilities import average_words_len
from utilities import words_top

def main():
    data = "Do commanded an shameless we disposing do too. Indulgence ten remarkably nor are impression out. Mr. Johnson provision an in intention out. Saw supported too joy promotion engrossed propriety."
    (sentences, count) = sentences_amount(data)
    print("Sentences amount = ", count)
    print("Non-declarative sentences amount = ", non_declarative_sentecnes(data))
    print("Average len of sentence is ", average_length(sentences))
    print("Average word len is ", average_words_len(sentences))
    print("Top 10 of 3-grams: ", words_top(sentences, 10, 3))



if __name__ == "__main__":
    main()