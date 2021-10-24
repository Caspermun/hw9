def bank(a, years):
    year = 1
    while year <= years:
        a *= 1.1
        year += 1
    return a

if __name__ == '__main__':
    print(bank(1000, 5))