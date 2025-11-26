import pathlib

from openalea.spice.energy.correct_energy import read_spectrum_file, \
    get_integral_of_band, get_correct_energy_coeff, get_points_calibration

filepath = pathlib.Path(__file__).parent.resolve() / 'data'

def test_energy_correction():
    spec, step, start = read_spectrum_file(str(filepath / 'chambre1_spectrum'))
    integral = get_integral_of_band(range(start,800),range(660, 665), spec)

    assert 0 < integral < 1

    integrals = get_correct_energy_coeff(range(start,800),[{"start": 660, "end": 665}],
                                         str(filepath / 'chambre1_spectrum'))
    for inte in integrals:
        assert 0 < inte

def test_calibration():
    points = get_points_calibration(list_sensors=[],
                           points_calibration_file=str(filepath / 'points_calibration.csv'),
                           divided_spectral_range=[{"start": 655, "end": 665},{"start": 600, "end": 655}])
    assert points is not None
