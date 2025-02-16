# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xmore(AutotoolsPackage, XorgPackage):
    """xmore - plain text display program for the X Window System."""

    homepage = "https://cgit.freedesktop.org/xorg/app/xmore"
    xorg_mirror_path = "app/xmore-1.0.2.tar.gz"

    version('1.0.2', sha256='7371631d05986f1111f2026a77e43e048519738cfcc493c6222b66e7b0f309c0')

    depends_on('libxaw')
    depends_on('libxt')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
