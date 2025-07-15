def compute_lps(pattern):
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # Vị trí xuất hiện
        elif i < len(text) and pattern[j] != text[i]:
            j = lps[j-1] if j != 0 else 0
    return -1

print(kmp("ababcabcabababd", "ababd"))  # Output: 10
