"""Setup for Command Dice"""

# Built In
from setuptools import setup

entry_points = {"console_scripts": ["roll=command_dice:roll"]}

setup(name="command_dice",
      version="0.0.1",
      entry_points=entry_points)
