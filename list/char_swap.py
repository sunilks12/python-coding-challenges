def swap_char(test_list):
    res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
    return res
