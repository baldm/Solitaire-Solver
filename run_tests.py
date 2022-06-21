import unittest

# This file will call all unittests found in the entire directory
# Source: 
# https://stackoverflow.com/questions/644821/python-how-to-run-unittest-main-for-all-source-files-in-a-subdirectory
# User: @Sven Erik Knop
# Accessed: 21/06/2022 19:50

testsuite = unittest.TestLoader().discover('tests/')
unittest.TextTestRunner(verbosity=2).run(testsuite)
