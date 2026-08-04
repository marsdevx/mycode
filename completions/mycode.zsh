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

  _python_argcomplete "$@"
}

compdef _mycode mycode
