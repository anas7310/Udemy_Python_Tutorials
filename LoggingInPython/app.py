import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b}= {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying: {a} * {b}= {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Divide {a} / {b}= {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Cannot divide by zero")
        return None

add(10,13)
subtract(9,3)
multiply(47,2)
divide(20,0)

