class FuctionsWithNums:

    def __init__(self, number):
        self.num = number

    def __del__(self):
        print("%s is deleted" % self)

    def is_divisible_by(self, divisor):
        return self.num % divisor == 0

    @staticmethod
    def stat_method(num_one, num_two):
        return (lambda n1, n2: n1 * n2)(num_one, num_two)


class Child(FuctionsWithNums):

    def __init__(self, variable, number):
        super().__init__(number)
        self.var = variable
        self._p_var = 0

    def __is_string(self):
        return isinstance(self.var, str)


class SecondChild(Child):

    def __init__(self, variable, number):
        super().__init__(variable, number)

    @staticmethod
    def stat_method(num_one, num_two):
        temp = num_one * num_two

        while num_one and num_two:
            if num_one > num_two:
                num_one %= num_two
            else:
                num_two %= num_one

        gcd = num_one + num_two
        lcm = temp // gcd

        return gcd, lcm


if __name__ == "__main__":
    obj = FuctionsWithNums(3)
    print("Is 3 divisible by 6?", obj.is_divisible_by(6))
    print("Result of static method is: ", obj.stat_method(2, 3))

    obj_child = Child("str", 16)
    print("Is 16 divisible by 4?", obj_child.is_divisible_by(4))
    print("Protected variable is: ", obj_child._p_var)
    # print("Private method is: ", obj.__is_string()) Cannot call the private method

    obj_second_child = SecondChild(16, 10)
    print("Result of static method is:", obj_second_child.stat_method(2, 3))

    from functools import reduce

    # Use map to print the square of each numbers rounded
    # to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    # Fix all three respectively.
    map_result = list(map(lambda x: x ** 2, my_floats))
    map_result = [round(i, 2) for i in map_result]
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)
