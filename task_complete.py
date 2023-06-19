import asyncio

# Define a coroutine function
async def my_coroutine(name):
    print(f'Starting {name}')
    await asyncio.sleep(1)  # Simulate some asynchronous operation
    print(f'Finishing {name}')

# Create an event loop
loop = asyncio.get_event_loop()

# Create and schedule tasks
task1 = loop.create_task(my_coroutine('Task 1'))
task2 = loop.create_task(my_coroutine('Task 2'))

# Run the event loop until all tasks are complete
try:
    loop.run_until_complete(asyncio.gather(task1, task2))
finally:
    loop.close()