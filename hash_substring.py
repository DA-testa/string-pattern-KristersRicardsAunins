# python3
import os

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()[0]
    if input_type == 'F':
        ievad = "06"
        if 'a' in ievad:
            return
        ievad = "tests/" + ievad
        with open(ievad) as file:
            pattern = file.readline()
            txt = file.readline()
    elif input_type == 'I':
        pattern = input()
        txt = input()
    else:
        return
    return (pattern, txt)
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(*output, atd = " ")

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    hash = []
    cip = []
    def atrast_burty(input_type):
        for i in range(len(hash)):
            if (input_type == hash[i][0]):
                return hash[i][1]
        return(-1)
    k = len(pattern)-1
    j = len(text)
    l = 100**(n-1)
    n = 0
    for i in range (n):
        n *= 100
        t = find_letter(txt[i])
        if(t!=-1):
            n+=t
        else:
            hash.append([text[i], len(hash)+1])
            n+=len(hash)
    n.append(n)
    # and return an iterable variable
    #return [0]
    
# this part launches the functions
if __name__ == '__main__':
    input_data = read_input()
    if input_data is not None:
        pattern, text = input_data
        occurrences = get_occurrences(pattern, text)
    print_occurrences(get_occurrences(*read_input()))

