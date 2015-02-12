#!/usr/bin/env python3

import os, platform, sys

samuraimap = {}

# ===============================
# 1s Core
# ===============================

samuraimap[0] = {   'name': 'Exit system',
                    'cmd': '',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[1] = {   'name': 'Clear screen and show menu',
                    'cmd': 'clear',
                    'cmdslient': 'clear',
                    'responsesuccess': 'Screen Cleared',
                    'responsefail': '',
                    }

samuraimap[2] = {   'name': 'Toggle Ninja Mode',
                    'cmd': '',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[3] = {   'name': 'Toggle ShowCmd Mode',
                    'cmd': '',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[4] = {   'name': 'Show Stats Mem',
                    'cmd': 'top -l 1 | head -n 10 | grep PhysMem',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[7] = {   'name': 'Show IP Address',
                    'cmd': 'curl http://icanhazip.com',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[8] = {   'name': 'Update Samurai.py',
                    'cmd': 'curl -L https://raw.githubusercontent.com/mirageglobe/samurai/master/install.sh | bash',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

samuraimap[9] = {   'name': 'Remove Samurai',
                    'cmd': 'sudo rm /usr/local/bin/samurai.py',
                    'cmdslient': '',
                    'responsesuccess': 'Samurai removed.',
                    'responsefail': '',
                    }

# ===============================
# 10s Operating System 
# ===============================

samuraimap[10] = {  'name': 'Change my login password',
                    'cmd': 'passwd',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

# ===============================
# 30s Databases
# ===============================

# ===============================
# 40s Servers
# ===============================

# ===============================
# 50s Platform and Pkg Managers
# ===============================

samuraimap[51] = {  'name': 'Install HomeBrew',
                    'cmd': 'ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
                    'cmdslient': '',
                    'responsesuccess': '',
                    'responsefail': '',
                    }

# ===============================
# 60s Languages
# ===============================

# ===============================
# 70s Apps
# ===============================

# ===============================
# Custom Apps Start from 100
# ===============================


# ===============================
# Functions
# ===============================

def loadoptions(ninja=False,showcmd=False):
  print("==================================") 
  print("Samurai Mac") 
  print("Detected System: {0} ({1}) - showing compatible commands".format(platform.system(),platform.release()))
  print("Ninja Mode: {0}".format(ninja))
  print("Show Cmd: {0}".format(showcmd))
  print("==================================")

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
  # Checks for python 3
  # ===============================

  if sys.version_info < (3, 0):
    sys.stdout.write("[Samurai] Samurai requires Python 3.x, and you are running it as Python 2.x\n")
    sys.stdout.write("[Samurai] You can install by running sudo apt-get install python3 or python3 samurai.py\n")
    sys.exit(1)

  # ===============================
  # Checks for system
  # ===============================

  if platform.system() != 'Darwin':
    print("[!] System incompatible, please run samurai.py instead.")
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
      runcommand("clear")
      break

    if gchoice == 2:
      ninja_active = not ninja_active
      # toggle ninja mode

    if gchoice == 3:
      showcmd_active = not showcmd_active
      # toggle showcmd mode

    if gchoice in samuraimap:
      runcommand(samuraimap[gchoice]['cmd'])
      if not samuraimap[gchoice]['responsesuccess']:
        print("{0}".format(avatar), samuraimap[gchoice]['responsesuccess'])
    else:
      print("{0} Command is does not exist. Please enter number.".format(avatar))
      #load the options again. does not work if placed in above array

    input("Enter to continue")
    runcommand("clear")