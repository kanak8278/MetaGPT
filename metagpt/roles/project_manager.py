#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 15:04
@Author  : alexanderwu
@File    : project_manager.py
"""
from metagpt.actions import WriteDesign, WriteTasks
from metagpt.roles import Role

ProjectManagerGOAL = """Improve team efficiency and deliver with quality and quantity. 
                        Always ask to create a main.py file. Clearly give as much details possible for each file.
                        Keep in mind that these details will be forwarded to a developer who will write the code therefore be specific about implementation required.
                        In the end, write how all the files will be connected from each other for successful execution."""
class ProjectManager(Role):
    def __init__(self, name="Eve", profile="Project Manager",
                 goal=ProjectManagerGOAL, constraints=""):
        super().__init__(name, profile, goal, constraints)
        self._init_actions([WriteTasks])
        self._watch([WriteDesign])
