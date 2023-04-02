# python3
import os

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()
    if input_type == 'F':
        fails = input()
        atrasanas = './tests/'
        faila_vieta = os.path.join(atrasanas, fails)
        with open(faila_vieta, mode="r") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    elif input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    else:
        print("error")
    return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p =31
    m = len(pattern)
    n = len(text)
    p_pow = [1] * (n - m + 1)
    for i in range(1, n - m + 1):
        p_pow[i] = (p_pow[i - 1] * p) % (10**9 + 9)
    pattern_hash = 0
    text_hash = 0
    for i in range (m):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * p_pow[m - i - 1]) % (10**9 + 9)
        text_hash = (text_hash + (ord(text[i]) - ord('a') + 1) * p_pow[m - i -1]) % (10**9 + 9)
    occurrences= []
    for i in range(n - m + 1):
        if pattern_hash == text_hash and pattern == text[i:i + m]:
            occurrences.append(i)
        if i < n - m:
            text_hash = (text_hash - (ord(text[i]) - ord('a') + 1) * p_pow[m - 1]) % (10**9 + 9)
            text_hash = (text_hash * p + (ord(text[i + m]) - ord('a') + 1)) % (10**9 + 9)
            text_hash = (text_hash + (10**9 + 9)) % (10**9 + 9)
            return occurrences
    # and return an iterable variable
    #return [0]


# this part launches the functions
if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))

