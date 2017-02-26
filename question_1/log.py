import logging

def log_maker(write) :
	logging.basicConfig(filename='event_log.log',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filemode='w')
	logging.info(write)