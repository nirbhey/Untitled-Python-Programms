import textwrap
s = "This is a very very very very very very very very very long string"

print(textwrap.fill(s, 7),) # The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph
print(textwrap.wrap(s, 7)) # The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. It returns a list of output lines.