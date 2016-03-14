#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import authentication
import getpass


def login(username, maxattempts=3):
    """ 1.  username (str): A string representing
    the username of the userattempting to log in
    2.  maxattempts (int, optional):
    An integer represent the maximum number of prompted attempts
    before the function returns False. Defaults to ``3``"""
    authenticate = False
    password = getpass.getpass(prompt='Password: ')
    while password < maxattempts:
        username = False
        getpass.getpass(prompt='Please enter your password: ')
        authentication.authenticate(username, password, maxattempts)
        if password >= maxattempts:
            return False
        else:
            return True
