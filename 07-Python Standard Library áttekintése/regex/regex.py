import re
# https: // regex101.com/

# 1.
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")

# 2.
text = 'Bello Banana Poopaye Po ka'
pattern = re.compile(r'\w')

num = pattern.findall(text)
print(num)

# []	A set of characters	"[a-m]"
# \	Signals a special sequence(can also be used to escape special characters)	"\d"
# .	Any character(except newline character)	"he..o"
# ^	Starts with "^hello"
# $	Ends with "planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or "falls|stays"
# ()	Capture and group

# \d - Matches any decimal digit; this is equivalent to the class [0-9].
# \D - Matches any non-digit character; this is equivalent to the class [^0-9].
# \s - Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
# \S - Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \w - Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# \W - Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
