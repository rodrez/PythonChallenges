import string
import re

def is_pangram(s):

    return ''.join(sorted(set(re.sub(r'[^a-zA-Z]', "", s).lower()))) == string.ascii_lowercase
