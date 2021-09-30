class PrimeGenerator:
    """Handle generation of prime numbers"""
    # Initialize prime numbers as a list and composites as a set

    def __init__(self):
        self.primes = []
        self.composites = set()

    def prime_to_max(self, n):
        """Generate a list of prime numbers"""
        for i in range(2, n+1):

            for j in range(i*2, n+1, i):
                self.composites.add(j)

            if i in self.composites:
                continue

            self.primes.append(i)

        return self.primes
