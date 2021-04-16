import json
from pathlib import Path
import difflib
from difflib import SequenceMatcher


### FUNCTIONS ####

def read_json(json_path):
    json_path = Path(json_path)
    if json_path.is_file():
        data = json.load(open(json_path))
        return data
    else:
        raise Exception("Specified json_path does not exist")


def translate(word):

    word = word.lower()
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        match = difflib.get_close_matches(
            word, data.keys(), n=1)[0]
        decision = input(
            f"Did you mean {match} instead? Press Y for Yes and N for No: ")
        if decision == "Y":
            return data[match]
        else:
            return "The word doesn't exist. Please, check it"
    else:
        return "The word doesn't exist. Please, check it"

# def read_file(myfile):
#     try:
#         data = json.load(open(myfile))
#         return data
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)


### SCRIPT ####
json_path = "13-english-thesaurus/data.json"
data = read_json(json_path)
word = input("Enter word: ")

outcome = translate(word)

if type(outcome) == list:
    for item in outcome:
        print(item)
else:
    print(outcome)
