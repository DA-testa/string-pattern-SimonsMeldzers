# python3

def read_input():
        file_type = input().strip()
        if file_type == 'F':
            # file_name = input()
            file_name = 'tests/06'

            # if 'a' in file_name:
            #     return
            # if 'tests/' not in file_name:
            #     file_name = 'tests/' + file_name
            with open(file_name, 'r') as f:
                pattern = f.readline().strip()
                text = f.readline().strip()

        elif file_type == 'I':
            pattern = input().strip()
            text = input().strip()

        return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9 + 9
    n = len(pattern)
    t = len(text)
    
    pattern_hash = 0
    for i in range(n):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m

    text_hash = 0
    for i in range(n):  
        text_hash = (text_hash * p + ord(text[i])) % m

    occurrences = []
    if pattern_hash == text_hash and pattern == text[:n]:
        occurrences.append(0)

    p_pow = pow(p, n-1, m)
    for i in range(1, t-n+1):
        text_hash = (text_hash - ord(text[i-1]) * p_pow) % m
        text_hash = (text_hash * p + ord(text[i+n-1])) % m

        if pattern_hash == text_hash and pattern == text[i:i+n]:
            occurrences.append(i)

    return occurrences



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

