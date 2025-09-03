from typing import Tuple
from math  import lcm
from functools import reduce
import builtins
DEBUG = True
def tabs_to_spaces():
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input())
    depth_equations = {}
    current_depth = -1
    for line in lines:

        if '{' in line:
            current_depth += 1
        # initialize the set in dict
        if depth_equations.get(current_depth, None) is None:
            depth_equations[current_depth] = set()
        num_s = line.count('s')
        num_t = line.count('t')
        # add equation
        depth_equations[current_depth].add( (num_s, num_t) )

        print(f'depth {current_depth}: {line}, equations: {line[0:-1]}')
        if '}' in line:
            current_depth -= 1
    # Check level by level
    # Ensure compatability between levels
    final_solution = 1
    for depth_level, depth_set in depth_equations.items():
        space_identity = -1
        all_solutions = []

        for a, b in depth_set:
            # Defines number of spaces
            if b == 0:
                if space_identity == -1:
                    space_identity = a
                elif space_identity != a:
                    # two conflicting “fixed” space identities at same depth
                    return -1
                continue

            # Base case
            solution = solve_equation((a, b), depth_level)
            if not isinstance(solution, int):
                raise TypeError(
                    f"Expected int from solve_equation, got {type(solution)}: {solution} "
                    f"for equation {(a, b)} at depth {depth_level}"
                )
            print(f'solution: {solution} for equation: {(a, b)} and depth: {depth_level}')
            all_solutions.append(solution)

        print(f'For depth {depth_level}: {all_solutions}')

        if all_solutions:
            current_solution = lcm(*all_solutions)  # fastest & cleanest
        else:
            current_solution = space_identity if space_identity != -1 else None

        print(f'lcm: {current_solution}')

        if space_identity != -1 and current_solution is not None:
            print('space_identity exists, checking solution:')
            for a, b in depth_set:
                if not is_valid_pair((a, b), space_identity, current_solution):
                    if space_identity % current_solution == 0:
                        current_solution = space_identity
                        print(f'lcm updated: ')
                    else:
                        return -1
        if current_solution != 0:
            final_solution = lcm(final_solution, current_solution)

    print(f'final_solution: {final_solution}')
    return final_solution


def solve_equation(pair: Tuple[int, int], level: int):
    spaces = pair[0]
    tabs_coefficient   = pair[1]
    # (spaces + tabs_coefficient * i) mod level = 0
    # spaces mod level + tabs_coefficient * i mod level = 0
    # i mod level = -spaces mod level / tabs_coefficient mod level
    # i mod level = -spaces / tabs_coefficient mod level
    i = ( -1* spaces // tabs_coefficient) % level
    if i == 0:
        i = level
    return i

def is_valid_pair(pair: Tuple[int, int], space_identity: int, solution: int) -> bool:
    spaces = pair[0]
    tabs_coefficient   = pair[1]
    return (spaces + tabs_coefficient * solution) == space_identity


_ORIG_PRINT = builtins.print          # do this before patching!
if not DEBUG:
    builtins.print = lambda *a, **k: None
sol = tabs_to_spaces()
builtins.print = _ORIG_PRINT

print(sol)
CS 37300	Data Mining And Machine Learning