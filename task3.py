def recur_method(numb, flip=0):
    if numb == 0:
        return flip
    else:
        flip = (flip * 10) + (numb % 10)
        numb = numb // 10
        return recur_method(numb, flip)


n = int(input())
recur_method(n)