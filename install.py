# Copyright 2021 AIPlan4EU project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

    # Install cppplanner
    if os.path.exists(os.path.join(bindings_dir, 'upf_cppplanner')):
        print('cppplanner already installed!')
    else:
        os.system('bash ' + os.path.join(dir_path, 'cpp_planner', 'compile.sh'))
        shutil.copytree(os.path.join(dir_path, 'cpp_planner'), os.path.join(bindings_dir, 'upf_cppplanner'))
        print('cppplanner installed successfully!')
