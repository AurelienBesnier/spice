import openalea.plantgl.all as pgl
from openalea.spice.libspice import Scene, Vec3, VectorFloat, VectorUint
from openalea.spice.common.tools import flatten
from openalea.spice import Scene as sp_scene

def pgl_to_spice(scene: pgl.Scene, sensors=False, setup=True):
    spice_scene = Scene()
    nb_shapes = len(scene)
    i = 1
    tr = pgl.Tesselator()
    for sh in scene:
        print(f"Adding shape {i}/{nb_shapes}", end="\r")
        sh.apply(tr)
        if isinstance(sh.geometry, pgl.Text):
            continue
        sh.geometry = tr.result
        sh.geometry.computeNormalList()
        normals = VectorFloat(flatten(sh.geometry.normalList))
        indices = VectorUint(flatten(sh.geometry.indexList))
        vertices = VectorFloat(flatten(sh.geometry.pointList))
        ambient = Vec3(
            sh.appearance.ambient.red / 255.0,
            sh.appearance.ambient.green / 255.0,
            sh.appearance.ambient.blue / 255.0,
        )
        diffuse = ambient

        material_name = sh.appearance.name
        trans = sh.appearance.transparency
        refl = sh.appearance.ambient.red / 255.0
        specular = sh.appearance.specular.red / 255.0

        # using mat Phong
        illum = 1

        if trans > 0.0:
            illum = 9
            print("Transparent material: " + material_name)

        shininess = sh.appearance.shininess
        if sensors:
            spice_scene.addFaceSensorInfos(
                vertices,
                indices,
                normals,
                "sensor",
                refl,
                specular,
                trans,
                1.0 - shininess,
            )
        else:
            spice_scene.addFaceInfos(
                vertices,
                indices,
                normals,
                diffuse,
                ambient,
                specular,
                shininess,
                trans,
                illum,
                str(sh.id),
                1,
                refl,
                trans,
                1.0 - shininess,
            )
        i += 1
    if setup:
        spice_scene.setupTriangles()

    return spice_scene


def spice_add_pgl(spice_scene: sp_scene, pgl_scene: pgl.Scene, sensors=False, setup=False):
    nb_shapes = len(pgl_scene)
    i = 1
    tr = pgl.Tesselator()
    for sh in pgl_scene:
        print(f"Adding shape to spice scene {i}/{nb_shapes}", end="\r")
        sh.apply(tr)
        if isinstance(sh.geometry, pgl.Text):
            continue
        sh.geometry = tr.result
        sh.geometry.computeNormalList()
        normals = VectorFloat(flatten(sh.geometry.normalList))
        indices = VectorUint(flatten(sh.geometry.indexList))
        vertices = VectorFloat(flatten(sh.geometry.pointList))
        ambient = Vec3(
            sh.appearance.ambient.red / 255.0,
            sh.appearance.ambient.green / 255.0,
            sh.appearance.ambient.blue / 255.0,
            )
        diffuse = ambient

        material_name = sh.appearance.name
        trans = sh.appearance.transparency
        refl = sh.appearance.ambient.red / 255.0
        specular = sh.appearance.specular.red / 255.0

        # using mat Phong
        illum = 1

        if trans > 0.0:
            illum = 9
            print("Transparent material: " + material_name)

        shininess = sh.appearance.shininess
        if sensors:
            spice_scene.addFaceSensorInfos(
                vertices,
                indices,
                normals,
                "sensor",
                refl,
                specular,
                trans,
                1.0 - shininess,
                )
        else:
            spice_scene.addFaceInfos(
                vertices,
                indices,
                normals,
                diffuse,
                ambient,
                specular,
                shininess,
                trans,
                illum,
                str(sh.id),
                1,
                refl,
                trans,
                1.0 - shininess,
                )
        i += 1
    if setup:
        spice_scene.setupTriangles()

    return spice_scene