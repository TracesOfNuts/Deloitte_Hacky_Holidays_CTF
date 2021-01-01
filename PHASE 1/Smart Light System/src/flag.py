with open('hex.txt', 'r') as file:
    lines = file.readlines()
    #print('lines:', lines)
    
    # remove all `\n` characters
    x = [lines[i].replace('\n','') for i in range(len(lines))]
    #print('x:\n', x)
    
    # set flag length
    fl = len(lines)//2
    
    # create 2 hex list variables
    hex_at_rbp_90 = x[:fl]
    hex_at_rbp_50 = x[fl:]
    #print('hex_at_rbp_90:\n', hex_at_rbp_90, '\n')
    #print('hex_at_rbp_90:\n', hex_at_rbp_50, '\n')
    
    # converts the hex to bin
    binA = [int(i,16) for i in hex_at_rbp_90]
    binB = [int(i,16) for i in hex_at_rbp_50]
    #print('binA:\n', binA, '\n')
    #print('binB:\n', binB, '\n')
    
    # perform XOR operation
    xor = [binA[i]^binB[i] for i in range(fl)]
    #print('xor:', xor)
    
    # convert back to ASCII
    flag_list = [xor[i].to_bytes((xor[i].bit_length() + 7) // 8, 'big').decode() for i in range(fl)]
    #print('flag_list:', flag_list)
    
    # combine the list of characters to get the flag
    flag = ''
    for i in flag_list:
        flag += i
    print(flag)