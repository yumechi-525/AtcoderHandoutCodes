def solve():
    h, w = map(int, input().split())
    print((w - 1) * h + (h - 1) * w)

if __name__=="__main__":
    solve()