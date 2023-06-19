import asyncio

# Define a coroutine function that runs indefinitely
async def my_background_task():
    while True:
        print('Background task is running...')
        await asyncio.sleep(1)  # Wait for 1 second before the next iteration

# Create an event loop
loop = asyncio.get_event_loop()

# Create and schedule the background task
task = loop.create_task(my_background_task())

try:
    # Run the event loop indefinitely
    loop.run_forever()
except KeyboardInterrupt:
    # Cancel the background task and stop the event loop on KeyboardInterrupt
    task.cancel()
    loop.run_until_complete(task)
finally:
    loop.close()