# Generate all permutations for caesar cipher

cipher = input("Enter the cipher: ")

for i in range(26):
    print(i , end="")
    for j in cipher:
        if ord(j)+i >90:
            print(chr(ord(j)+i - 26), end="")
        else:
            print(chr(ord(j)+i), end="")
    print("")

