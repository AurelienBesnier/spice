from dataclasses import dataclass
from pathlib import Path


@dataclass
class Configuration:
    DIVIDED_SPECTRAL_RANGE: list[dict]
    OPTICAL_PROPERTIES: list[dict]
    NB_PHOTONS: int = 100000
    MAXIMUM_DEPTH: int = 1
    SCALE_FACTOR: float = 1.0
    T_MIN: float = 0.1
    NB_THREAD: int = 4
    BASE_SPECTRAL_RANGE: tuple = (400, 800)
    BACKFACE_CULLING: bool = True
    KEEP_ALL: bool = False
    RENDERING: bool = False
    OPTICAL_PROPERTIES_DIR: Path = ""
    ENVIRONMENT_FILE: Path = ""

    def __init__(
        self,
        nb_photons=100000,
        max_depth=1,
        scale_factor=1.0,
        t_min=0.1,
        nb_thread=8,
        backface_culling=True,
        base_spectral_range=(400, 800),
        divided_spectral_range=None,
        rendering=False,
        keep_all=False,
        optical_properties_dir="",
        environment_file="",
    ):
        self.NB_PHOTONS = nb_photons
        self.MAXIMUM_DEPTH = max_depth
        self.SCALE_FACTOR = scale_factor
        self.T_MIN = t_min
        self.NB_THREAD = nb_thread
        self.BACKFACE_CULLING = backface_culling
        self.BASE_SPECTRAL_RANGE = base_spectral_range
        self.RENDERING = rendering
        self.KEEP_ALL = keep_all
        if divided_spectral_range is None:
            divided_spectral_range = [{"start": 0, "end": 0}]
        self.DIVIDED_SPECTRAL_RANGE = divided_spectral_range
        self.OPTICAL_PROPERTIES_DIR = Path(optical_properties_dir)
        self.ENVIRONMENT_FILE = Path(environment_file)

    def read_file(self, filepath: Path):
        """
        Read all the parameters of simulation in the configuration file

        Parameters
        ----------
        filepath: str
            Name of the configuration file.

        """
        if not filepath.is_file():
            raise FileNotFoundError(filepath)
        # read file
        with open(filepath, encoding="UTF8") as f:
            for line in f:
                if "$" in line:
                    row = line.replace("\n", "").split(" ")
                    if row[0] == "$NB_PHOTONS":
                        self.NB_PHOTONS = int(row[1])
                    elif row[0] == "$MAXIMUM_DEPTH":
                        self.MAXIMUM_DEPTH = int(row[1])
                    elif row[0] == "$OPTICAL_PROPERTIES_DIR":
                        self.OPTICAL_PROPERTIES_DIR = Path(row[1])
                    elif row[0] == "$ENVIRONMENT_FILE":
                        self.ENVIRONMENT_FILE = Path(row[1])
                    elif row[0] == "$SCALE_FACTOR":
                        self.SCALE_FACTOR = float(row[1])
                    elif row[0] == "$RENDERING":
                        if row[1] == "0":
                            self.RENDERING = False
                        if row[1] == "1":
                            self.RENDERING = True
                    elif row[0] == "$KEEP_ALL":
                        if row[1] == "0":
                            self.KEEP_ALL = False
                        if row[1] == "1":
                            self.KEEP_ALL = True
                    elif row[0] == "$T_MIN":
                        self.T_MIN = float(row[1])
                    elif row[0] == "$NB_THREAD":
                        self.NB_THREAD = int(row[1])
                    elif row[0] == "$BACKFACE_CULLING":
                        self.BACKFACE_CULLING = row[1].upper() == "YES"
                    elif row[0] == "$BASE_SPECTRAL_RANGE":
                        self.BASE_SPECTRAL_RANGE = (int(row[1]), int(row[2]))
                    elif row[0] == "$DIVIDED_SPECTRAL_RANGE":
                        nb_bands = int(row[1])
                        self.DIVIDED_SPECTRAL_RANGE.clear()
                        for i in range(nb_bands):
                            start = int(row[(i + 1) * 2])
                            end = int(row[(i + 1) * 2 + 1])
                            self.DIVIDED_SPECTRAL_RANGE.append(
                                {"start": start, "end": end}
                            )
