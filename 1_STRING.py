#strings methods
a="shruti pralhad chaudhari"
print(a.capitalize()) #Converts the first character to upper case
print(a.casefold())   #Converts string into lower case
print(a.center(50))    #Returns a centered string #string.center(length, character)
print(a.count("i"))    #method returns the number of times a specified value appears in the string.

print(a.encode())  #Returns an encoded version of the string
print(a.endswith("i")) #Returns true if the string ends with the specified value
print(a.startswith("s"))
print(a.expandtabs())  #Sets the tab size of the string
print(a.find("h")) #Searches the string for a specified value and returns the position of where it was found
print(a.format()) #Formats specified values in a string
print(a.format_map)  #Formats specified values in a string
print(a.index("shruti")) #Searches the string for a specified value and returns the position of where it was found
print(a.isalnum()) #method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(a.isalpha()) #Returns True if all characters in the string are in the alphabet
