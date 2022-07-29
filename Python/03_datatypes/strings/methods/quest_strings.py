# question 1 Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
# name = “  JOHn  .“ to “john”


name = "JOHn"

name_n = name.casefold()
print(name_n)


#  question 2 Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

sentence_one = "The Dog Breed is German Shepherd"

sentence_one_slice = sentence_one[8:23]
print(sentence_one_slice)

# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"

sentence_two_slice = sentence_two[16:30]
print(sentence_two_slice)

# Split the below sentence using ; “The lazy dog; ran so fast; it hit the wall.” And display length of the result.

sentence_three = "The lazy dog; ran so fast; it hit the wall."

sentence_three_split = sentence_three.split(";")
print(len(sentence_three_split))

print(sentence_three_split)
