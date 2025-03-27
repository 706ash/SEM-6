def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    return tmp

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword, remainder

def receiver(codeword, key):
    remainder = mod2div(codeword, key)
    return remainder

# User Inputs
message = input("Enter message: ")
divisor = input("Enter divisor: ")

# Sender Side
print("\n--Sender--")
print(f"Enter message: {message}")
print(f"Enter divisor: {divisor}")
appended_message, crc = encodeData(message, divisor)
print(f"Dividend after adjustment: {message}{'0'*(len(divisor)-1)}")
print(f"CRC: {crc}")
print(f"Final message transmitted: {appended_message}")

# Receiver Side
print("\n--Receiver--")
has_changed = input("Has the message changed? (y/n): ")
if has_changed.lower() == 'y':
    error_bit = int(input("Which bit has an error? (1-indexed): ")) - 1
    received_message = list(appended_message)
    received_message[error_bit] = '1' if received_message[error_bit] == '0' else '0'
    received_message = ''.join(received_message)
else:
    received_message = appended_message

print(f"Message received: {received_message}")
received_crc = receiver(received_message, divisor)
print(f"CRC: {received_crc}")

if '1' in received_crc:
    print("Error detected.")
else:
    print("No error.")