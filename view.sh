# Viewer for Linux

if [ "$(which evince)" != ""  ]; then
     evince --fullscreen "$@"
     exit 0
fi

# For ChromeOS, because xdg-open not available...

# Viewer for OS X
if [ "$(which open)" != ""  ]; then
     open "$@"
     exit 0
fi
