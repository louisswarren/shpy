import os
import shutil
import glob
import subprocess

def glob_all(paths):
    for path in paths:
        yield from sorted(glob.glob(path))

def cp(*paths, recursive=None):
    *sources, dest = glob_all(paths)
    if len(sources) == 1 and not os.path.isdir(dest):
        if not os.path.isdir(sources[0]) or recursive:
            shutil.copyfile(sources[0], dest)
    else:
        for source in sources:
            if not os.path.isdir(source) or recursive:
                target = os.path.join(dest, os.path.basename(source))
                shutil.copyfile(source, target)
            else:
                raise Exception("Can't copy directory without recursive flag")

def ls(path=None, all=None):
    if all:
        return os.listdir(path)
    return [fname for fname in os.listdir(path) if not fname.startswith('.')]

def mkdir(path, parents=None):
    if parents:
        os.makedirs(path)
    else:
        os.mkdir(path)

def mv(*paths):
    *sources, dest = glob_all(paths)
    if len(sources) == 1 and not os.path.isdir(dest):
        os.rename(sources[0], dest)
    else:
        for source in sources:
            target = os.path.join(dest, os.path.basename(source))
            os.rename(source, target)

def touch(path):
    with open(path, 'a'):
        os.utime(path)

def rm(*paths, recursive=None):
    for path in glob_all(paths):
        if not os.path.isdir(path):
            os.remove(path)
        elif recursive:
            shutil.rmtree(path)
        else:
            raise Exception("Can't remove directory without recursive flag")

def run(*cmdlist, stderr=subprocess.STDOUT):
    return subprocess.check_output(cmdlist, stderr=stderr).decode()
