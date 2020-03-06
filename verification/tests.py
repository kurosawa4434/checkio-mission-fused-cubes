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


def make_spheres_tests(radiuses):
    answers = [56, 136, 304, 624, 1016, 1568, 2368, 3280, 4512, 5904, 7664, 9760, 12112]
    return [{
        'input': spheres[r],
        'answer': [answers[r-3]],
        'explanation': [f'spheres_test_{r}', select_drawing_cubes(spheres[r])],
    } for r in radiuses]


def make_random_tests(num):
    random_tests = []
    for n in range(num):
        cubes = [(randint(-10, 10), randint(-10, 10),
                  randint(-10, 10), randint(1, 7)) for _ in range(10)]
        random_tests.append(
            {
                'input': cubes,
                'answer': sorted(fused_cubes(cubes)),
                'explanation': [f'random_test_{n}', select_drawing_cubes(cubes)],
            }
        )
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [[0, 0, 0, 3], [1, 2, 2, 3]],
            "answer": [52],
            "explanation": ['fused'],
        },
        {
            "input": [[0, 0, 0, 3], [1, 3, 2, 3]],
            "answer": [54],
            "explanation": ['touch with faces'],
        },
        {
            "input": [[0, 0, 0, 3], [1, 3, 3, 3]],
            "answer": [27, 27],
            "explanation": ['touch with edges'],
        },
        {
            "input": [[0, 0, 0, 3], [3, 3, 3, 3]],
            "answer": [27, 27],
            "explanation": ['touch with vetices'],
        },
        {
            "input": [[0, 0, 0, 3], [3, 4, 3, 3]],
            "answer": [27, 27],
            "explanation": ['separated'],
        },
        {
            "input": [[0, 0, 0, 3], [-2, -2, -2, 3]],
            "answer": [53],
            "explanation": ['negative coordinate'],
        },
    ],
    "Extra": [
        {
            "input": [
                [-1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 0, 1],
                [0, -1, 0, 1],
                [0, 0, 1, 1],
                [0, 0, -1, 1],
            ],
            "answer": [1, 1, 1, 1, 1, 1],
            "explanation": ['cross'],
        },
        {
            "input": [
                [-2, -4, 0, 2],
                [0, -2, 2, 2],
                [-2, 0, 4, 2],
                [-4, 2, 2, 2],
                [-6, 0, 0, 2],
            ],
            "answer": [8, 8, 8, 8, 8],
            "explanation": ['stair'],
        },
        {
            "input": [
                [0, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 2, 0, 1],
                [0, 3, 0, 1],
                [0, 5, 0, 1],
                [-1, 4, 0, 1],
                [0, 4, 0, 1],
                [1, 4, 0, 1],
                [2, 4, 0, 1],
                [3, 4, 0, 1],
                [4, 4, 0, 1],
                [5, 4, 0, 1],
                [-1, 6, 0, 1],
                [0, 6, 0, 1],
                [1, 6, 0, 1],
                [2, 6, 0, 1],
                [3, 6, 0, 1],
                [4, 6, 0, 1],
                [5, 6, 0, 1],
                [4, 0, 0, 1],
                [4, 1, 0, 1],
                [4, 2, 0, 1],
                [4, 3, 0, 1],
                [4, 5, 0, 1],
                [2, 5, 0, 1],
            ],
            "answer": [25],
            "explanation": ['torii'],
        },
        {
            "input": [
                [-4, 0, -4, 2],
                [-2, 0, -4, 2],
                [0, 0, -4, 2],
                [2, 0, -4, 2],
                [2, 0, -2, 2],
                [2, 0, 0, 2],
                [2, 0, 2, 2],
                [-3, 2, -3, 2],
                [-1, 2, -3, 2],
                [1, 2, -3, 2],
                [1, 2, -1, 2],
                [1, 2, 1, 2],
                [-2, 4, -2, 2],
                [0, 4, -2, 2],
                [0, 4, 0, 2],
                [-1, 0, -5, 1],
                [0, 0, -5, 1],
                [-1, 1, -4, 2],
                [-1, 3, -3, 2],
                [4, 0, -1, 1],
                [4, 0, 0, 1],
                [2, 1, -1, 2],
                [1, 3, -1, 2],
                [-1, 6, -1, 2]
            ],
            "answer": [140],
            "explanation": ['maya'],
        },
        {
            "input": [
                [0, 0, -10, 1],
                [0, 0, -9, 1],
                [0, 0, -8, 1],
                [0, 0, -7, 1],
                [0, 0, -6, 1],
                [3, 0, -10, 1],
                [3, 0, -9, 1],
                [3, 0, -8, 1],
                [3, 0, -7, 1],
                [3, 0, -6, 1],
                [1, 4, -6, 2],
                [0, 0, -5, 2],
                [2, 0, -5, 2],
                [0, 1, -5, 2],
                [2, 1, -5, 2],
                [1, 3, -5, 2],
                [2, 0, -3, 2],
                [1, 2, -3, 2],
                [1, 1, -1, 2],
                [1, 0, 0, 2],
                [1, 0, 2, 2],
                [3, 0, 1, 1],
                [3, 0, 2, 1],
                [3, 0, 3, 1],
                [-9, 2, 6, 1],
                [-10, 0, 5, 2],
                [-9, 0, 5, 2],
                [-9, 0, 6, 2],
                [-11, 0, 4, 1],
                [-10, 0, 4, 1],
                [-9, 0, 4, 1],
                [-8, 0, 4, 1],
                [-7, 0, 4, 1],
                [-7, 0, 5, 1],
                [-7, 0, 6, 1],
                [-7, 0, 7, 1],
                [-7, 0, 8, 1],
                [-8, 0, 8, 1],
                [-11, 0, 5, 1],
            ],
            "answer": [28, 89],
            "explanation": ['sphinx'],
        },
        {
            "input": [
                [-9, 0, 0, 2],
                [-9, 2, 0, 2],
                [-5, 0, 1, 2],
                [-5, 2, 1, 2],
                [-1, 0, 2, 2],
                [-1, 2, 2, 2],
                [3, 0, 3, 2],
                [3, 2, 3, 2],
                [7, 0, 2, 2],
                [7, 2, 2, 2],
                [6, 3, 2, 2],
                [4, 3, 2, 2],
                [2, 3, 3, 2],
                [0, 3, 3, 2],
                [-2, 3, 2, 2],
                [-4, 3, 2, 2],
                [-2, 0, -7, 2],
                [0, 0, 0, 1],
                [0, 1, 0, 1],
                [3, 0, -1, 1],
                [3, 1, -1, 1],
            ],
            "answer": [2, 2, 8, 16, 103],
            "explanation": ['stone henge'],
        },
    ],
    'Spheres': make_spheres_tests(range(3, 16, 3)),
    'Randoms': make_random_tests(5)
}
