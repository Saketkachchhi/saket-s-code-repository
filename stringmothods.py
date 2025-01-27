a = "SAKEt study's CE in SVIT, Vasad...."

print(len(a))                                  #length of the string

print(a.lower())                               #convert to lowercase

print(a.upper())                               #convert to uppercase

print(a.capitalize())                          #capitalize the first letter

print(a.rstrip("."))                           #remove the last character

print(a.split(" "))                            #split the string into a list, using space as the separator

print(a.replace("CE", "Computer Engineering")) #replace the first substring with the second substring

print(a.count("s"))                            #count the number of occurrences of the substring

print(a.center(100))                           #center the string within a string of length 100

print(a.endswith("...."))                      #check if the string ends with the substring

print(a.endswith("Et", 0, 5))                  #check if the string ends with the substring within the specified range

print(a.find("study"))                         #find the index of the first occurrence of the substring

print(a.isalnum())                               #check if all characters are alphanumeric

print(a.isalpha())                               #check if all characters are alphabetic

print(a.islower())                               #check if all characters are lowercase

print(a.isupper())                               #check if all characters are uppercase

print(a.swapcase())                              #swap the case of the string

print(a.title())                                 #convert the string to title case