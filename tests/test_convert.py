from openalea.plantgl.all import Sphere, Scene, Shape, Text
from openalea.plantgl.scenegraph import Material

from openalea.spice.common.convert import pgl_to_spice, spice_add_pgl
from openalea.spice.simulator import Simulator


def test_plantgl_to_spice():
    sim = Simulator()
    assert sim.scene.nVertices() == 0
    pgl_sc = Scene([Shape(Sphere(5), Material(transparency=0.6)), Text("test")])
    pgl_to_spice(pgl_sc, sim)
    assert sim.scene.nVertices() > 0

    # With Adding sensors
    pgl_sc = Scene([Shape(Sphere(5), Material(transparency=0.6)), Text("test")])
    pgl_to_spice(pgl_sc, sim, sensors=True, setup=True)
    assert sim.scene.nVertices() > 0

    # Test adding PGL scene directly
    spice_add_pgl(sim, pgl_sc)
    assert sim.scene.nVertices() > 0

    spice_add_pgl(sim, pgl_sc, sensors=True, setup=True)
    assert sim.scene.nVertices() > 0