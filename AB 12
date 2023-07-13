import asyncio

async def main(): 
    task = asyncio.create_task(other_function()) #-> call the other function
    #await task #-> 1 2 A B 
    print("A")
    await asyncio.sleep(1)
    #await other_function() #-> wait to the other_function() to execute and then...
    print("B") #-> it will print B ... A 1 2 B
    #await task #-> A 1 B 2
    # --- RETURN VALUES ---
    return_value = await task
    print(f"Return value was {return_value}") #-> A 1 B 2 10

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())

# THIS PROGRAM WILL PRINT A B 1 2 IN DIFFERENT ORDERS THANKS TO ASYNCIO
