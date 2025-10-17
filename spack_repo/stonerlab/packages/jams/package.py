# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Jams(CMakePackage):
    """Joe's Awesome Magnetic Simulator is an atomistic magnetisation dynamics code with CUDA GPU acceleration."""

    homepage = "https://github.com/stonerlab/jams"
    git = "https://github.com/stonerlab/jams.git"
    url = "https://github.com/stonerlab/jams/archive/refs/tags/v2.21.0.tar.gz"
    
    maintainers("drjbarker")

    license("MIT", checked_by="drjbarker")

    version("master", branch="master")
    version("2.21.0", sha256="7c9a41381be6a03e6c642a96e85f761f41a2790f7e5d3e6d2876bdccc1cb6c0f")

    variant("cuda", default=False, description="Enable CUDA support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on("cuda", type="build", when="+cuda")

    depends_on("blas")
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

