"""
Author:  Kalyan Vishnubhatla

This class resets all iOS simulators on the system by utilzing Apple's command line tools
"""


import logging
import re
import subprocess


class ResetIosSimulators(object):
    """Reset all simulators content and settings"""

    def perform_reset(self):
        # Get all the simulators first
        logging.info("Preparing to reset all simulators")
        p = subprocess.Popen(['xcrun', 'simctl', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        simulators, error = p.communicate()
        simulators = simulators.split("\n")

        # Get the simulator data from the rest of it
        for simulator in simulators:
            if simulator.startswith("    ") and not simulator.find("unavailable") > -1:
                # Extract the UUID using regex
                uuid = re.search('\(([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})\)', simulator,
                                 re.IGNORECASE).group(1)
                logging.info("Resetting " + uuid)
                subprocess.call(['xcrun', 'simctl', 'erase', uuid])


