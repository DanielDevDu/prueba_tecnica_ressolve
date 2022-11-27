import os
import re
import json
import math

###################################################################################
# This function helps you to test your solution using validation_test.json
###################################################################################


def validate_function(function_name):
    validation_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "validation_test.json")
    validation_test = {}
    with open(validation_file_path, 'r') as f:
        validation_test = json.load(f)

    test_list = None
    try:
        test_list = validation_test[function_name]
    except:
        print("Error - the function name does not exits in the validation test json")
        exit(1)
    print("Total test found: {}".format(len(test_list)))
    test_ok = 0
    for index, test in enumerate(test_list):
        input_value = test['input']
        result = globals()[function_name](input_value)
        if result == test['output']:
            print("Test {} -> input: {} expected: {} function result: {} -> OK".format(index,
                  test['input'], test['output'], result))
            test_ok += 1
        else:
            print("Test {} -> input: {} expected: {} function result: {} -> FAILED".format(index,
                  test['input'], test['output'], result))

    print("Total tests passed: {} Total tests failed: {}".format(
        test_ok, int(len(test_list) - test_ok)))


def pairwise(it):
    """Allow to iterate over a list by pairs"""
    it = iter(it)
    while True:
        try:
            yield next(it), next(it)
        except StopIteration:
            # no more elements in the iterator
            return


def list_average(input_value):
    """
    ----------------------------------------------------------
    Given a list of numbers, return their average (int cast).
    However, if one of the values is 10 then it does not count
    towards the average and values to its right do not count
    until another 10 value appears.
    ----------------------------------------------------------
    """

    number = 10
    size = len(input_value)
    total_sum = sum(input_value)

    # All indexes where number=10 is present
    indexes = [i for i, x in enumerate(input_value) if x == number]
    len_indexes = len(indexes)

    if len_indexes == 0:
        # No 10 in the list
        output = total_sum / size
    else:
        output_list = []
        res_list = []
        if len_indexes == 1:
            # Only one 10 in the list
            output_list = input_value[:indexes[0]]
            if len(output_list) == 0:
                output = 0
            else:
                output = sum(output_list) / len(output_list)
        else:
            for i, j in pairwise(indexes):
                res_list += input_value[i:j+1]
                if len_indexes % 2 != 0 and j == indexes[-2]:
                    # special case when the number occurs an odd number of times
                    res_list += input_value[indexes[-1]:]

            count_res = len(res_list)
            res_sum = sum(res_list)

            size = size - count_res
            total_sum = total_sum - res_sum
            output = total_sum / size

    return int(output)


def multiplies_numbers(input_value):
    """
    -----------------------------------------
    Given a string, return the multiplication
    of the numbers appearing in the string
    -----------------------------------------
    """

    output = re.findall(r'\d+', input_value)
    output = [int(i) for i in output]
    result = 1
    for num in output:
        result *= num
    return result


def christmas_tree(input_value):
    """
    -------------------------------------------
    Given an odd number(n),
    print a christmas tree pattern(nxn matrix).
    -------------------------------------------
    """

    x = input_value
    rows = int(x/2) + 1

    for i in range(0, rows, 1):
        # print tree
        print(' ' * (x - (i + 1)), '*' * (2*i+1))
    for i in range(0, rows, 1):
        # print trunk
        print(' ' * (2*(rows-1)), '*' * (1))


print("\n\n======================== List Average ========================\n\n")
validate_function('list_average')
print("\n\n======================== Multiplies Numbers ========================\n\n")
validate_function('multiplies_numbers')
print("\n\n======================== Christmas Trees ========================\n\n")
christmas_tree(5)
