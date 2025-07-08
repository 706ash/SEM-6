def binary_xor_division(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
        
    l = b.bit_length()
    if a.bit_length() < l:
        return a
    
    s = a.bit_length() - l
    r = a >> s
    
    for i in range(s - 1, -1, -1):
        if (r >> (l - 1)) & 1:
            r ^= b
        r = (r << 1) | ((a >> i) & 1)
    
    if (r >> (l - 1)) & 1:
        r ^= b
    
    return r & ((1 << (l - 1)) - 1)

while True:
    print("\n=== CRC ===")

    # Sender Side
    print("\n--Sender--")
    get_message = input("Enter message: ")
    get_divisor = input("Enter divisor: ")

    count = len(get_divisor) - 1
    adjusted_message = get_message + '0' * count
    print(f"Dividend after adjustment: {adjusted_message}")

    dividend = int(adjusted_message, 2)
    divisor = int(get_divisor, 2)

    remainder = binary_xor_division(dividend, divisor)
    crc_length = len(get_divisor) - 1
    crc_str = format(remainder, f'0{crc_length}b')

    print(f"CRC: {crc_str}")

    transmitted_message = get_message + crc_str
    print(f"Final message transmitted: {transmitted_message}")

    # Receiver Side
    print("\n--Receiver--")
    receiver_input = input("Has the message changed? (y/n): ")

    if receiver_input.lower() == 'y':
        whichbit = int(input("Which bit has an error? (1-indexed): "))
        message_list = list(transmitted_message)
        # Flip the specified bit
        index = whichbit - 1
        message_list[index] = '1' if message_list[index] == '0' else '0'
        transmitted_message = ''.join(message_list)

        dividend = int(transmitted_message, 2)
        remainder = binary_xor_division(dividend, divisor)
        crc_result = format(remainder, f'0{crc_length}b')

        print(f"Message received: {transmitted_message}")
        print(f"CRC: {crc_result}")
        print("Error Detected")
    else:
        dividend = int(transmitted_message, 2)
        remainder = binary_xor_division(dividend, divisor)
        crc_result = format(remainder, f'0{crc_length}b')

        print(f"Message received: {transmitted_message}")
        print(f"CRC: {crc_result}")
        print("No Error")

    print("------------------------------------------------------------")
