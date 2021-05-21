from unittest import TestCase
import unittest
import pkgutil
from os import walk
from os import path
import numpy as np


class TestPackage(TestCase):
    def test_import_blade_1(self):
        import bladex as bx
        profile = bx.profilebase.ProfileBase()

    def test_import_blade_2(self):
        import bladex as bx
        vec = np.array([1.2, 2.4])
        profile = bx.profiles.CustomProfile(vec, vec, vec, vec)

    def test_import_blade_3(self):
        import bladex as bx
        profile = bx.profiles.NacaProfile('0012')

    def test_import_blade_4(self):
        import bladex as bx
        profile = bx.profiles.NacaProfile('0012')
        sections = [profile, profile]
        radii = np.array([1.0, 2.0])
        chord = np.array([0.5, 1.0])
        pitch = np.array([0.2, 0.3])
        rake = np.array([0.2, 0.3])
        skew = np.array([5.0, 10.0])
        blade = bx.blade.Blade(sections, radii, chord, pitch, rake, skew)

    def test_import_blade_5(self):
        import bladex as bx
        inter = bx.ndinterpolator.RBF('gaussian_spline', 1.2)