import os
import shutil
from pysmt.cmd.installers.base import solver_install_site


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bindings_dir = os.path.expanduser(solver_install_site(plat_specific=True))

    # Install pyplanner
    if os.path.exists(os.path.join(bindings_dir, 'upf_pyplanner')):
        print('pyplanner already installed!')
    else:
        shutil.copytree(os.path.join(dir_path, 'pyplanner'), os.path.join(bindings_dir, 'upf_pyplanner'))
        print('pyplanner installed successfully!')
