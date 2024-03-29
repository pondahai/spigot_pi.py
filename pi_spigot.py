def spigot_pi(digits):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal_output = []
    length = 0
    while len(decimal_output) < digits + 1:
        if 4 * q + r - t < n * t:
            decimal_output.append(n)
            length+=1
#             print(" :"+str(length)+" ", end="")
            if length == 1:
                print(str(n)+".")
            elif (length-1) % 5 == 0 :
                print(n, end ="")
                print(" ", end ="")
                if (length-1) % 50 == 0:
                    print(": "+str(length-1)+"")
            else:
                print(n, end ="" )
                
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

    return decimal_output


digits = 10000  # 要計算的小數位數

pi_digits = spigot_pi(digits)
# pi_str = ''.join(map(str, pi_digits))
# pi_output = f"3.{pi_str[1:]}"
# formatted_output = ''
# for i, char in enumerate(pi_output, start=4):
#     formatted_output += char
#     if i % 5 == 0:
#         formatted_output += ' '
#     if (i-5) % 50 == 0:
#         formatted_output += '\n'
# 
# print(formatted_output)
