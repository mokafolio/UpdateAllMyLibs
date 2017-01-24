#!/usr/bin/env python3

import os
import subprocess
import shutil

cwd = os.getcwd()

def pullLib(_name, _bInstall):
    if os.path.exists(_name):
        os.chdir(os.path.join(cwd, _name))
        output = subprocess.check_output(["git", "pull", "origin", "master"])
        print(output)
        shutil.rmtree("build")
        os.mkdir("build")
        os.chdir(os.path.join(cwd, _name, "build"))
        output = subprocess.check_output(["cmake", ".."])
        print(output)
        output = subprocess.check_output(["make", "install"])
        print(output)
        os.chdir(cwd)

pullLib("Stick", True)
pullLib("Crunch", True)
pullLib("Scrub", True)
pullLib("Brick", True)
pullLib("Luanatic", True)
pullLib("CrunchLua", True)
pullLib("Paper", True)
pullLib("PaperLua", True)
pullLib("Pic", True)
#pullLib("Pigment", True)
