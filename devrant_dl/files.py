import os
import json


def write(obj, basepath, file_base, txt="/", js="/"):
    # Check if output dir needs to be created
    if not os.path.exists(basepath):
        os.mkdir(basepath)

    # Check if output dir needs to be created
    if not os.path.exists(basepath + txt):
        os.mkdir(basepath + txt)

    # Check if output dir needs to be created
    if not os.path.exists(basepath + js):
        os.mkdir(basepath + js)

    # Write txt
    with open(basepath + txt + file_base + ".txt", "w") as fp:
        fp.write(str(obj))
        fp.close()

    # Write json
    with open(basepath + js + file_base + ".json", "w") as fp:
        fp.write(json.dumps(obj.dict()))
        fp.close()
