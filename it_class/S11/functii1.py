def range_product(start, stop):
    """Calculate the product for numbers between start and stop."""
    prod = 1
    for i in range(start, stop):
        prod *= i
    return prod

start_in = int(input("Start: "))
stop_in = int(input("Stop: "))

print(f"Produsul numerelor din intervalul {start_in} si {stop_in} este {range_product(start_in, stop_in)}")

