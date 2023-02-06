from django.http import HttpResponse


import logging
import datetime
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s '
logger = logging.getLogger(__name__)

# # To override the default severity of logging
# logger.setLevel('DEBUG')

# # Use FileHandler() to log to a file
# file_handler = logging.FileHandler("mylog.log")
# formatter = logging.Formatter(log_format)
# file_handler.setFormatter(formatter)

# # Don't forget to add the file handler
# logger.addHandler(file_handler)



# # # import the logging library
# import logging
# # # Get an instance of a logger





# from logging import getLogger, StreamHandler, Formatter, Handler, NOTSET, getLevelName
# from datetime import datetime as date_time
# from sqlite3 import connect
# class FileHandler(Handler):
#     def __init__(self, db_file):
#         super().__init__()
#         self.db_file = db_file
#         self.db_file = connect("db.sqlite3")
#         self.db_file.execute('CREATE TABLE IF NOT EXISTS logs (date TEXT, '
#                 'time TEXT, lvl INTEGER, lvl_name TEXT, msg TEXT, '
#                 'logger TEXT, lineno INTEGER)')

#     def emit(self, record):
#         self.db_file.execute(
#             'INSERT INTO logs VALUES (:1,:2,:3,:4, :5, :6, :7)', (
#                 date_time.now().strftime('%A, the %d of %B, %Y'),
#                 date_time.now().strftime('%I:%M %p'),
#                 record.levelno,
#                 record.levelname,
#                 record.msg,
#                 record.name,
#                 record.lineno
#                 )
#         )
#         self.db_file.commit()



# logger = getLogger(__name__)
# logger.setLevel('DEBUG')
# logger_formatter = Formatter(
#         fmt = '<LVL: %(levelno)s (%(levelname)s), LOGGER: %(name)s> - "%(message)s at %(asctime)s"',
#         datefmt = '%I:%M %p on %A, the %d of %B, %Y'
#     )

# logger_database_handler = FileHandler('db.sqlite3')

# logger.addHandler(logger_database_handler)
# logger_database_handler.setLevel(10)

# # logger.log(
# #             msg = 'Something happened to db',
# #             level = 10
# #             )
# print(connect('db.sqlite3').execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall())



# -*- coding: utf-8 -*-

#
# Found it in the internet and modified for my own
# Amka [meamka@ya.ru]
#

# import logging
# import os
# import sqlite3
# from datetime import datetime

# class SQLiteHandler(logging.Handler): # Inherit from logging.Handler
#     """
#     Logging handler that write logs to SQLite DB
#     """
#     def __init__(self, filename):
#         global db
#         # run the regular Handler __init__
#         logging.Handler.__init__(self)
#         # Our custom argument
#         db = sqlite3.connect(filename) # might need to use self.filename
#         db.execute("CREATE TABLE IF NOT EXISTS debug(date datetime, loggername text, filename, srclineno integer, func text, level text, msg text)")
#         db.commit()

#     def emit(self, record):
#         # record.message is the log message
#         thisdate = datetime.now()
#         db.execute(
#             'INSERT INTO debug(date, loggername, filename, srclineno, func, level, msg) VALUES(?,?,?,?,?,?,?)',
#             (
#                 thisdate,
#                 record.name,
#                 os.path.abspath(record.filename),
#                 record.lineno,
#                 record.funcName,
#                 record.levelname,
#                 record.msg,
#             )
#         )
#         db.commit()


# if __name__ == '__main__':
#     # Create a logging object (after configuring logging)
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(SQLiteHandler('debugLog.sqlite'))
#     logger.debug('Test 1')
#     logger.warning('Some warning')
#     logger.error('Alarma!')


def hello_reader(request):
    # logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    logger.warning("I am a hello reader function")
    return HttpResponse("<h1>Hello Reader :)</h1>")

def Success(request):

    # logger.warning('Success was accessed at '+str(datetime.datetime.now())+' hours!')
    logger.error("I am a Success page")

    return HttpResponse("<h1>Success Page :)</h1>")
