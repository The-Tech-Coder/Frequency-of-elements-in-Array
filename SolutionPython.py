def frequency(arr):
    freq = [None] * len(arrstring)
    done = -1
    for i in range(len(arrstring)):
        count = 1
        for j in range(i+1, len(arrstring)):
            if(arrstring[i] == arrstring[j]):
                count = count + 1
                freq[j] = done

            if(freq[i] != done):
                freq[i] = count

    print("Element - Frequency")
    for i in range(len(freq)):
        if(freq[i] != done):
            print(" " + str(arrstring[i]) + " - " + str(freq[i]))

arrstring = [1, "a", "a", 2, 3, "b", 3, "b", 2, "b", 4, 2]
frequency(arrstring)
