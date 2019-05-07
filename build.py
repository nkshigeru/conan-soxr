#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.remove_build_if(lambda build: not build.options["soxr:shared"]) # Remove static
    builder.run()
