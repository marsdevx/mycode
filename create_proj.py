#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    File:         create_proj.py                             ⡇⣶⠆⣴⣶⡶⢠⡖⡴⣴⠂⢄⣒⡂⡶⣐⣒⣒⣒⡂⢲⡆⢲⣦⠐⣶⣶⣶⣶⣶⠀⡔⣶⣶⣶⡶⢠⣶⡀⡆⣶⡶⠶⡀⢢⢶⡖⡀⠄⡲⣶⣶⣖⡆⠠⢰⣶⣆⢶⡄⢲⢸   #
#                                                             ⡇⡟⡆⣿⣿⡇⣾⠃⣿⠃⢢⣿⣿⡇⣧⣿⣿⣿⣿⣷⡀⣿⢠⢻⣆⠜⣿⣿⣯⣿⡇⢧⢻⠛⣿⢃⣾⣿⡅⢧⣶⣿⣿⣿⣔⠕⠳⢳⡌⢄⠙⣿⣿⡼⢂⢃⢿⣿⡜⡇⣇⢸   #
#    Project:      mycode                                     ⡇⢇⡇⣿⣿⠀⣿⠸⡟⢀⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣧⡸⣇⣧⢿⣄⠸⣿⣿⣻⣿⢸⡜⡤⣿⢸⣿⣿⠇⣸⣿⣿⣿⣿⣿⣧⣻⡄⢿⣄⠄⠘⣿⣿⣼⡘⢸⣿⡇⡇⢸⢸   #
#    Github:       marsdevx                                   ⡇⢸⡇⠟⣿⠀⡟⠀⢁⣾⣿⡿⢿⣛⡸⠿⠯⠿⣿⣛⡿⣷⣝⢞⢷⡙⢦⠈⢿⣿⣿⡀⣷⡄⠞⣾⣿⡿⣰⣿⣿⣿⡿⣿⣻⠿⠯⠿⠦⣝⢳⠄⠈⢿⡆⡇⢺⣿⡇⣇⢸⢸   #
#                                                             ⡇⢸⡇⠠⣿⡀⡇⢀⣿⠿⠉⠈⠁⢀⣀⠀⠀⠀⠀⠀⠉⠓⢿⣯⣏⠻⣦⣕⠄⠙⢿⣧⠘⣿⣦⣻⣿⣿⣿⣿⣿⠗⠋⠁⠀⣀⠀⠀⠀⠀⠀⠉⠐⠀⠃⡃⢸⣿⡇⢸⢸⣸   #
#    Created:      12:44   22/05/2025                         ⡇⡘⣿⠀⢺⡇⠃⢈⠁⠀⢠⣴⠀⣬⡍⠀⠀⠀⢠⣦⠀⣤⡐⢌⢿⣷⣬⣻⢷⣥⣀⠘⠳⡘⣿⣿⣿⣿⣿⠟⠅⣠⡔⢀⣬⡅⠀⠀⠀⣰⣦⠰⣤⠀⠀⠁⢸⡿⢀⡟⣿⢸   #
#    Updated:      12:44   22/05/2025                         ⡇⡇⣿⡆⠈⢿⡀⢾⣿⣄⠸⣿⠸⣿⣧⠀⠀⢀⣾⣯⠶⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⣌⣻⣿⣿⣿⣿⣴⣿⣧⢸⣿⣇⠀⠀⣠⣿⡷⠶⡟⢀⣾⠃⣾⠃⣼⠃⣿⢸   #
#                                                             ⡇⣇⠿⣷⠐⡌⢧⠸⣿⣿⣷⢽⠣⠹⢿⣿⣿⡿⠿⢋⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡂⠹⠿⣿⣿⣿⠿⠣⣪⢵⣿⠇⣸⠃⢠⡟⣰⣿⢸   #
#    Path:         ./create_proj.py                           ⡇⣿⢠⣿⡇⢹⡆⢣⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣴⠁⢰⢸⢱⢸⣿⢸   #
#                                                             ⡇⣿⡼⢹⣿⡀⢻⣮⡂⠻⣿⣿⣿⡿⣽⣟⡾⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣻⢯⡿⣽⣿⣿⠟⠑⢠⡆⠐⠇⠎⣾⣿⢸   #
#                                                             ⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾   #

import os
import json
import requests
import subprocess

github_path = os.path.expanduser("~/.config/mycode/config.json")

def input_conf():
  with open(github_path) as f:
    config_file = json.load(f)

  username = input("Enter your GitHub username: ")
  token = input("Enter your GitHub token: ")
  config_file["github"]["username"] = username
  config_file["github"]["token"] = token

  with open(github_path, "w") as f:
    json.dump(config_file, f, indent=2)

def create_github_repo(repo_name, username, token):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {"name": repo_name, "private": True}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Successfully created private repository: {repo_name}")
        return f"https://github.com/{username}/{repo_name}.git"
    elif response.status_code == 422:
        print(f"Repository {repo_name} already exists on GitHub.")
        return f"https://github.com/{username}/{repo_name}.git"
    else:
        print(f"Error creating repository: {response.json()}")
        input_conf()
        return None

def create_project(project_name, target_dir, username, token):
    repo_url = create_github_repo(project_name, username, token)
    if not repo_url:
        print("Failed to create GitHub repository. \n Please rerun your command.")
        return

    project_path = os.path.join(target_dir, project_name)

    try:
        subprocess.run(["git", "clone", repo_url, project_path], check=True)
        os.chdir(project_path)
        with open(".gitignore", "w") as gitignore:
            gitignore.write("temp\nimpr.md\n__pycache__\n.vscode\n.DS_Store")
        with open("README.md", "w") as readme:
            readme.write("# Repository Status\n\nThis Git repository is currently in beta version. Features and functionality are subject to change. Feedback and contributions are welcome!\n")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "chore: initial commit with README and .gitignore"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Project {project_name} has been created and initialized.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None