
def isprime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:  # 防爆int（虽然没用）
        if x % i == 0:
            return False
        i += 1
    return True


