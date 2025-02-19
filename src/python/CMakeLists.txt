

find_package(Python COMPONENTS Interpreter Development REQUIRED)
# find_package(pybind11 CONFIG REQUIRED)
# Detect the installed nanobind package and import it into CMake
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

# add_library(spice_core MODULE ext_photonmapping.cpp)
# target_link_libraries(spice_core PUBLIC pybind11::module pybind11::opt_size pybind11::thin_lto pybind11::windows_extras
#     tinyobjloader embree OpenMP::OpenMP_CXX pm)
# pybind11_strip(spice_core)

nanobind_add_module(spice ext_photonmapping_nano.cpp)
target_link_libraries(spice PUBLIC tinyobjloader embree OpenMP::OpenMP_CXX pm)
