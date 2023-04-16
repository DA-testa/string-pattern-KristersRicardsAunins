#221RDC033
def read_input():
    input_type = input().strip().upper()
    if input_type == 'F':
        input_f = "tests/06" #File Path
        with open(input_f) as file:
            pattern = file.readline() #First line
            text = file.readline() #Second line
    elif input_type == 'I':
        pattern = input()
        text = input()
    return (pattern, text)

def print_occurrences(output):
   print(*output, sep=' ')

def get_occurrences(pattern, text):
    hush = [] #To store hash values
    numb = [] #To store the rolling hash values
    def find_letter(input_type):
        for i in range(len(hush)):
            if (input_type == hush[i][0]):
                return hush[i][1]
        return(-1) #If hash value is not in the table then return -1
    q = len(pattern) - 1
    w = len(text)
    e = 100**(q - 1)
    n = 0
    for i in range(q):
        n *= 100
        r = find_letter(text[i])
        if(r != -1):
            n += r
        else:
            hush.append([text[i], len(hush) + 1])
            n += len(hush)
    numb.append(n)
    for i in range(q, w):
        r = find_letter(text[i - q])
        n -= e * r
        n *= 100
        r = find_letter(text[i])
        if(r != -1):
            n += r
        else:
            hush.append([text[i], len(hush) + 1])
            n += len(hush)
        numb.append(n)
    n = 0
    for i in range(q):
        n *= 100
        r = find_letter(pattern[i])
        if(r != -1):
            n += r
        else:
            return[-1]
    y = []
    for i in range(len(numb)):
        if n == numb[i]:
            y.append(i)
    return y
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
