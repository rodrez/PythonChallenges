import re

email_validation = re.compile(r'''([a-zA-Z0-9._&=-] + @[a-zA-Z0-9.-]+(\.[a-zA-Z] (2,4)))''', re.VERBOSE)

# a-z is the same as typing the whole alphabet
# ^ -caret [^5] will match any character except '5'. If the caret appears elsewhere,
# it does not have any special meaning
# If you need to match [ or \, we can precede them with \[ or \\.
# \w matches any alphanumeric character. Is equivalent to [a-zA-Z0-9_]

