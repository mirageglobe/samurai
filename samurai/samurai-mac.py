#!/usr/bin/env python3

import os, platform, sys, socket

samuraimap = {}

# ===============================
# Samurai Specific
# ===============================

samuraimap[0] = {   'name': 'Exit Samurai',
                    'cmd': 'clear',
                    'responsesuccess': ''
                    }

samuraimap[1] = {   'name': 'Update Samurai',
                    'cmd': 'curl -L https://raw.githubusercontent.com/mirageglobe/samurai/master/install.sh | bash',
                    'responsesuccess': ''
                    }

samuraimap[2] = {   'name': 'Remove Samurai',
                    'cmd': 'sudo rm /usr/local/bin/samurai && sudo rm /usr/local/bin/samurai-mac.py && sudo rm /usr/local/bin/samurai-linux.py',
                    'responsesuccess': 'Samurai removed.'
                    }

samuraimap[3] = {   'name': 'Toggle ShowCmd mode',
                    'cmd': '',
                    'responsesuccess': ''
                    }

samuraimap[4] = {   'name': 'Clear screen and show menu',
                    'cmd': 'clear',
                    'responsesuccess': 'Screen Cleared'
                    }

# ===============================
# 10s Operating System
# ===============================

samuraimap[10] = {  'name': 'Change my login password',
                    'cmd': 'passwd',
                    'responsesuccess': ''
                    }

samuraimap[11] = {  'name': 'Show stats Mem',
                    'cmd': 'top -l 1 | head -n 10 | grep PhysMem',
                    'responsesuccess': ''
                    }

samuraimap[12] = {  'name': 'Show top 10 CPU usage',
                    'cmd': 'top -o cpu -n 10',
                    'responsesuccess': ''
                    }

samuraimap[13] = {  'name': 'Show IP address (Global)',
                    'cmd': 'curl http://icanhazip.com',
                    'responsesuccess': ''
                    }

samuraimap[14] = {  'name': 'Show Mac invisible files',
                    'cmd': 'defaults write com.apple.finder AppleShowAllFiles YES && killall Finder /System/Library/CoreServices/Finder.app',
                    'responsesuccess': ''
                    }

samuraimap[15] = {  'name': 'Hide Mac invisible files',
                    'cmd': 'defaults write com.apple.finder AppleShowAllFiles NO && killall Finder /System/Library/CoreServices/Finder.app',
                    'responsesuccess': ''
                    }

samuraimap[16] = {  'name': 'Reload shell',
                    'cmd': 'exec $SHELL -l',
                    'responsesuccess': ''
                    }

samuraimap[17] = {  'name': 'List current users',
                    'cmd': 'cat /etc/passwd',
                    'responsesuccess': ''
                    }

samuraimap[18] = {  'name': 'Show local listening ports',
                    'cmd': 'lsof -i -P',
                    'responsesuccess': ''
                    }

samuraimap[19] = {  'name': 'Show kernel and OS information',
                    'cmd': 'uname -a',
                    'responsesuccess': ''
                    }

samuraimap[20] = {  'name': 'Use Caffeinated and prevent mac from sleeping',
                    'cmd': 'echo "running caffeinate. ctrl-c to exit" && caffeinate -s',
                    'responsesuccess': ''
                    }


# ===============================
# 30s Platform and Pkg Managers
# ===============================

samuraimap[31] = {  'name': 'Install homebrew',
                    'cmd': 'which brew || ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
                    'responsesuccess': ''
                    }

samuraimap[32] = {  'name': 'Install cask for homebrew',
                    'cmd': 'which brew || brew install caskroom/cask/brew-cask',
                    'responsesuccess': ''
                    }

samuraimap[33] = {  'name': 'Update and clean homebrew',
                    'cmd': 'which brew || brew update && brew upgrade && brew cleanup',
                    'responsesuccess': ''
                    }

samuraimap[34] = {  'name': 'Install pyenv (python manager)',
                    'cmd': 'which brew || brew update && brew install pyenv',
                    'responsesuccess': ''
                    }

samuraimap[35] = {  'name': 'Install chruby and ruby-install (ruby manager)',
                    'cmd': 'which brew || brew update && brew install chruby ruby-install',
                    'responsesuccess': ''
                    }

samuraimap[36] = {  'name': 'Install nvm (node manager)',
                    'cmd': 'which nvm || curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh | bash',
                    'responsesuccess': ''
                    }


# ===============================
# Functions
# ===============================

def loadoptions(ninja=False,showcmd=False):
  print("=======================================")
  print("Samurai for Mac")
  print("[ShowCMD={0}|System:{1}({2})]".format(showcmd,platform.system(),platform.release()))
  print("=======================================")

  for key, value in sorted(samuraimap.items()):
    if showcmd:
      print("[", key, "] -", value['name'], " ::> " , value['cmd'])
    else:
      print("[", key, "] -", value['name'])

def runcommand(cmdstring):
  return_value = os.system(cmdstring)

# ===============================
# Main Code
# ===============================

if __name__ == "__main__":

  # ===============================
  # Checks for system
  # ===============================

  if platform.system() != 'Darwin':
    print("[Samurai] System incompatible, please run samurai.py instead.")
    sys.exit(1)

  # ===============================
  # Setting arguments
  # ===============================

  ninja_active = False
  showcmd_active = False

  # Adding ninja mode here - ninja mode activated within menu
  # In ninja mode, the commands are not executed; until the end. if you run ninja, it will create a scroll.sh with bash commands which can be used with vagrant
  # export DEBIAN_FRONTEND=noninteractive
  # apt-get -y install package1 package2

  # ===============================
  # Default load of system
  # ===============================

  avatar = "[samurai]"
  gloop = True

  # ===============================
  # Entering loop of samurai
  # ===============================

  runcommand("clear")

  while gloop:
    gchoice = 9999

    loadoptions(ninja_active,showcmd_active)
    gchoice = input("================================== \n{0} What is your command? : ".format(avatar))

    if gchoice.isdigit():
      gchoice = int(gchoice)
    else:
      gchoice = 9999

    if gchoice == 0:
      break

    if gchoice == 3:
      showcmd_active = not showcmd_active       # toggle showcmd mode

    if gchoice in samuraimap:
      runcommand(samuraimap[gchoice]['cmd'])
      if not samuraimap[gchoice]['responsesuccess']:
        print("{0}".format(avatar), samuraimap[gchoice]['responsesuccess'])
    else:
      print("{0} Command is does not exist. Please enter number.".format(avatar))       #load the options again. does not work if placed in above array

    input("Enter to continue")
    runcommand("clear")