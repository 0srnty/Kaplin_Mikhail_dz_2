def recur_method(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f'{i} - {chr(i)} '
    print(output_str)
    if to_symbol < LAST_ASCII_NUM:
        return recur_method(from_symbol + STEP, to_symbol + STEP)


first_ascii_num = 32
LAST_ASCII_NUM = 127
STEP = 10
recur_method(first_ascii_num, first_ascii_num + STEP)