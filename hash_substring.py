# python3

def read_input():
        file_type = input().strip()
        if file_type == 'F':
            file_name = input()

            if 'a' in file_name:
                return
            if 'tests/' not in file_name:
                file_name = 'tests/' + file_name
            with open(file_name) as f:
                pattern = f.readline().strip()
                text = input().strip()

        elif file_type == 'I':
            pattern = f.readline().strip()
            text = input().strip()
        else:
            return 'Error'

        return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9 + 9
    n = len(pattern)
    t = len(text)
    
    text_hash = 0
    for i in range(n):  
        text_hash = (text_hash * p + ord(text[i])) % m

    pattern_hash = 0
    for i in range(n):
        pattern_hash = (pattern_hash * p + ord(text[i])) % m

    occurrences = []
    if text_hash == pattern_hash and pattern == text[:n]:
        occurrences.append()

    for i in range(t-n+1):
        text_hash = ((text_hash - ord(text[i])) % m) * (p + ord(text(i+n)) % m)

        if pattern_hash == text_hash:
            occurrences.append(i)

    return occurrences



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

