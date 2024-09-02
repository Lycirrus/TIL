def comb(lng):
    case = []

    def comb_in(v, l, case):
        if len(case) == 2:
            com_lst.append(case[:])
            return
        else:
            for u in range(v, l):
                case.append(u)
                comb_in(u + 1, l, case)
                case.pop()
    comb_in(0, lng, case)


def get_price(v, cng, lng, amx):
    global max_price
    if v == cng:
        int_num = int(''.join(num_lst))
        max_price = max(max_price, int_num)
        return
    else:
        for u in range(lng):
            if tf[u]:
                change = com_lst[u]
                tf_idx = tf.index(False)
                tf[tf_idx] = True
                tf[u] = False
                num_lst[change[0]], num_lst[change[1]] = num_lst[change[1]], num_lst[change[0]]
                get_price(v + 1, cng, lng, amx)
                num_lst[change[0]], num_lst[change[1]] = num_lst[change[1]], num_lst[change[0]]
            else:
                get_price(v + 1, cng, lng, amx)
                tf_idx = tf.index(False)
                tf[tf_idx] = True
                tf[u] = False


T = int(input())
for tc in range(1, T + 1):
    num, cng = input().split()
    cng = int(cng)

    max_price = 0
    num_lst = list(num)
    num_len = len(num_lst)

    com_lst = []
    comb(num_len)

    sort_num_lst = sorted(num_lst, reverse=True)
    all_max = int(''.join(sort_num_lst))
    tf = [True] * len(com_lst)
    get_price(0, cng, len(com_lst), all_max)

    print(f'#{tc} {max_price}')
