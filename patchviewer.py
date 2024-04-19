#!python3 -i

# Copyright (c) 2023 Manos Pitsidianakis <manos@pitsidianak.is>
# Licensed under the EUPL-1.2-or-later.
#
# You may obtain a copy of the Licence at:
# https://joinup.ec.europa.eu/software/page/eupl
#
# SPDX-License-Identifier: EUPL-1.2

import argparse
import tempfile
from mailbox import mbox
import subprocess


class Patch:
    def __init__(self, message, bytes):
        self.message = message
        self.bytes = bytes

    def key(self):
        return self.message["Subject"].replace("\n", "")

    def view(self):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(self.bytes)
            fp.seek(0)
            fp.flush()
            subprocess.run(["bat", "-l", "patch", fp.name])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("file", type=str, help="")

    args = parser.parse_args()
    patches = mbox(args.file, create=False)
    patches = list(
        map(
            lambda k: Patch(patches.get_message(k), patches.get_bytes(k)),
            patches.keys(),
        )
    )
    for i, p in enumerate(patches):
        print(i, p.key())
    print("patches: list")
