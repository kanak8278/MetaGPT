#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import platform
import fire
import yaml
import os

from metagpt.roles import Architect, Engineer, ProductManager, ProjectManager, QaEngineer, ProjectAnalyzer
from metagpt.software_company import SoftwareCompany

def read_roles_config(roles_config_file: str = "roles_config.yaml"):
    """
    Read the roles config file.
    :return: a dictionary of roles and their attributes.
    """
    
    with open(roles_config_file, "r") as f:
        roles_config = yaml.load(f, Loader=yaml.FullLoader)
    return roles_config

def read_config(config_file: str):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
        print("config: ", config)
    
    return config

async def startup(idea: str, investment: float = 3.0, n_round: int = 5,
                  code_review: bool = False, run_tests: bool = False, roles_config: dict = None):
    """Run a startup. Be a boss."""
    product_manager = roles_config['ProductManager']
    architect = roles_config['Architect']
    project_manager = roles_config['ProjectManager']
    engineer = roles_config['Engineer']
    qa_engineer = roles_config['QaEngineer']    
    
    company = SoftwareCompany()
    company.hire(
        [
        ProductManager(profile=product_manager['profile'], goal=product_manager['goal'], constraints=product_manager['constraints']),
        Architect(profile=architect['profile'], goal=architect['goal'], constraints=architect['constraints']),
        ProjectManager(profile=project_manager['profile'], goal=project_manager['goal'], constraints=project_manager['constraints']),
        Engineer(profile=engineer['profile'], goal=engineer['goal'], constraints=engineer['constraints'], n_borg=5, use_code_review=code_review), 
        ProjectAnalyzer()
        ],
            )
    if run_tests:
        # developing features: run tests on the spot and identify bugs (bug fixing capability comes soon!)
        company.hire([QaEngineer()])
    company.invest(investment)
    company.start_project(idea)
    await company.run(n_round=n_round)
    #  company.debug()
    # company.hire([Engineer()])


def main(config_file: str = "config/parameters.yaml"):
    """
    We are a software startup comprised of AI. By investing in us, you are empowering a future filled with limitless possibilities.
    :param idea: Your innovative idea, such as "Creating a snake game."
    :param investment: As an investor, you have the opportunity to contribute a certain dollar amount to this AI company.
    :param n_round:
    :param code_review: Whether to use code review.
    :return:
    """
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    config = read_config(config_file)
    idea = config['Idea']
    investment = config['Investment']
    n_round = config['N_Rounds']
    code_review = config['Code_Review']
    run_tests = config['Run_Tests']
    roles_config_file = config['Roles_Config_File']
    
    roles_config = read_roles_config(roles_config_file)
    
    asyncio.run(startup(idea, investment, n_round, code_review, run_tests, roles_config))


if __name__ == '__main__':
    fire.Fire(main)
