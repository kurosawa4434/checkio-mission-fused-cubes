from collections import defaultdict
from functools import lru_cache
from typing import Tuple, List, Iterable


def fused_cubes(cubes: List[Tuple[int]]) -> Iterable[int]:

    def is_fused(cube_1, cube_2):
        return {(x + dx, y + dy, z + dz)
                for dx, dy, dz in ([-1, 0, 0], [1, 0, 0],
                                   [0, -1, 0], [0, 1, 0],
                                   [0, 0, -1], [0, 0, 1],
                                   [0, 0, 0])
                for x, y, z in cube_1} & cube_2

    @lru_cache()
    def slice_cube(x, y, z, e):
        return {(x + dx, y + dy, z + dz)
                for dx in range(e) for dy in range(e) for dz in range(e)}

    colors = defaultdict(int)
    rest = set(cubes)

    def set_color(cube, c):
        stack = [cube]
        while stack:
            tgt_cube_sliced = slice_cube(*(stack.pop()))
            for r in list(rest):
                if is_fused(set(tgt_cube_sliced), set(slice_cube(*r))):
                    colors[r] = c
                    stack.append(r)
                    rest.remove(r)

    c = 0
    for cube in cubes:
        if not colors[cube]:
            c += 1
            colors[cube] = c
            set_color(cube, c)

    result = defaultdict(set)
    for k, v in colors.items():
        result[v] |= slice_cube(*k)

    return map(len, result.values())


if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
