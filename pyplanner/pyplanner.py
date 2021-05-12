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

from dataclasses import dataclass
from typing import FrozenSet, Callable, List
import heapq
from contextlib import contextmanager
from time import time

@contextmanager
def timing(description: str) -> None:
    start = time()
    yield
    elapsed_time = (time() - start) * 1000

    print(f"{description}: {elapsed_time}ms")


@dataclass
class Action:
    name: str
    precondition: FrozenSet[str]
    positive_effect: FrozenSet[str]
    negative_effect: FrozenSet[str]


@dataclass
class Problem:
    actions: List[Action]
    init: FrozenSet[str]
    goal: FrozenSet[str]


class Solver():
    def __init__(self, heuristic: Callable[[FrozenSet[str]], float] = None):
        self.heuristic = heuristic
        if heuristic is None:
            self.heuristic = lambda x: 0

    def solve(self, problem: Problem) -> List[str]:
        open_list = [(self.heuristic(set(problem.init)), problem.init, [])]
        closed_list = set()
        while open_list:
            _, current, path = heapq.heappop(open_list)
            if current not in closed_list:
                closed_list.add(current)
                if problem.goal.issubset(current):
                    return path

                for act in problem.actions:
                    if act.precondition.issubset(current):
                        child = current.difference(act.negative_effect).union(act.positive_effect)
                        if child not in closed_list:
                            child_f = len(path) + 1 + self.heuristic(set(child))
                            heapq.heappush(open_list, (child_f, child, path+[act.name]))
