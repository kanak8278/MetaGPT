import yaml
 
import yaml

def read_config(config_file: str):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config


# def read_roles_config(roles_config_file: str):
#     with open(roles_config_file, 'r') as f:
#         roles_config = yaml.safe_load(f)
#     return roles_config



def read_roles_config(roles_config_file: str = "roles_config.yaml"):
    """
    Read the roles config file.
    :return: a dictionary of roles and their attributes.
    """
    
    with open(roles_config_file, "r") as f:
        roles_config = yaml.safe_load(f)
    return roles_config


config = read_config('parameters.yaml')

print(config)

idea = config['Idea']
investment = config['Investment']
n_rounds = config['N_Rounds']
code_review = config['Code_Review']
run_tests = config['Run_Tests']
roles_config_file = config['Roles_Config_File']

roles_config = read_roles_config(roles_config_file)
print(roles_config)

# print(read_roles_config("roles_config.yaml"))