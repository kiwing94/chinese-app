
[app]
title = Chinese Flashcard App
package.name = chineseflashcards
package.domain = org.kiwing
source.dir = .
source.include_exts = py,json,ttf,otf
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
osx.python_version = 3
android.permissions = INTERNET
android.pip_extra_args = --break-system-packages
[buildozer]
log_level = 2
warn_on_root = 1

[python]
# (list) List of patterns to exclude from the package
exclude_patterns = license,licenses

[android]
# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Target API
android.target = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (crash-safe)
android.theme = '@android:style/Theme.Material.Light'

# (str) Presplash screen used
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png
