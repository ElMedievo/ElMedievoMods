#!/bin/bash

[ -e dist ] && rm -r dist
[ -e build ] && rm -r build

pyinstaller elmedievo_mods_win32.spec

mkdir dist/elmedievo_mods

cp -r ../icons dist/elmedievo_mods

mv dist/elmedievo_mods.exe dist/elmedievo_mods
