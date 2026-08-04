<div align="center">
  <img src="imgs/logo.png" width="320px" alt="Mycode Logo">
</div>

<br>

<div align="center">

[![Last Commit](https://custom-icon-badges.demolab.com/github/last-commit/marsdevx/mycode?logoColor=white&labelColor=2C2C2C&label=Last%20Commit&color=8A2BE2&logo=mark-github)](https://github.com/marsdevx/mycode/commits/main "Last Commit")
[![Platforms](https://custom-icon-badges.demolab.com/static/v1?logoColor=white&labelColor=2C2C2C&label=Platforms&message=macOS%20|%20Linux&color=D32F2F&logo=device-desktop)](https://github.com/marsdevx/mycode "Platforms")
<br>
[![Languages](https://custom-icon-badges.demolab.com/static/v1?logoColor=white&labelColor=2C2C2C&label=Languages&message=Bash%20|%20Python%203.12&color=748ADB&logo=file-code)](https://github.com/marsdevx/mycode "Languages")
[![GitHub API](https://custom-icon-badges.demolab.com/static/v1?logoColor=white&labelColor=2C2C2C&label=API&message=GitHub%20REST%20v3&color=F47F42&logo=code)](https://docs.github.com/en/rest "GitHub API")
[![Shell Support](https://custom-icon-badges.demolab.com/static/v1?logoColor=white&labelColor=2C2C2C&label=Shell&message=Zsh%20%7C%20Bash&color=009688&logo=gnu-bash)](https://github.com/marsdevx/mycode "Shell Support")
[![License](https://custom-icon-badges.demolab.com/static/v1?logoColor=white&labelColor=2C2C2C&label=License&message=MIT&color=00C853&logo=law)](https://github.com/marsdevx/mycode/blob/main/LICENSE "License")

</div>

---

# 📂 MyCode

**Mycode** is a **terminal**-based, **cross-platform** application built with **Python**, designed to help developers efficiently **manage** and **organize** their work projects on **macOS** and **Linux**. With a customizable mycoderc config file, this tool brings **clarity**, **automation**, and **speed** to your **development workflow**.

* Organize your **projects** by **groups** using a simple, readable **config file**.
* Instantly view what **projects** you’ve worked on recently and in what order.
* Open any project in **Visual Studio Code** directly from the **terminal**—with optional **terminal auto-close**.
* Store your **GitHub credentials** locally and securely in a **.json** file for quick reuse.
* Create **new projects** with a single command:
  - Instantly create a private **GitHub** repo,
  - **Clone** it to a local folder,
  - Add **default** **README** and **.gitignore**,

Take control of your dev life with this smart and simple CLI utility that works seamlessly across macOS and Linux!

---

## 🖼️ Preview

<div align="center">
  <img src="imgs/preview1.png" alt="Preview">
  <img src="imgs/preview2.png" alt="Preview">
</div>

---

## 🛠️ Installation

To install this project, Launch the Terminal app on your system, and run the commands below. <br>
  - If a pop-up appears prompting you to download the Xcode Command Line Tools after the first command, click “Download” and then run the first command again.

1. **Install mycode**
```bash
brew tap marsdevx/mycode
brew trust marsdevx/mycode
brew install mycode
```

2. **Set up mycoderc file**
> After the first launch of the program, a default configuration file will be created at: `~/.config/mycode/mycoderc`
```bash
💾 Configuration File Rules:
  - `--add <path>`: Adds all subfolders in the specified path to global projects.
  - `--addspecific <path>`: Adds only the specified folder to global projects.
  - `--remove <path> --from <path>`: Excludes a specific subfolder from a parent path.

🔗 Grouping Projects:
Groups can be defined using `[group:group_name]` syntax in the configuration file.
  - Group-specific rules:
      - `--add <path>`: Adds subfolders to the group only.
      - `--addspecific <path>`: Adds only the specified folder to the group.
      - `--remove <path> --from <path>`: Excludes a specific subfolder in the group.
  - Example:
      [group:example_group]
      {
          --add ~/example/path
          --addspecific ~/example/specific_project
          --remove ~/example/path/excluded_folder --from ~/example/path
      }
```

3. **Set up Shell Autocompletion**
> Completion is installed by Homebrew. Zsh only needs the completion system initialized in `~/.zshrc`:
```bash
autoload -Uz compinit
compinit
```

> Then start a new shell, or run:
```bash
source ~/.zshrc
```

> If you set up completion for an earlier version, remove the old
> `eval "$(register-python-argcomplete mycode)"` line and the hand-written
> `_mycode` function from your shell config — they shadow the installed completion.

---

## 🚀 Usage

- `mycode -s all`  
  Show all global projects defined in your config.

- `mycode -s groups`  
  Show all available groups and the projects within them.

- `mycode -s <group_name>`  
  Show all projects in the specified group.

- `mycode <project_name>`  
  Open the specified project in **Visual Studio Code** and automatically close the terminal.  
  Auto-close is done with AppleScript and requires **macOS** with **iTerm2**. Elsewhere, use `-n`.

- `mycode <project_name> -n`  
  Open the specified project in **VS Code**, but **do not close the terminal**.

- `mycode -c <project_name> <target_dir>`  
  Create a new local project folder and a **private GitHub repository**, generate default files, and push it to GitHub — all in one command.

---

## 📋 License

All the code contained in this repo is licensed under the [MIT License](LICENSE)

```
MIT License

Copyright (c) 2025 marsdevx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⭐ Support

If you like this project, don’t forget to ⭐ **star** it and **follow** me!  
Your **support** helps me create more projects. 🚀  

🔗 **Explore more of my work on [GitHub](https://github.com/marsdevx?tab=repositories) and discover other exciting projects!**