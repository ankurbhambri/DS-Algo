def toh(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return

    toh(n - 1, from_rod, aux_rod, to_rod)

    print(f"Move disk {n} from {from_rod} to {to_rod}")

    toh(n - 1, aux_rod, to_rod, from_rod)

toh(3, 'A', 'C', 'B')  # A, B and C are names of rods