import subprocess


# Ask for user credentials
print("Downloading/updating server software...")
print("You must provide a steam account in order to download and update the server software. It is recommended you create a new account for this purpose. Continue the script when you have done so.")
input("Press any key to continue . . .")

steamuser = input("Enter steam username: ")
steampw = input("Enter steam password: ")
args = '+login %s %s +force_install_dir ../arma3 +app_update 233780 validate quit' % (steamuser, steampw)
subprocess.call("steamcmd/steamcmd.exe " + args)