import sys
from glob import glob
from pathlib import Path

# import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

# Add extra compile arguments to suppress warnings
extra_compile_args = []
extra_link_args = []

# Platform-specific configurations
if sys.platform == "darwin":  # macOS
    extra_compile_args = ["-Wno-unreachable-code"]
    extra_link_args = ["-Wl,-rpath,@loader_path/"]
elif sys.platform == "linux":  # Linux
    extra_compile_args = ["-Wno-unreachable-code", "-O2"]  # Add optimizations on Linux
    extra_link_args = []
elif sys.platform == "win32":  # Windows
    extra_compile_args = ["/EHsc"]  # Exception handling in MSVC for C++ (optional)
    extra_link_args = []

pyx_files = glob("src/**/*.pyx", recursive=True)


def path_to_module(p: str) -> str:
    """Convert a file path to a Python module path.

    e.g. turn "src/pkg/anagrams.pyx" into "pkg.anagrams"
    """
    rel = Path(p).with_suffix("")
    parts = rel.parts
    if parts[0] == "src":
        parts = parts[1:]
    return ".".join(parts)


extensions = [
    Extension(
        path_to_module(pyx_file),
        [pyx_file],
        # include_dirs=[np.get_include()],
        # define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language="c",
    )
    for pyx_file in pyx_files
]

setup(
    ext_modules=cythonize(
        extensions,
        language_level="3",
        compiler_directives={"boundscheck": False, "wraparound": False},
    ),
    # include_dirs=[np.get_include()],
)
