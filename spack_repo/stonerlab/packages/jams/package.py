# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Jams(CMakePackage):
    """Joe's Awesome Magnetic Simulator is an atomistic magnetisation dynamics code with CUDA GPU acceleration."""

    homepage = "https://github.com/stonerlab/jams"
    git = "https://github.com/stonerlab/jams.git"
    
    maintainers("drjbarker")

    license("MIT", checked_by="drjbarker")

    version("master", branch="master")
    version("2.22.0", tag="v2.22.0", commit="e834b2242ce0f69ee9a5c5c2eefa815857d54e68")

    variant("cuda", default=False, description="Enable CUDA support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on("cuda", type="build", when="+cuda")

    depends_on("blas")
    # On macOS openblas has terrible trouble compiling so we depend on this
    # shim to use accelerate instead. The user can override it if they
    # really want to by specing a different blas package.
    depends_on("veclibfort", when="platform=darwin")

    depends_on("hdf5")
    depends_on("fftw")
    depends_on("git")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("CMAKE_POLICY_VERSION_MINIMUM", "3.10"),
            self.define_from_variant("JAMS_BUILD_CUDA", "cuda"),
        ]

        return args

