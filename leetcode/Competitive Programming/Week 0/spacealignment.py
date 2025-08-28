def tabs_to_spaces():
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input())
    depth_equations = {}
    current_depth = 0
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
    print(depth_equations)
tabs_to_spaces()