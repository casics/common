# -*- python-indent-offset: 4 -*-
#
# @file    github.py
# @brief   Utilities for dealing with GitHub logins and such.
# @author  Michael Hucka
#
# <!---------------------------------------------------------------------------
# Copyright (C) 2015 by the California Institute of Technology.
# This software is part of CASICS, the Comprehensive and Automated Software
# Inventory Creation System.  For more information, visit http://casics.org.
# ------------------------------------------------------------------------- -->

from   configparser import ConfigParser
import os
import sys
from   pymongo import MongoClient
from   datetime import datetime

from messages import *

class GitHub():
    '''Class for handling GitHub user log-ins.'''

    @staticmethod
    def login(hosting_service, service_account):
        cfg = Config('mongodb.ini')
        section = hosting_service
        user_name = None
        user_password = None
        try:
            if service_account:
                for name, value in cfg.items(section):
                    if name.startswith('login') and value == service_account:
                        user_name = service_account
                        index = name[len('login'):]
                        if index:
                            user_password = cfg.get(section, 'password' + index)
                        else:
                            # login entry doesn't have an index number.
                            # Might be a config file in the old format.
                            user_password = value
                        break
                # If we get here, we failed to find the requested login.
                msg('Cannot find "{}" in section {} of config.ini'.format(
                    service_account, section))
            else:
                try:
                    user_name = cfg.get(section, 'login1')
                    user_password = cfg.get(section, 'password1')
                except:
                    user_name = cfg.get(section, 'login')
                    user_password = cfg.get(section, 'password')
        except Exception as err:
            msg(err)
            text = 'Failed to read "login" and/or "password" for {}'.format(
                section)
            raise SystemExit(text)
        return (user_name, user_password)


# Configuration file handling
# .............................................................................

class Config():
    '''A class to encapsulate reading our configuration file.'''

    _default_config_file = os.path.join(os.path.dirname(__file__), "config.ini")

    def __init__(self, cfg_file=_default_config_file):
        self._cfg = ConfigParser()
        try:
            with open(cfg_file) as f:
                self._cfg.readfp(f)
        except IOError:
            raise RuntimeError('file "{}" not found'.format(cfg_file))


    def get(self, section, prop):
        '''Read a property value from the configuration file.
        Two forms of the value of argument "section" are understood:
           * value of section is an integer => section named after host
           * value of section is a string => literal section name
        '''
        if isinstance(section, str):
            return self._cfg.get(section, prop)
        elif isinstance(section, int):
            section_name = Host.name(section)
            if section_name:
                return self._cfg.get(section_name, prop)
            else:
                return None


    def items(self, section):
        '''Returns a list of tuples of (name, value) for the given section.
        Two forms of the value of argument "section" are understood:
           * value of section is an integer => section named after host
           * value of section is a string => literal section name
        '''
        if isinstance(section, str):
            return self._cfg.items(section)
        elif isinstance(section, int):
            section_name = Host.name(section)
            if section_name:
                return self._cfg.items(section_name)
            else:
                return None
