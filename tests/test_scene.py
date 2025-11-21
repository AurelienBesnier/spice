import pathlib

from openalea.spice import Scene

filepath = pathlib.Path(__file__).parent.resolve()

def test_load_scene_with_lights():
    scene = Scene()
    scene.loadModel(str(filepath / "cornellbox-water2.obj"))
    scene.build()
    assert scene.nLights() == 2
