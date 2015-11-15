__author__ = 'sjosund'

from abc import abstractmethod

class AbstractNumberList(object):

    def __init__(self, max_number):
        """

        :type max_number: int
        """
        self.max_number = max_number

    @abstractmethod
    def get_numbers(self):
        """

        :rtype : list
        """
        pass


class NumberList(AbstractNumberList):

    def get_numbers(self):
        return range(self.max_number)


class AbstractNumberListDecorator(AbstractNumberList):

    def __init__(self, number_list):
        """
        :type number_list: AbstractNumberList
        """
        self.number_list = number_list



class DividebleByNDecorator(AbstractNumberListDecorator):
    def __init__(self, number_list, n):
        """

        :type number_list: AbstractNumberList
        :type n: int
        """
        super(DividebleByNDecorator, self).__init__(number_list)
        self.n = n

    def get_numbers(self):
        return filter(lambda i: i%self.n == 0, self.number_list.get_numbers())


if __name__ == '__main__':
    nl = DividebleByNDecorator(
        DividebleByNDecorator(
            NumberList(500),
            3
        ),
        4
    )
    print(nl.get_numbers())