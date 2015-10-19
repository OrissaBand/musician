#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of musician.
# https://github.com/orissaband/musician

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, funkymonkeymonk <monkey@buildingbananas.com>


import os

if (os.uname()[4].startswith("arm") or ):
    import rpio
else:
    import rpiomock as rpio


def initialize_pins():
    return rpio.initialize_pins()
    # return True
