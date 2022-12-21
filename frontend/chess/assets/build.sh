# This assumes poetry, gets where poetry stores its dependencies
# VIRTUAL_ENV_PATH=`poetry show -v 2> /dev/null | head -n1 | cut -d ' ' -f 3`
# SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && (pwd -W 2> /dev/null || pwd))

# HAVE TO SET THE PATH SEPARATOR, WINDOWS IT IS ';', LINUX AND MAC IT IS ':'
PATH_SEP=":"
UNAME=$( command -v uname)

case $( "${UNAME}" | tr '[:upper:]' '[:lower:]') in
  linux*)
    printf 'linux\n'
    ;;
  darwin*)
    printf 'darwin\n'
    ;;
  msys*|cygwin*|mingw*)
    # or possible 'bash on windows'
    printf 'windows\n'
    PATH_SEP=";"
    ;;
  nt|win*)
    printf 'windows\n'
    PATH_SEP=":"
    ;;
  *)
    printf 'unknown\n'
    ;;
esac

# Clean up anything just in case
rm -rf dist
rm -rf build

# And go...
pyinstaller \
--windowed \
--onefile \
-n chessgame \
--add-data "${SCRIPT_DIR}/chess/assets/bishop.png${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/boo.mp3${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/clack.mp3${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/correct.wav${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/gameDefinitions.json${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/Hide.png${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/LoginButtonImage.png${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/queen.png${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/rook.png${PATH_SEP}assets" \
--add-data "${SCRIPT_DIR}/chess/assets/Show.png${PATH_SEP}assets" \
${SCRIPT_DIR}/entry_point.py
