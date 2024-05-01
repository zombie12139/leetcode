import bisect

def is_sub_sequence(source: str, target: str) -> int:
    if target == 0:
        return 0

    index = dict()   # 索引
    for i, ch in enumerate(source):
        if ch in index:
            index[ch].append(i)
        else:
            index[ch] = [i]
    i = -1
    ret = 1
    for ch in target:
        if ch not in index:
            return -1
        next_i = bisect.bisect_right(index[ch], i)
        if next_i < len(index[ch]) and index[ch][next_i] > i:
           i = index[ch][next_i]
        else:
            i = index[ch][0]
            ret += 1
    return ret

def main():
    print(is_sub_sequence('abc', 'abcbc'))
    print(is_sub_sequence('abc', 'abcdbc'))
    print(is_sub_sequence('xyz', 'xzyxz'))

if __name__ == "__main__":
    main()