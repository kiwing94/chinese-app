
[app]
title = Chinese Flashcard App
package.name = chineseflashcards
package.domain = org.kiwing
source.dir = .
source.include_exts = py,json,ttf,otf
version = 0.1
requirements = python3==3.10,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.p4a_branch = develop
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1

[python]
exclude_patterns = license,licenses

[android]
android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2