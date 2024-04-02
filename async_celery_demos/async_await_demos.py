import asyncio
import time


async def get_coffee():
    await asyncio.sleep(1)
    return "Coffee"


async def get_milk():
    await asyncio.sleep(1.5)
    return "Milk"


async def prepare_coffee_with_milk():
    coffee, milk = await asyncio.gather(get_coffee(), get_milk())

    await asyncio.sleep(0.5)

    # Aggregate the results
    return f"{coffee} with {milk}"


async def main_async(index):
    print(f"Task {index} started")
    start_time = time.time()
    print(await prepare_coffee_with_milk())
    end_time = time.time()

    print(f"Task {index} executed in {end_time - start_time} seconds")


async def main():
    start_time = time.time()
    await asyncio.gather(*[main_async(i) for i in range(10)])
    end_time = time.time()

    print(f"All tasks executed in {end_time - start_time} seconds")

asyncio.run(main())

# All tasks executed in 2.0167672634124756 seconds
