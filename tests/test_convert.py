from openalea.plantgl.all import Sphere, Scene, Shape

from openalea.spice.common.convert import pgl_to_spice
from openalea.spice.simulator import Simulator


def test_plantgl_to_spice():
    sim = Simulator()
    assert sim.scene.nVertices() == 0
    pgl_sc = Scene([Shape(Sphere(5))])
    pgl_to_spice(pgl_sc, sim)
    assert sim.scene.nVertices() > 0
