def recur_method(numb, s=0, m=1):
    if s == m:
        print(f"answer: {s == m}")

    elif s < m:
        return recur_method(numb, s+1, numb * (numb + 1) // 2)


n = int(input())
recur_method(n)