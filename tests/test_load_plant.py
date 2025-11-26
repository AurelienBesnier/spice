import pathlib

from openalea.spice import Scene, Vec3

from openalea.spice.loader.load_plant import add_lpy_file_to_scene

filepath = pathlib.Path(__file__).parent.resolve() / 'data'

def test_add_lpy_file_to_scene():
    sc = Scene()
    tr = {}
    list_sh_id = add_lpy_file_to_scene(sc, str(filepath / 'rose-simple4.lpy'),
                                       120, tr, Vec3(0,0,0))

    assert list_sh_id is not None