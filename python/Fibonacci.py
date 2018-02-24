class Fibonacci(object):
    def generate(self, length):
        """Generate a Fibonacci list

        :param length:
            the length of the list to generate
        :return:
            an array list of numbers

        >>> f = Fibonacci()
        >>> f.generate(1)
        [0]
        >>> f.generate(2)
        [0, 1]
        >>> f.generate(3)
        [0, 1, 1]
        >>> f.generate(4)
        [0, 1, 1, 2]
        >>> f.generate(5)
        [0, 1, 1, 2, 3]
        >>> f.generate(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        """
        sequence = []
        for index in range(length):
            if index < 2:
                sequence.append(index)
            else:
                sequence.append(sequence[index - 1] + sequence[index - 2])
        return sequence