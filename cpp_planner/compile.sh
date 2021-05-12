#!/bin/sh
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


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PYTHON_VERSION=`python3 -c "import sys; print('%s.%s' %(sys.version_info.major,sys.version_info.minor))"`

g++ -O3 -Wall -shared -std=c++17 -fPIC -I${DIR}/. -I${DIR}/pybind11/include -I/usr/include/python${PYTHON_VERSION} ${DIR}/cppwrapper.cxx ${DIR}/planner.cxx -lpython${PYTHON_VERSION} -o ${DIR}/_upf_cppplanner.so
