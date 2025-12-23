from itertools import permutations

def S_of_perm(perm):
    """Compute S(p) for a given permutation p."""
    running_and = (1 << 60) - 1  # big all-ones; will be reduced immediately
    total = 0
    for x in perm:
        running_and &= x
        total += running_and.bit_count()
    return total

def brute_maximize_S(n, verbose=False):
    """
    Exhaustively search all permutations of [0..2^n-1] to maximize S(p).

    WARNING: (2^n)! permutations -> explodes fast.
    Practical only for very small n (typically n<=4).
    """
    m = 1 << n
    arr = list(range(m))

    best_score = -1
    best_perm = None
    checked = 0

    for perm in permutations(arr):
        checked += 1
        score = S_of_perm(perm)
        if score > best_score:
            best_score = score
            best_perm = perm
            if verbose:
                print(f"new best: S={best_score}, perm={best_perm}")
        if verbose and checked % 100000 == 0:
            print(f"checked {checked} perms... current best S={best_score}")

    return best_score, best_perm

if __name__ == "__main__":
    n = 4
    best_score, best_perm = brute_maximize_S(n, verbose=True)
    print("n =", n)
    print("best S =", best_score)
    print("best perm =", best_perm)
