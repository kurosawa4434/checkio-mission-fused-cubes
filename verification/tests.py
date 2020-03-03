"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [[0, 0, 0, 3], [1, 2, 2, 3]],
            "answer": [52],
            "explanation": ''
        },
        {
            "input": [[0, 0, 0, 3], [1, 3, 2, 3]],
            "answer": [54],
            "explanation": ''
        },
        {
            "input": [[0, 0, 0, 3], [1, 3, 3, 3]],
            "answer": [27, 27],
            "explanation": ''
        },
        {
            "input": [[0, 0, 0, 3], [3, 3, 3, 3]],
            "answer": [27, 27],
            "explanation": ''
        },
        {
            "input": [[0, 0, 0, 3], [3, 4, 3, 3]],
            "answer": [27, 27],
            "explanation": ''
        },
        {
            "input": [[0, 0, 0, 3], [-2, -2, -2, 3]],
            "answer": [53],
            "explanation": ''
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
            "explanation": 'cross'
        },
        {
            "input": [
                [-2, -4, 0, 2],
                [0, -2, 2, 2],
                [-2, 0, 4, 2],
                [-4, 2, 2, 2],
                [-6, 0, 0, 2],
            ],
            "answer": [8, 8, 8, 8 ,8],
            "explanation": ''
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
            "explanation": 'torii'
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
            "explanation": 'maya'
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
            "explanation": 'sphinx'
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
            "explanation": 'stone henge'
        },
    ],
}
