class TextCleaner:

    def clean(self, f):
        """Handle switching to lowercase and eliminating puntuation"""
        self.f2 = f.replace(',', ' '+'COMMA')
        self.f3 = self.f2.replace('(', '')
        self.f4 = self.f3.replace(')', '')
        self.f5 = self.f4.replace('"', '')
        self.f6 = self.f5.lower()
        self.f7 = self.f6.replace('comma', 'COMMA')
        self.f8 = self.f7.split()
        return self.f8
