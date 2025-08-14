import logging
## we can use this file anywhere any number of time if we use it like this 
## configuring the logging
logging.basicConfig(
    filename = 'app.log', ## now we have written every information in the file named app.log
    filemode='w',
    level=logging.DEBUG,
    format ='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)