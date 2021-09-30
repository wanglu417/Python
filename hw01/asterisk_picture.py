def pyramid(n):
    for i in range(1,n+1):
        numwhite = n-i
        print(' '*numwhite + '*'*i + '*'*i)
    for i in range(1,n+1):
        numwhite = n-i
        print(' '*numwhite + '*'*i + '*'*i) 
    numwhite = n-1
    print(' '*numwhite + '*'*1 + '*'*1)
    numwhite = n-1
    print(' '*numwhite + '*'*1 + '*'*1) 
    numwhite = n-1
    print(' '*numwhite + '*'*1 + '*'*1) 
    numwhite = n-1
    print(' '*numwhite + '*'*1 + '*'*1) 
row = int(input('number of rows: '))
pyramid(row)
