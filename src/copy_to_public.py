import os
import shutil


def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    def _copy_static(src, dst):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            if os.path.isfile(src_path):
                print(f"Copying file {src_path} to {dst_path}")
                shutil.copy(src_path, dst_path)
            elif os.path.isdir(src_path):
                os.mkdir(dst_path)
                _copy_static(src_path, dst_path)

    _copy_static(src, dst)
