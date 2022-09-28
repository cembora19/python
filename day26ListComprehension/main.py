import pandas
#{new_key:new_value for (index,row) in df.iterrows()}
#TODO 1. create a dictionary in this format:
#{"a: "alfa", "b": "bravo"}
#TODO 2. create a list of the phonetic code words forma a word that user inputs.
PATH="day26ListComprehension\\tr_alphabet.csv"

data=pandas.read_csv(PATH)
tr_data_frame={row.letter:row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    word=input("Enter a word: ").upper()
    try:
        list=[tr_data_frame[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list)
generate_phonetic()