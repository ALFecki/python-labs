from utilities import sentences_amount
from utilities import non_declarative_sentecnes
from utilities import split_to_words
from utilities import average_length
from utilities import average_words_len
from utilities import words_top
import os

def main():
    choose = int(input("Choose your inpur format: 1 - file, 2 - console input\n"))
    data = ""
    match choose:

        case 1:
            while not data:
                print("Files at directory: ", os.listdir())
                file_name = input("Enter file name: ")
                print(file_name)
                try:
                    file = open(file_name)
                except:
                    print("No such file in directory")
                    continue
                data = file.read()
    
        case 2:
            data = input("Enter your data: ")
        

    (sentences, count) = sentences_amount(data)
    print("Sentences amount = ", count)
    print("Non-declarative sentences amount = ", non_declarative_sentecnes(data))
    print("Average len of sentence is ", average_length(sentences))
    print("Average word len is ", average_words_len(sentences))
    print("Top 10 of 3-grams: ", words_top(sentences, 10, 3))



if __name__ == "__main__":
    main()