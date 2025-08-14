## logging with practical example
import logging

##logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"), # we can use FileHandler for file name and writing as well
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic app") ## module name

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def subtract(a,b):
    result = a+b
    logger.debug(f"Subtracting {a}-{b}={result}")
    return result

def mult(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Division {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by 0 not possible")
        return None

add(10,15)
subtract(15,10)
mult(10,20)
divide(20,10)
