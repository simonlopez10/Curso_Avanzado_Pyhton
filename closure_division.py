def make_division_by(n):
    def numerator(x: int) -> float:
        assert n !=0, 'You cannot divide by zero'
        return x/n
    return numerator

def run():
    divided_by_2 = make_division_by(2)
    print(divided_by_2(10))

if __name__ == '__main__':
    run()


