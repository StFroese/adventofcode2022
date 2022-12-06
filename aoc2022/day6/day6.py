def read_input():
    with open('input.txt', 'r') as f:
        line = f.read()[:-1]
    return line

def main():
    input = read_input()

    # part 1
    res = next((i+4 for i,a,b,c,d in zip(range(len(input)), input,input[1:],input[2:],input[3:]) if len(set([a,b,c,d])) == 4), None)
    print(res)

    # part 2 (this can be done more beautiful but I don't have time today...)
    res = next((i+14 for i,a,b,c,d,e,f,g,h,j,k,l,m,n,p in zip(range(len(input)), input, input[1:], input[2:], input[3:], input[4:], input[5:], input[6:], input[7:], input[8:], input[9:], input[10:], input[11:], input[12:], input[13:]) if len(set([a,b,c,d,e,f,g,h,j,k,l,m,n,p])) == 14), None)
    print(res)

if __name__ == '__main__':
    main()
