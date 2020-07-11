import platform
import sys
platform = platform.system()

if "Windo" in str(platform):
    print("gottem")
print(platform)