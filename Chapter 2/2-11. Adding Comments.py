#   This program is about stripping Names.

name = "        \t  Arun         \n           "
print(name)
print(name.lstrip())    #.lstrip() strips the left spaces.
print(name.rstrip())    #.rstrip() strips the right spaces.
print(name.strip())     #.strip() strips both left and right spaces.

#   This program is about printing name in different cases.
name  ="Arun"
print(name.lower())     #.lower() lowers all the characters.
print(name.upper())     #.upper() capitalizes all the characters.
print(name.title())         #.title() capitalize only the first letter.