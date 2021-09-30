import sys
from prime_generator import PrimeGenerator


def main():
    pg = PrimeGenerator()
    print(pg.prime_to_max(int(sys.argv[1])))


main()
