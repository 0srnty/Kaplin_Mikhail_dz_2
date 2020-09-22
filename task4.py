def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f"count - {n_count}, sum - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum+numb)


n = int(input())
recur_method(n)