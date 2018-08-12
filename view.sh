# Viewer for Linux
if [ "$(which xdg-open)" != ""  ]; then
     xdg-open "$@"
     exit 0
fi

# Viewer for OS X
if [ "$(which open)" != ""  ]; then
     open "$@"
     exit 0
fi
