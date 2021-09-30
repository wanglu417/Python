from stack import Stack


class StringProcessor:
    """Class for processing strings"""

    def process_string(self, line):
        # Create instances for two stacks
        self.stack0 = Stack()
        self.stack1 = Stack()
        for i in line:
            self.stack0.push(i)
        while(len(self.stack0.items) > 0):
            self.temp = self.stack0.pop()
            if self.temp == '*':
                self.stack1.push(self.stack0.pop())
            elif self.temp == '^':
                if len(self.stack0.items) == 0:
                    break
                self.stack1.push(self.stack0.pop())
                if len(self.stack0.items) == 0:
                    break
                self.stack1.push(self.stack0.pop())
            else:
                continue
        # Handle the condition when the length <=0
        return ''.join(self.stack1.items)
