#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# def decryptPassword(s):
#     #first extract digits
#     password = []
    
#     digits = []
#     last_digit_index = 0
#     for i in s:
#         if (i.isdigit() and i !='0'):
#             digits.append(i)
#             last_digit_index +=1
#     s = s[last_digit_index:]
#     #digits.sort(reverse=True)
    
    
#     i = 0
#     while(i < len(s)):
#         if(s[i].isupper() and s[i+1].islower() and s[i+2].isupper()):
#             password.append(s[i+1])
#             password.append(s[i])
#             i+=3
#             continue
        
#         if s[i] == '0':
#             password.append(digits[-1])
#             digits.pop()
#             i+=1
#             continue
        
#         if s[i] != '0':
#             password.append(s[i])
#             digits.pop()
#             i+=1
#             continue

def decryptPassword(s):
    digits = []
    chars = list(s)
    
    for i in range(len(chars)):
        if chars[i].isdigit() and chars[i] != '0':
            digits.append(chars[i])
            chars[i] = ''  # Mark digit positions to be removed

    result = []
    i = 0
    while i < len(chars):
        if i + 2 < len(chars) and chars[i].isupper() and chars[i+1].islower() and chars[i+2] == '*':
            # Swap and remove '*'
            result.append(chars[i+1])
            result.append(chars[i])
            i += 3
        elif chars[i] == '0':
            result.append(digits.pop()) 
            i += 1
        else:
            result.append(chars[i])
            i += 1
    
    return ''.join(result)

 
text = "51Pa*0Lp*0e"
print(decryptPassword(text))       