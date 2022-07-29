# Inbukt methodes in oythone used on strings

# 1 Capitalize all letters

import email
from itertools import count


school = "Lelmokwo Boy's"
school = school.upper()
print(school)

# 2. change all letters to lower case

church = "St James Koromosho"

church_new = church.lower()
print(church_new)

# 3. using use case methode
Your_email = input("Enter your email: ")

Your_email = Your_email.lower()
print(Your_email)

# using a strip value
s = " hello"
print(s)
f = s.strip()
print(f)

# 4. methode count

full_name = "Sammy Kipkosgei"

name_count = full_name.count("m")
print(name_count)

# 5. concatinating stings

f_name = input("Input your first name: ")
l_name = input("Input your second name: ")

full_name = f_name + " " + l_name

print(full_name)

# .6 checking the leng of the string

v = "Hello there, My name is kcodev i'm learning programing"
l = len(v)
print(l)
