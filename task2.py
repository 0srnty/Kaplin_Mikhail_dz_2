def recur_method(numb, even=0, odd=0):
    if numb == 0:
        return even, odd
    else:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            even += 1
            return recur_method(numb, even, odd)
        else:
            odd += 1
            return recur_method(numb, even, odd)


n = int(input())
recur_method(n)