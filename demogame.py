#!/usr/bin/env python3

"""
Imports the the game demo and executes the main function.
"""
import sys
from os import environ
# Hide the Hello to Pygame message
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'YES'

from videogame import game



if __name__ == "__main__":
    sys.exit(game.MultiSceneGameDemo().run())
