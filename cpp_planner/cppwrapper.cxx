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

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

#include "planner.hxx"

namespace py = pybind11;

PYBIND11_MODULE(_upf_cppplanner, m) {
    m.doc() = "UPF c++->python example";

    py::class_<cppplanner::Action>(m, "Action")
      .def(py::init<const std::string&,
                    const std::set<std::string>&,
                    const std::set<std::string>&,
                    const std::set<std::string>&>())
      .def_property_readonly("name", &cppplanner::Action::name)
      .def_property_readonly("precondition", &cppplanner::Action::name)
      .def_property_readonly("positive_effect", &cppplanner::Action::name)
      .def_property_readonly("negative_effect", &cppplanner::Action::name);

    py::class_<cppplanner::Problem>(m, "Problem")
      .def(py::init<const std::vector<cppplanner::Action>&,
                    const std::set<std::string>&,
                    const std::set<std::string>&>())
      .def_property_readonly("actions", &cppplanner::Problem::actions)
      .def_property_readonly("init", &cppplanner::Problem::init)
      .def_property_readonly("goal", &cppplanner::Problem::goal);

    m.def("solve",
          py::overload_cast<cppplanner::Problem>(&cppplanner::solve),
          "Solves a problem without heuristic");
    m.def("solve_with_heuristic",
          py::overload_cast<cppplanner::Problem, std::function<double(std::set<std::string>)>>(&cppplanner::solve),
          "Solves a problem with heuristic");

}
