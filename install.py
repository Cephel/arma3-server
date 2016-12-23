import os
import shutil
import subprocess
import urllib.request
import encodings.idna
import zipfile
import ctypes
import sys


isadmin = ctypes.windll.shell32.IsUserAnAdmin();

if not isadmin:
	input("Warning, you are not running this script as an admin. Some manual steps are required later if you choose to continue. Press any key to continue . . .")

input("Warning, this will completely reinstall the server, including deleting all game and server files! Press any key to continue . . .")
input("Warning, if you want to just update the server, run 'update-game.cmd' instead. Last chance to stop! Press any key to continue . . .")

def mkdir(path):
	print("Creating " + path)
	os.makedirs(path)
	return

def isdir(path):
	return os.path.isdir(path)
	
def deldir(path):
	print("Deleting " + path)
	shutil.rmtree(path)
	return

# Create the necessary folders
# Deleting old folders if they exist
print("Creating folders...")

if isdir("arma3"):
	deldir("arma3")
mkdir("arma3")

if isdir("missions"):
	deldir("missions")
mkdir("missions")

if isdir("mods"):
	deldir("mods")
mkdir("mods")

if isdir("profiles"):
	deldir("profiles")
mkdir("profiles")

if isdir("steamcmd"):
	deldir("steamcmd")
mkdir("steamcmd")

if isdir("userconfig"):
	deldir("userconfig")
mkdir("userconfig")

print("Downloading SteamCMD...")
file = urllib.request.urlopen("http://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip")
with open("steamcmd/steamcmd.zip", "wb") as code:
	code.write(file.read())

print("Extracting SteamCMD...")
zipfile = zipfile.ZipFile("steamcmd/steamcmd.zip", "r")
zipfile.extractall("steamcmd")
zipfile.close()

# Setup symlinks
subprocess.call("externals/python.exe setup-links.py")

if not isadmin:
	input("Warning, before proceeding, make sure the links are created. Press any key to continue . . .")

# Run SteamCMD
subprocess.call("externals/python.exe update-game.py")

# Yay
input("Install script completed!\nPress any key to continue . . .")