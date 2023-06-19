import asyncio
import threading
import time

# Function to be run in a separate thread
def blocking_task(task_id):
    # Obtain the thread ID
    thread_id = threading.get_ident()

    # Perform some time-consuming operation
    for i in range(5):
        print(f"Running blocking task {task_id} in thread {thread_id}: {i}")
        time.sleep(1)

# Coroutine function that interacts with the blocking tasks
async def coroutine_task():
    print("Coroutine task started")

    # Run multiple blocking tasks in separate threads
    task_ids = [1, 2, 3]
    tasks = [asyncio.to_thread(blocking_task, task_id) for task_id in task_ids]
    await asyncio.gather(*tasks)

    print("Coroutine task completed")

# Main function to run the asyncio event loop
def main():
    # Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run the coroutine task
    loop.run_until_complete(coroutine_task())

    # Close the event loop
    loop.close()

# Run the main function
if __name__ == '__main__':
    main()