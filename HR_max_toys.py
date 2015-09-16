def max_toys(prices, rupees):
    spent = 0
    answer = 0
    prices.sort()
    for price in prices:
        if spent + price <= rupees:
            spent += price
            answer += 1
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)