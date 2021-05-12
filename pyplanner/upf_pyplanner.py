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

import upf_pyplanner.pyplanner as pp

def _upf_action_to_pp(action):
    return pp.Action(action.name,
                     frozenset(action.precondition),
                     frozenset(action.positive_effect),
                     frozenset(action.negative_effect))

def _upf_problem_to_pp(problem):
    actions = [_upf_action_to_pp(x) for x in problem.actions]
    return pp.Problem(actions, frozenset(problem.init), frozenset(problem.goal))

def solve(problem):
    s = pp.Solver()
    return s.solve(_upf_problem_to_pp(problem))

def solve_with_heuristic(problem, h):
    s = pp.Solver(h)
    return s.solve(_upf_problem_to_pp(problem))
