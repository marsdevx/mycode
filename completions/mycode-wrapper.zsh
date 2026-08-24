#    File:         mycode-wrapper.zsh
#    Project:      mycode
#    Github:       marsdevx
#    Path:         ./completions/mycode-wrapper.zsh
#
#    The zsh completion functions for mycode, with no registration and no
#    assumptions about how argcomplete's driver got loaded. Two callers share
#    this file: completions/mycode.zsh (sourced from ~/.zshrc by non-Homebrew
#    installs) and the Homebrew formula, which bakes it into the installed
#    _mycode. Keep it free of anything specific to either.
#
#    Expects `__python_argcomplete_run` to already be defined, and
#    `is-at-least` to be autoloadable.

# Zsh filters argcomplete's candidates a second time, and that pass is
# case-sensitive -- `mycode home<TAB>` would drop "HomeLab" even though mycode
# itself already offered it. A per-command `matcher-list` zstyle cannot fix
# that: the style is read before the command is known, so the only form that
# takes effect would change matching for every command the user completes.
# Hand the match spec to compadd via -M instead. This is
# `_python_argcomplete`'s zsh branch plus that one option.
_mycode_argcomplete() {
  local IFS=$'\013'
  local -a completions nosort nospace
  completions=($(IFS="$IFS" \
      COMP_LINE="$BUFFER" \
      COMP_POINT="$CURSOR" \
      _ARGCOMPLETE=1 \
      _ARGCOMPLETE_SHELL="zsh" \
      _ARGCOMPLETE_SUPPRESS_SPACE=1 \
      __python_argcomplete_run "${words[1]}"))
  if is-at-least 5.8; then
    nosort=(-o nosort)
  fi
  if [[ "${completions-}" =~ ([^\\]): && "${match[1]}" =~ [=/:] ]]; then
    nospace=(-S '')
  fi
  _describe "${words[1]}" completions "${nosort[@]}" "${nospace[@]}" \
      -M 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}'
}

_mycode() {
  # `-c <project_name> <target_dir>`: the name is freeform, the target is a path.
  if (( CURRENT > 2 )) &&
      [[ ${words[CURRENT-2]} == --create || ${words[CURRENT-2]} == -c ]]; then
    _files
    return
  fi

  if (( CURRENT > 1 )) &&
      [[ ${words[CURRENT-1]} == --create || ${words[CURRENT-1]} == -c ]]; then
    return
  fi

  _mycode_argcomplete "$@"
}
