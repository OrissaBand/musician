#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of musician.
# https://github.com/orissaband/musician

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, funkymonkeymonk <monkey@buildingbananas.com>

from preggy import expect

from musician import gpiocontrol as subject
from tests.base import TestCase


class GPIOTestCase(TestCase):
    def test_initialize_pins(self):
        expect(subject.initialize_pins()).to_equal(True)
