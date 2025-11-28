import numpy

from openalea.spice.common.math import (
    denormalize,
    average_vector,
    cross_vector,
    spherical_to_cartesian,
    orthonormal_basis,
    geo_hemisphere,
)
from openalea.plantgl.all import Vector3


def test_denormalize():
    zero = denormalize(0.0)
    assert zero == 0

    maximum = denormalize(1.0)
    assert maximum == 255

    middle = denormalize(0.5)
    assert middle == 127


def test_average_vector():
    list_vector = [Vector3(0, 0, 0), Vector3(1, 1, 1)]

    average = average_vector(list_vector)
    assert average[0] == 0.5 and average[1] == 0.5 and average[2] == 0.5

def test_spherical_to_cartesian():
    cartesian = spherical_to_cartesian(theta=numpy.pi / 4, phi=numpy.pi / 4,
                                       x_seg=10, y_seg=5)
    numpy.testing.assert_almost_equal(cartesian[0], 0.2151032)
    numpy.testing.assert_almost_equal(cartesian[1], 0.9697137)
    numpy.testing.assert_almost_equal(cartesian[2], 0.1156969)

def test_cross_vector():
    a, b = Vector3(0, 0, 0), Vector3(1, 1, 1)

    res = cross_vector(a, b)

    assert res[0] == 0 and res[1] == 0 and res[2] == 0

def test_orthonormal_basis():
    n = Vector3(0, 0, 0)

    t, b = orthonormal_basis(n)

    assert t[0] == 0 and t[1] == 0 and t[2] == 0
    assert b[0] == 0 and b[1] == 0 and b[2] == 0

    n = Vector3(0, 1, 0)

    t, b = orthonormal_basis(n)

    assert t[0] == -1 and t[1] == 0 and t[2] == 0
    assert b[0] == 0 and b[1] == 0 and b[2] == -1

def test_geo_hemisphere():
    sphere = geo_hemisphere(centre=Vector3(0, 0, 0),
                            normal=Vector3(0, 0, 1),
                            rayon=5)

    assert sphere is not None