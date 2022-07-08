Set WshShell = WScript.CreateObject("WScript.Shell")
strCurDir = WshShell.CurrentDirectory
Return = WshShell.Run(strCurDir & "\reproductor.py",3,false)