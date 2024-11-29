# 20241129

direction = ((0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0))


def oob(y, x):
    return y < -1000 or 1000 < y or x < -1000 or 1000 < x


def simulate(atoms):
    energies = 0

    while atoms:
        candidates = []
        visited = set()
        exploding = set()

        for y, x, d, e in atoms:
            dy, dx = direction[d]
            ny, nx = y + dy, x + dx

            if oob(ny, nx):
                continue

            if (ny, nx) in visited:
                exploding.add((ny, nx))
            else:
                visited.add((ny, nx))

            candidates.append((ny, nx, d, e))

        next_atoms = []
        for y, x, d, e in candidates:
            if (y, x) in exploding:
                energies += e
            else:
                next_atoms.append((y, x, d, e))

        atoms = next_atoms

    return energies


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    print(f"#{test} {simulate([list(map(int, input().split())) for _ in range(N)])}")
