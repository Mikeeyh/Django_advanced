import time


def get_coffee():
    time.sleep(1)
    return "Coffee"


def get_milk():
    time.sleep(1.5)
    return "Milk"


def prepare_coffee_with_milk():
    coffee = get_coffee()
    milk = get_milk()

    time.sleep(0.5)

    # Aggregate the results
    return f"{coffee} with {milk}"


def main_sync(index):
    print(f"Task {index} started")
    start_time = time.time()
    print(prepare_coffee_with_milk())
    end_time = time.time()

    print(f"Task {index} executed in {end_time - start_time} seconds")


def main():
    start_time = time.time()
    ll = [main_sync(i) for i in range(10)]
    end_time = time.time()

    print(f"All tasks executed in {end_time - start_time} seconds")


main()

# All tasks executed in 30.019728899002075 seconds
