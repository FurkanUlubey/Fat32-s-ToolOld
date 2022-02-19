import subprocess
from turtle import setx
import webbrowser
import os 
while True:
  get_input = input("command: ")
  if get_input == "browser":
      webbrowser.open_new_tab("https://search.brave.com/")
  if get_input == "cmd":
      os.system("start")
  if get_input == "notepad":
       os.system("notepad")
  if get_input == "dxdiag":
      os.system("dxdiag")
  if get_input == "regedit":
      os.system("regedit")
  if get_input == "explorer":
      os.system("explorer")
  if get_input == "eudcedit":
      os.system("eudcedit")
  if get_input == "msinfo32":
      os.system("msinfo32")
  if get_input == "eventvwr":
      os.system("eventvwr")
  if get_input == "charmap":
      os.system("charmap")
  if get_input == "colorcpl":
      os.system("colorcpl")  
  if get_input == "taskschd":
      os.system("taskschd")
  if get_input == "taskmgr":
      os.system("taskmgr")
  if get_input == "sndvol":
      os.system("sndvol")
  if get_input == "Color Management":
      os.system("colorcpl")
  if get_input == "ColorMan":
      os.system("colorcpl")
  if get_input == "TaskMan":
      os.system("taskmgr")
  if get_input == "Volume Mixer":
      os.system("sndvol")
  if get_input == "rstrui":
      os.system("rstrui")
  if get_input == "psr":
      os.system("psr")

    ## 1nd Fun Fact: Script-Ware winning. 

  if get_input == "U2X -download -7zip -2107 -win -x64":
     webbrowser.open_new_tab("https://www.7-zip.org/a/7z2107-x64.exe")
  if get_input == "osk":
      os.system("osk")
  if get_input == "U2X -download -steam -all":
      webbrowser.open_new_tab("https://store.steampowered.com/about/")
  if get_input == "help":
      print("cmd - open command prompt")
      print("browser - open the browser")
      print("U2X - an package manager")
      print("U2X -download -steam -all - opens steam download page")
      print("dxdiag - opens direct X gui")
      print("eventvwr - opens event viewer")
      print("TaskMan - opens Task Manager") ## yaz ma l ## o # 
      print("taskmgr - opens Task Manager") ## B3rkay
      print("sndvol - open Volume Mixer") ## LOLsomadasdok
      print("psr - opens step record") ## Prens_J
      print("magnify - opens magnifying glass")
      print("U2X -download -7zip -2107 -win -x64 - download 7 zip windows 64 bit")
  if get_input == "netplwiz":
      os.system("netplwiz")
  if get_input == "msconfig":
      os.system("msconfig")
  if get_input == "magnify":
      os.system("magnify")
  if get_input == "filehistory":
      os.system("filehistory")
  if get_input == "eventvwr":
      os.system("eventvwr")
  if get_input == "dpiscaling":
      os.system("dpiscaling")
  if get_input == "diskmgmt":
      os.system("diskmgmt")
  if get_input == "dccw":
      os.system("dccw")
  if get_input == "control":
      os.system("control")
  if get_input == "cleanmgr":
      os.system("cleanmgr")
  if get_input == "certmgr":
      os.system("certmgr")
  if get_input == "calc":
      os.system("calc")
  if get_input == "tpm":
      os.system("tpm")

  ## 2nd Fun Fact: Brave Browser Better.

  else:
     print("not found")