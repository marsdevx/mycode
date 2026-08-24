#    File:         mycode.zsh
#    Project:      mycode
#    Github:       marsdevx
#    Path:         ./completions/mycode.zsh
#
#    Zsh completion for mycode, for installs that did not come from Homebrew.
#    Source this from ~/.zshrc after `compinit`:
#
#        source /path/to/mycode/completions/mycode.zsh
#
#    Homebrew installs a self-contained _mycode instead and needs none of this.

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

# The completion functions themselves live next door, shared verbatim with the
# Homebrew formula so the two cannot drift apart.
source "${0:A:h}/mycode-wrapper.zsh"

compdef _mycode mycode
