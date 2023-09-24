#!/usr/bin/env python
# coding: utf-8


import subprocess
import os
if __name__ == "__main__":
    import Install
    Install.installFunc()


if __name__ == "__main__":
    path = os.path.abspath('Stream.py')
    repertoire_parent = os.path.dirname(path)
    file_path = os.path.join(repertoire_parent, 'Stream.py')

    subprocess.run(["streamlit", "run", file_path])
    process = subprocess.Popen(["streamlit", "run", file_path])
