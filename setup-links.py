import os
import ctypes
import sys


isadmin = ctypes.windll.shell32.IsUserAnAdmin()

if not isadmin:
	input("""Warning, you are not running this script as an admin, therefore it cannot create any symlinks. Execute setup-links.cmd as an admin or create the following symlinks manually:
arma3/mpmissions -> ../missions
arma3/mods -> ../mods
arma3/profiles -> ../profiles
arma3/userconfig -> ../userconfig

setup-links will now exit. Press any key to continue . . .""")
	sys.exit()

input("Setting up symlinks. This will delete any existing symlinks. Press any key to continue . . .")

def isdir(path):
	return os.path.isdir(path)
	
def unlink(path):
	print("Deleting " + path)
	os.unlink(path)
	return
	
def mklink(src, dst):
	print("Creating symlink " + dst + " ==> " + src)
	os.symlink(src, dst)
	return

# The backslash is necessary on windows
if isdir("arma3/mpmissions"):
	unlink("arma3/mpmissions")
mklink("..\\missions", "arma3/mpmissions")	

if isdir("arma3/mods"):
	unlink("arma3/mods")
mklink("..\\mods", "arma3/mods")

if isdir("arma3/profiles"):
	unlink("arma3/profiles")
mklink("..\\profiles", "arma3/profiles")

if isdir("arma3/userconfig"):
	unlink("arma3/userconfig")
mklink("..\\userconfig", "arma3/userconfig")
