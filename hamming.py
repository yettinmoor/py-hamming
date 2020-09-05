def hamming16(x):
    masks = [ 0xaaaa, 0xcccc, 0xf0f0, 0xff00 ]
    err = 0
    for i, m in enumerate(masks):
        if count_bits(x & m) % 2 != 0:
            err |= 1 << i
    x ^= (1 << err) if err else 0
    return x, count_bits(x) % 2 == 0


def count_bits(x):
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits


tests = [
    0b0100100011101101, # ok
    0b0100100001101101, # 1 error
    0b0100101001101101, # 2 errors
]
for i in tests:
    h, ok = hamming16(i)
    print("{:016b}, {} error(s)".format(h, (h != i) + (not ok)))
