## CREATE

first_name = "Camilo" # double  quotes
last_name = 'Torres' # single quotes
scaping_text = 'doesn\'t' # use \' to escape the single quote...
using_numbers = 3 * 'un' + 'ium' # Concatenating with the + operator, and repeating with * (unununium)
full_name = first_name + last_name # Create a str using concatenation
input_str = input('What is your favorite food') # Create a str using an input
text = ('Put several strings within parentheses ' 'to have them joined together.') # Two or more string literals next to each other are automatically concatenated

## READ
text_test = 'Hello World!!! I\'m using Python'

size = len(text_test) # Length of 'text_test'
print(full_name) # Print a str in console
print('Javascript' in text_test) # Search for Javascript in 'text_test'
print(text_test.count('A')) # How many times appears 'A' in 'text_test'
print(text_test.startswith('Hell')) # Validate if 'text_test' starts with 'Hell'
print(text_test.endswith('Hell')) # Validate if 'text_test' ends with 'Hell'
print(text_test[2]) # Shows the letter that is on key = 2
print(text_test[size - 1]) # Shows 'text_test' from right to left
print(text_test[-1]) # Shows the last index of 'text_test'
print('C:\some\name') # here \n means newline!
print(r'C:\some\name')  # note the r before the quote (raw strings)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

full_name = first_name + ' ' + last_name # Concatenating 2 str
template_one = f"Hi, my first name is {first_name} and my last name is {last_name}" # Using format
template_two = "Hi, my first name is {} and my last name is {}".format(first_name, last_name) # Using format

## UPDATE

print(template_one.upper())
print(template_one.lower())
print(template_one.capitalize())
print(template_one.title())
print(template_one.swapcase())
print(template_one.replace('Anita', 'Carlos'))
print(template_one[0:9])
print(template_one[:9])
print(template_one[::-1])