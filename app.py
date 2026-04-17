from logger import log_message

def add(a, b):
    result = a + b
    log_message(f"Adding {a} + {b} = {result}")
    return result

if __name__ == "__main__":
    print(add(2, 3))