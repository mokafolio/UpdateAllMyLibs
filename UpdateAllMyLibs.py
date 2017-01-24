#!/usr/bin/env python3

import os
import subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(description="Updates all dem moka libs!")
parser.add_argument("root", default=".")
args = parser.parse_args()

cwd = os.path.abspath(args.root)
os.chdir(cwd)

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
