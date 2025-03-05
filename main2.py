def print_multiplication_table():
    table_size = 10

    print("    ", end="")
    for i in range(1, table_size + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (table_size * 4 + 4))

    for i in range(1, table_size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, table_size + 1):
            print(f"{i * j:4}", end="")
        print()



print_multiplication_table()
