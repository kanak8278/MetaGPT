#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/1 12:41
@Author  : alexanderwu
@File    : logs.py
"""

import sys

from loguru import logger as _logger

from metagpt.const import PROJECT_ROOT
from datetime import datetime


def define_log_level(print_level="INFO", logfile_level="DEBUG"):
    """调整日志级别到level之上
       Adjust the log level to above level
    """
    # base_log_file_path = PROJECT_ROOT / 'logs/log'

    # # Initialize the counter
    # counter = 1

    # # Generate a unique log file path
    # while True:
    #     # Generate the log file path
    #     log_file_path = f'{base_log_file_path}_{counter:02d}.txt'

    #     # Check if the log file already exists
    #     if not os.path.exists(log_file_path):
    #         # The log file does not exist, so we can use this path
    #         break

    #     # Increment the counter and try again
    #     counter += 1
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Create the log file name with the timestamp
    log_file_name = f"log_{timestamp}.txt"

    # Add the log file with the timestamped name
    
    _logger.remove()
    _logger.add(sys.stderr, level=print_level)
    _logger.add(PROJECT_ROOT / f'logs/{log_file_name}', level=logfile_level)
    # _logger.add(PROJECT_ROOT / 'logs/log.txt', level=logfile_level)
    return _logger


logger = define_log_level()
