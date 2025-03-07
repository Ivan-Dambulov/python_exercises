N = int(input())
M = int(input())
S = int(input())


valid_addresses = []


for address in range(M, N - 1, -1):

    if address % 2 == 0 and address % 3 == 0:

        if address == S:
            break
        valid_addresses.append(address)


print(" ".join(map(str, valid_addresses)))
