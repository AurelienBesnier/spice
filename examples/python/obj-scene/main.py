from datetime import datetime
import random
import sys
from pathlib import Path

from openalea.spice.libspice_core import *

if __name__ == "__main__":
    n_samples = 12
    n_photons = int(1e6)
    n_estimation_global = 100
    n_photons_caustics_multiplier = 10
    n_estimation_caustics = 50
    final_gathering_depth = 4
    max_depth = 25

    aspect_ratio = 16 / 9
    image_width = 512
    image_height = int(image_width / aspect_ratio)
    image = Image(image_width, image_height)

    lookfrom = Vec3(-800, 100, 0)
    lookat = Vec3(110, 50, 50)
    vup = Vec3(0, -1, 0)
    vfov = 20.0
    dist_to_focus = 5.0
    aperture = 0.01

    # coordinates must be in meters
    camera = Camera(lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    print("Creating Scene..")
    scene = Scene()
    scene.loadModel(str(Path.home() / "models/Sponza/sponza.obj"))
    scene.addPointLight(Vec3(0, -50, 0), 500, Vec3(1, 1, 1))
    scene.build()

    print("Done!")

    print("Building photonMap...")
    integrator = PhotonMapping(
        n_photons,
        n_estimation_global,
        n_photons_caustics_multiplier,
        n_estimation_caustics,
        final_gathering_depth,
        max_depth,
    )

    sampler = UniformSampler(random.randint(0, sys.maxsize))

    integrator.build(scene, sampler, True)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(
        integrator,
        scene,
        image,
        image_height,
        image_width,
        camera,
        n_photons,
        max_depth,
        "photonmap.ppm",
        sampler,
    )
    print("Done!")

    print("Rendering image...")
    image = Image(image_width, image_height)
    Render(
        sampler,
        image,
        image_height,
        image_width,
        n_samples,
        camera,
        integrator,
        scene,
        "output-photonmapping.ppm",
    )

    print("Done!")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    print("You did it !")
