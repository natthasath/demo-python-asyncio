import asyncio

async def coroutine_example():
    print("Coroutine started")
    await asyncio.sleep(1)  # Simulate some time-consuming task
    print("Coroutine resumed")
    await asyncio.sleep(2)  # Simulate another task
    print("Coroutine finished")

async def main():
    print("Main program started")
    await coroutine_example()
    print("Main program finished")

asyncio.run(main())