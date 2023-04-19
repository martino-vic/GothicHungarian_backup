"""
Read the prepared input files and search for phonetic matches
between Gothic and Hungarian
"""
import csv

from loanpy.loanfinder import phonetic_matches

def main():
    """
    #. Import `loanpy.loanfinder.phonetic_matches
       <https://loanpy.readthedocs.io/en/latest/documentation.html#loanpy.loanfinder.phonetic_matches>`
    #. Read the input data
    #. Pass it on to loanpy
    #. End the function since loanpy writes the file

    """
    with open("raw/hungarian.tsv", "r") as f:
        hun = list(csv.reader(f, delimiter="\t"))
    with open("raw/gothic.csv", "r") as f:
        got = list(csv.reader(f))

    phonetic_matches(hun, got, "out/phonetic_matches.tsv")

if __name__ == "__main__":
    main()
