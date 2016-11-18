#-*-coding:utf-8-*-
import logging
import logging.config

def  loginfo(msg):
    logging.config.fileConfig("log.conf")
    logger = logging.getLogger("logger_info")
    logger.info(msg)
    return 1

def logerror(msg):
    logging.config.fileConfig("log.conf")
    logger = logging.getLogger("logger_error")
    logger.error(msg)
    return 1
