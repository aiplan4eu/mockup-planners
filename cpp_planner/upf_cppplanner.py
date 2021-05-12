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

import upf_cppplanner._upf_cppplanner as cpp

def _upf_action_to_cpp(action):
    return cpp.Action(action.name, action.precondition, action.positive_effect, action.negative_effect)

def _upf_problem_to_cpp(problem):
    actions = [_upf_action_to_cpp(x) for x in problem.actions]
    return cpp.Problem(actions, problem.init, problem.goal)

def solve(problem):
    return cpp.solve(_upf_problem_to_cpp(problem))

def solve_with_heuristic(problem, h):
    return cpp.solve_with_heuristic(_upf_problem_to_cpp(problem), h)
