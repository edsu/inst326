import logging
import sys



def main():
    logging.basicConfig(filename='test.log', level=logging.WARNING)
    logging.info('Started')
    for n in range(100):
        logging.debug("Base is {0}".format(n))
        s = n**2
        if s > 500:
            logging.warning("Square is {0}".format(s))
    logging.info('Finished')

if __name__ == '__main__':
    main()
