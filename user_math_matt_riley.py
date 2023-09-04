"""

Author: Matt Riley
Date: August 31, 2023
Purpose: Experiment with different math functions,
and custom functions that utilize the math module.

@ uses math module - for some advanced math

"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_display(height, width):
    """
    Return area of a display given the height and width.

    @param height: the height of the display in inches
    @param width: the width of the display in inches
    @return: the area of the display
    @raise Exception: if height or width is not a number
    """
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_area_of_monitor({height},{width})")

    try: 
        area = height * width
        logger.info(f"The monitor area is {area} square inches.")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_monitor_size(height, width):
    """
    Return size of a display given the height and width.

    @param height: the height of the display in inches
    @param width: the width of the display in inches
    @return: the area of the display
    @raise Exception: if height or width is not a number
    """
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_monitor_size({height},{width})")

    try: 
        size = math.hypot(height,width)
        logger.info(f"The monitor size is {size} inches.")
        return size
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_viewing_distance_range(size):
    """
    Return minimum and maximum viewing distance for a display given the size in inches.

    @param size: the size of the display in inches
    @return: the minimum and maximum display size in inches
    @raise Exception: if height or width is not a number
    """
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_viewing_distance_range({size})")

    try:
        min_distance = size * 1.2
        max_distance = size * 2.5
        distance_range = (min_distance / 12, max_distance / 12)
        logger.info(f"The minumum viewing distance is {min_distance / 12} feet.")
        logger.info(f"The maximum viewing distance is {max_distance / 12} feet.")
        return distance_range
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_size_from_viewing_distance(distance):
    """
    Return minimum and maximum display size based on viewing distance in feet.

    @param distance: the distance from the display in feet
    @return: the minimum and maximum display size in inches
    @raise Exception: if distance is not a number
    """
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_size_from_viewing_distance({distance})")

    try:
        min_size = (distance * 12) / 2.5
        max_size = (distance * 12) / 1.2
        size_range = (min_size, max_size)
        logger.info(f"The minumum display size {min_size} inches.")
        logger.info(f"The maximum display size {max_size} inches.")
        return size_range
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"get_area_of_monitor(9,12) = {get_area_of_display(9,12)}")
    logger.info(f"get_area_of_monitor(13.2,23.5) = {get_area_of_display(13.2,23.5)}")
    logger.info(f"get_monitor_size(9,12) = {get_monitor_size(9,12)}")
    logger.info(f"get_monitor_size(13.2,23.5) = {get_monitor_size(13.2,23.5)}")
    logger.info(f"get_viewing_dinstance_range(15) = {get_viewing_distance_range(15)}")
    logger.info(f"get_viewing_dinstance_range(27) = {get_viewing_distance_range(27)}")
    logger.info(f"get_size_from_viewing_distance(3) = {get_size_from_viewing_distance(3)}")
    logger.info(f"get_size_from_viewing_distance(10) = {get_size_from_viewing_distance(10)}")

    print("Done. Please check the log file for more details.")