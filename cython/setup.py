import sys
from glob import glob
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

from Cython.Build import cythonize

# ---- platform flags ----
extra_compile_args = []
extra_link_args = []

if sys.platform == "darwin":  # macOS
    extra_compile_args = ["-Wno-unreachable-code"]
    extra_link_args = ["-Wl,-rpath,@loader_path/"]
elif sys.platform == "linux":  # Linux
    extra_compile_args = ["-Wno-unreachable-code", "-O2"]  # Add optimizations on Linux
    extra_link_args = []
elif sys.platform == "win32":  # Windows
    extra_compile_args = ["/EHsc"]  # Exception handling in MSVC for C++ (optional)
    extra_link_args = []

# ---- config ----
ROOT = Path(__file__).parent
PACKAGE = "cython_lib"  # DO NOT use "cython" as it conflicts with the Cython package
PKG_DIR = ROOT / PACKAGE

pyx_files = glob(str(PKG_DIR / "**/*.pyx"), recursive=True)


def to_module(path: str) -> str:
    """Convert a file path to a Python module path.

    e.g. cython/string/foo.pyx -> cy.string.foo
    """
    rel = Path(path).with_suffix("").relative_to(PKG_DIR)
    return PACKAGE + "." + ".".join(rel.parts)


class BuildExtMakeDirs(build_ext):
    def build_extension(self, ext):
        """Create directories for the extension if they do not exist."""
        if self.inplace or getattr(self, "editable_mode", False):
            out = Path(self.get_ext_fullpath(ext.name))
            out.parent.mkdir(parents=True, exist_ok=True)
        super().build_extension(ext)


extensions = [
    Extension(
        name=to_module(pyx_file),
        sources=[pyx_file],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language="c",
    )
    for pyx_file in pyx_files
]

setup(
    name=PACKAGE,
    version="0.1.0",
    cmdclass={"build_ext": BuildExtMakeDirs},
    ext_modules=cythonize(
        extensions,
        language_level="3",
        compiler_directives={"boundscheck": False, "wraparound": False},
    ),
)
