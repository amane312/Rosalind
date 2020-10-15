def character_table(t):

    if len (t[0]) < 1:
        return None
        
    if len(t) < 2:
        return None
    
    char = [[0 for i in t]]
    
    taxa = [[0], []]
    
    for i in range(1, len(t)):
        if t[i][0] == t[0][0]:
            taxa[0].append(i)
        else:
            taxa[1].append(i)
            
    if taxa[1] == []:
        return None
    
    a, b = [[], []]
    for i in taxa[0]:
        char[0][i] = 1
        a.append(t[i][1:])
    for j in taxa[1]:
        b.append(t[j][1:])
    
    row1 = character_table(a)
    if row1 != None:
        for i in row1:
            char.append(i)
            
    row2 = character_table(b)
    if row2 != None:
        for j in row2:
            char.append(j)
    
    return char
    
    
def main():
    with open('./rosalind_cstr.txt', 'r') as infile:
        strings = infile.read().strip().split('\n')
    
    answer = character_table(strings)
    
    print('\n'.join([''.join(map(str, answer[i])) for i in range(len(answer))]))
    
if __name__ == '__main__':
    main()