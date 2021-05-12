// Copyright 2021 AIPlan4EU project
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <string>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <tuple>
#include <optional>
#include <functional>

namespace cppplanner
{
  class Action
  {
  public:
    Action(const std::string& name,
           const std::set<std::string>& precondition,
           const std::set<std::string>& positive_effect,
           const std::set<std::string>& negative_effect);

    const std::string& name() const;

    const std::set<std::string>& precondition() const;

    const std::set<std::string>& positive_effect() const;

    const std::set<std::string>& negative_effect() const;

    bool operator<(const Action& oth) const;

  private:
    std::string name_;
    std::set<std::string> precondition_;
    std::set<std::string> positive_effect_;
    std::set<std::string> negative_effect_;
  };


  class Problem
  {
  public:
    Problem(const std::vector<Action>& actions,
            const std::set<std::string>& init,
            const std::set<std::string>& goal);

    const std::vector<Action>& actions() const;

    const std::set<std::string>& init() const;

    const std::set<std::string>& goal() const;

  private:
    std::vector<Action> actions_;
    std::set<std::string> init_;
    std::set<std::string> goal_;
  };

  std::optional<std::vector<std::string>> solve(Problem problem, std::function<double(std::set<std::string>)> heuristic);

  std::optional<std::vector<std::string>> solve(Problem problem);

}
