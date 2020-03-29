#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    upper_s = s.upper()
    result = []
    for idx, char in enumerate(upper_s):
        result.append(char + char.lower()*(idx))
    return '-'.join(result)
print(accum('ZpglnRxqenU'))
