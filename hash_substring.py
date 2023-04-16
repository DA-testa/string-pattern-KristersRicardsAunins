#221RDC033
def read_input():
    input_type = input().strip().upper()
    if input_type == 'F:
        input_f = "06"
        if 'a' in input_f:
            return
        input_f = "tests/" + input_f
        with open(input_f) as file:
            fred = file.readline()
            txt = file.readline()
    elif input_type == 'I:
        fred = input()
        txt = input()
    else:
        return
    return (fred, txt)

def print_occurrences(output):
   print(*output, sep=' ')

def get_occurrences(pattern, text):
    hush = []
    numb = []
    def find_letter(input_type):
        for i in range(len(hush)):
            if (input_type == hush[i][0]):
                return hush[i][1]
        return(-1)
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
