"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint
from my_solution import fused_cubes, select_drawing_cubes
from spheres import spheres


def make_test_dic(input, answer, explanation):
    return {
        'input': input,
        'answer': answer,
        'explanation': explanation,
    }


def make_spheres_tests(radiuses):
    answers = [56, 136, 304, 624, 1016, 1568, 2368, 3280, 4512, 5904, 7664, 9760, 12112]
    return [make_test_dic(spheres[r],
                          [answers[r - 3]],
                          select_drawing_cubes(spheres[r])) for r in radiuses]


def make_random_tests(num):
    def random_test():
        return [(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(1, 7)) for _ in range(10)]

    return [(cubes := random_test()) and make_test_dic(cubes,
                                                       sorted(fused_cubes(cubes)),
                                                       select_drawing_cubes(cubes)) for _ in range(num)]


def make_basic_tests(inputs):
    return [make_test_dic(inp, sorted(answer), select_drawing_cubes(inp)) for inp, answer in inputs]


TESTS = {
    "Basics": make_basic_tests([
        ([[0, 0, 0, 3], [1, 2, 2, 3]], [52]),
        ([[0, 0, 0, 3], [1, 3, 2, 3]], [54]),
        ([[0, 0, 0, 3], [1, 3, 3, 3]], [27, 27]),
        ([[0, 0, 0, 3], [3, 3, 3, 3]], [27, 27]),
        ([[0, 0, 0, 3], [3, 4, 3, 3]], [27, 27]),
        ([[0, 0, 0, 3], [-2, -2, -2, 3]], [53]),
    ]),
    "Extra": make_basic_tests([
        # cross
        ([[-1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1],
          [0, -1, 0, 1], [0, 0, 1, 1], [0, 0, -1, 1]],
         [1, 1, 1, 1, 1, 1]),

        # stair
        ([[-2, -4, 0, 2], [0, -2, 2, 2], [-2, 0, 4, 2],
          [-4, 2, 2, 2], [-6, 0, 0, 2]],
         [8, 8, 8, 8, 8]),

        # torii gate
        ([[0, 0, 0, 1], [0, 1, 0, 1], [0, 2, 0, 1],
          [0, 3, 0, 1], [0, 5, 0, 1], [-1, 4, 0, 1],
          [0, 4, 0, 1], [1, 4, 0, 1], [2, 4, 0, 1],
          [3, 4, 0, 1], [4, 4, 0, 1], [5, 4, 0, 1],
          [-1, 6, 0, 1], [0, 6, 0, 1], [1, 6, 0, 1],
          [2, 6, 0, 1], [3, 6, 0, 1], [4, 6, 0, 1],
          [5, 6, 0, 1], [4, 0, 0, 1], [4, 1, 0, 1],
          [4, 2, 0, 1], [4, 3, 0, 1], [4, 5, 0, 1],
          [2, 5, 0, 1]],
         [25]),

        # maya
        ([[-4, 0, -4, 2], [-2, 0, -4, 2], [0, 0, -4, 2],
          [2, 0, -4, 2], [2, 0, -2, 2], [2, 0, 0, 2],
          [2, 0, 2, 2], [-3, 2, -3, 2], [-1, 2, -3, 2],
          [1, 2, -3, 2], [1, 2, -1, 2], [1, 2, 1, 2],
          [-2, 4, -2, 2], [0, 4, -2, 2], [0, 4, 0, 2],
          [-1, 0, -5, 1], [0, 0, -5, 1], [-1, 1, -4, 2],
          [-1, 3, -3, 2], [4, 0, -1, 1], [4, 0, 0, 1],
          [2, 1, -1, 2], [1, 3, -1, 2], [-1, 6, -1, 2]],
         [140]),

        # sphinx
        ([[0, 0, -10, 1], [0, 0, -9, 1], [0, 0, -8, 1],
          [0, 0, -7, 1], [0, 0, -6, 1], [3, 0, -10, 1],
          [3, 0, -9, 1], [3, 0, -8, 1], [3, 0, -7, 1],
          [3, 0, -6, 1], [1, 4, -6, 2], [0, 0, -5, 2],
          [2, 0, -5, 2], [0, 1, -5, 2], [2, 1, -5, 2],
          [1, 3, -5, 2], [2, 0, -3, 2], [1, 2, -3, 2],
          [1, 1, -1, 2], [1, 0, 0, 2], [1, 0, 2, 2],
          [3, 0, 1, 1], [3, 0, 2, 1], [3, 0, 3, 1],
          [-9, 2, 6, 1], [-10, 0, 5, 2], [-9, 0, 5, 2],
          [-9, 0, 6, 2], [-11, 0, 4, 1], [-10, 0, 4, 1],
          [-9, 0, 4, 1], [-8, 0, 4, 1], [-7, 0, 4, 1],
          [-7, 0, 5, 1], [-7, 0, 6, 1], [-7, 0, 7, 1],
          [-7, 0, 8, 1], [-8, 0, 8, 1], [-11, 0, 5, 1]],
         [28, 89]),

        # stone henge
        ([[-9, 0, 0, 2], [-9, 2, 0, 2], [-5, 0, 1, 2],
          [-5, 2, 1, 2], [-1, 0, 2, 2], [-1, 2, 2, 2],
          [3, 0, 3, 2], [3, 2, 3, 2], [7, 0, 2, 2],
          [7, 2, 2, 2], [6, 3, 2, 2], [4, 3, 2, 2],
          [2, 3, 3, 2], [0, 3, 3, 2], [-2, 3, 2, 2],
          [-4, 3, 2, 2], [-2, 0, -7, 2], [0, 0, 0, 1],
          [0, 1, 0, 1], [3, 0, -1, 1], [3, 1, -1, 1]],
         [2, 2, 8, 16, 103]),
    ]),
    'Spheres': make_spheres_tests(range(3, 16, 1)),
    'Randoms': make_random_tests(5)
}
