import os

def ls(path=None, all=None):
    if all:
        return os.listdir(path)
    return [fname for fname in os.listdir(path) if not fname.startswith('.')]

def mv(*paths):
    *sources, dest = paths
    if len(sources) == 1 and not os.path.isdir(dest):
        os.rename(sources[0], dest)
    else:
        for source in sources:
            os.rename(source, os.path.join(dest, os.path.basename(source)))
