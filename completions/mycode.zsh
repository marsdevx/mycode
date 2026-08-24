#    File:         mycode.zsh
#    Project:      mycode
#    Github:       marsdevx
#    Path:         ./completions/mycode.zsh
#
#    Zsh completion for mycode. Source this from ~/.zshrc:
#
#
#    Requires `autoload -Uz compinit bashcompinit; compinit; bashcompinit`
#    earlier in the rc file.

# `register-python-argcomplete mycode` spawns a Python process on every shell
# start. Its output never changes, so cache it and only regenerate when the
# cache is missing.
_mycode_argcomplete_cache="${XDG_CACHE_HOME:-$HOME/.cache}/mycode-argcomplete.zsh"

if [[ ! -s "$_mycode_argcomplete_cache" ]]; then
  mkdir -p "${_mycode_argcomplete_cache:h}"
  register-python-argcomplete mycode > "$_mycode_argcomplete_cache" 2>/dev/null
fi
source "$_mycode_argcomplete_cache"
unset _mycode_argcomplete_cache

# Zsh filters argcomplete's candidates a second time, and that pass is
# case-sensitive -- so `mycode home<TAB>` would still drop "HomeLab" even
# though mycode itself offered it. A per-command `matcher-list` zstyle cannot
# fix this: that style is read before the command is known, so scoping it to
# mycode has no effect and the only working form would change matching for
# every command the user completes. Hand the match spec to compadd instead.
# This is `_python_argcomplete`'s zsh branch verbatim plus the -M option.
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

compdef _mycode mycode
