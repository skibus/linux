def calc_sum(start, end):
    result = 0
    number = start
    while number > 0:
        result += number
        number += 1
    return result


def main():
    print(calc_sum(1, 1000))


if __name__=='__main__':
    main()
