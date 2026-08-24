#    File:         mycode.py                                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣘⠿⠿⠿⢆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿    #
#                                                                               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣮⣭⣭⣴⣿⣿⣿⣿⣿⣿    #
#    Project:      mycode                                                       ⣿⣿⣿⣿⠿⠿⠿⠿⠿⠏⠻⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠟⠹⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿    #
#    Github:       marsdevx                                                     ⣿⣿⣿⣇⠀⢀⣀⣀⢀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠅⢀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠈⣿⣿⣿⣿    #
#                                                                               ⣿⣿⣿⣿⣷⡘⣿⣿⡇⢀⣤⣤⣤⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣀⣐⡀⡀⣿⣿⣿⡏⣼⣿⣿⣿    #
#    Created:      15:51   21/05/2025                                           ⣿⣿⣿⣿⣿⣿⣾⣿⣻⣝⣛⣛⣛⣫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠿⠿⠿⢟⣴⢿⣿⣴⣿⣿⣿⣿⣿    #
#    Updated:      19:07   21/05/2025                                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                                               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    Path:         ./mycode.py                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                                               ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⠟⣋⣍⣛⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #

import os
import json
import parse
import argparse
import subprocess
import argcomplete

# create_proj pulls in `requests`, which costs ~175ms to import. Only -c needs
# it, so it is imported inside create() instead of here.
github_path = os.path.expanduser("~/.config/mycode/config.json")

def check_json():
  if not os.path.exists(github_path):
    data = {
      "github": {
        "username": "",
        "token": ""
      }
    }

    with open(github_path, "w") as f:
      json.dump(data, f, indent=2)

def create(project_name, target_dir):
  import create_proj as cp

  target_dir = os.path.expanduser(target_dir)
  if not os.path.isdir(target_dir):
      print(f"Target directory does not exist: {target_dir}")
      return

  with open(github_path) as f:
    config_file = json.load(f)
  username = config_file["github"].get("username", "").strip()
  token = config_file["github"].get("token", "").strip()

  cp.create_project(project_name, target_dir, username, token)

def open_project(project_name, not_close):
  all_projects = parse.collect_projects(parse.config["projects_dir"], parse.config["specific_projects"], parse.config["remove_rules"])
  if project_name in all_projects:
    project_path = all_projects[project_name]
    print("\033[0;96mEnjoy your work, sir.\033[0m")
    print(f"Opening project '{project_name}'...")
    subprocess.run(["code", project_path])
    if not not_close:
      print("Closing terminal...")
      script = '''
      tell application "iTerm2"
          tell the current window
              close
          end tell
      end tell
      '''
      subprocess.run(["osascript", "-e", script])
  else:
    print(f"Project '{project_name}' not found.")

desc = ("✨ Manage and organize your projects with mycode ✨\n\n"
"📂 Requires a configuration file located at: `~/.config/mycode/mycoderc`\n\n"
"💾 Configuration File Rules:\n"
"  - `--add <path>`: Adds all subfolders in the specified path to global projects.\n"
"  - `--addspecific <path>`: Adds only the specified folder to global projects.\n"
"  - `--remove <path> --from <path>`: Excludes a specific subfolder from a parent path.\n\n"
"🔗 Grouping Projects:\n"
"Groups can be defined using `[group:group_name]` syntax in the configuration file.\n"
"  - Group-specific rules:\n"
"      - `--add <path>`: Adds subfolders to the group only.\n"
"      - `--addspecific <path>`: Adds only the specified folder to the group.\n"
"      - `--remove <path> --from <path>`: Excludes a specific subfolder in the group.\n"
"  - Example:\n"
"      [group:example_group]\n"
"      {\n"
"          --add ~/example/path\n"
"          --addspecific ~/example/specific_project\n"
"          --remove ~/example/path/excluded_folder --from ~/example/path\n"
"      }\n\n"
"🛠  Commands:\n"
"  - `mycode -s all`: Show all global projects.\n"
"  - `mycode -s groups`: Show all groups and their projects.\n"
"  - `mycode -s <group_name>`: Show all projects in the specified group.\n"
"  - `mycode <project_name>`: Open the specified project in VS Code.\n"
"  - `mycode <project_name> -n`: Open the project without closing the terminal.\n"
"  - `mycode -c <project_name> <target_dir>`: Create a new project and repository.\n\n"
"🎯 Shell Autocompletion:\n"
"  - Autocompletion is supported for Zsh and Bash, and is installed for you.\n"
"  - Zsh only needs the completion system initialized in ~/.zshrc:\n\n"
"      autoload -Uz compinit\n"
"      compinit\n\n"
"  - Then start a new shell, or run:\n"
"      source ~/.zshrc\n\n"
"  - No `register-python-argcomplete` line and no hand-written `_mycode`\n"
"    function are needed. If you added those for an earlier version, remove\n"
"    them -- they will shadow the installed completion.\n")

def main():
  check_json()
  prog = argparse.ArgumentParser(prog="mycode", add_help=False)

  # Completers are callables, not prebuilt lists: a list would make every run
  # scan the project tree just to build the parser, even when not completing.
  prog.add_argument("-s", "--show", nargs=1, help="Show the data list").completer = lambda **kw: parse.get_group()
  prog.add_argument("-c", "--create", nargs=2, metavar=("project_name", "target_dir"), help="Create a new project and repository")
  prog.add_argument("project", nargs="?", help="Name of project to open").completer = lambda **kw: parse.get_proj()
  prog.add_argument("-n", "--not-close", action="store_true", help="Don't close terminal after opening project")
  prog.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)

  # argcomplete's default validator is a case-sensitive startswith(), so
  # `mycode home<TAB>` would never offer "HomeLab". Fold both sides.
  def match_any_case(completion, prefix):
    return completion.lower().startswith(prefix.lower())

  argcomplete.autocomplete(prog, always_complete_options=False, validator=match_any_case)
  args = prog.parse_args()

  if args.create:
    project_name, target_dir = args.create
    create(project_name, target_dir)
    all_projects = parse.collect_projects(parse.config["projects_dir"], parse.config["specific_projects"], parse.config["remove_rules"])
    if project_name in all_projects:
        open_project(project_name, False)
    if project_name not in all_projects:
      print("\033[0;96mEnjoy your work, sir.\033[0m")
  elif args.show:
    show_arg = args.show[0]
    if show_arg == "all":
      parse.print_proj()
      print("\033[0;96mHere are your projects, sir\033[0m")
    elif show_arg == "groups":
      parse.print_groups()
      print("\033[0;96mHere are your projects, sir\033[0m")
    elif show_arg in parse.config["groups"]:
      parse.print_group(show_arg)
      print("\033[0;96mHere are your projects, sir\033[0m")
    else:
      print(f"Group '{show_arg}' not found.")
  elif args.project:
    open_project(args.project, args.not_close)
  if args.help or (not args.create and not args.show and not args.project):
    print(desc)
    return

if __name__ == "__main__":
  main()