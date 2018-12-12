import os

arr = os.listdir("in")
arr_basename = [a[:-4] for a in os.listdir("in")]
fvspath = "/home/alex/Downloads/FVSexe"
xdoscript = open("xdo.sh",'w')
xdoscript.write("#!/bin/bash \n")
#xdoscript.write("id=$(xdotool search --name '/Downloads/FVSexe')")
#xdoscript.write("xdotool windowactivate $id")
xdoscript.write("sleep 10\n")
for x in range(0, len(arr)):
    fullname = arr[x]
    basename = arr_basename[x] 
    #xdoscript.write("wine {}/FVSOntario.exe\n".format(fvspath))
    #xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type carbon.key\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type in/{}\n".format(fullname))
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type out/{}.out\n".format(basename))
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type out/{}_treelist.out\n".format(basename))
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type out/{}_summary.out\n".format(basename))
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool type out/{}_cheapoii.out\n".format(basename))
    xdoscript.write("sleep 0.2\n")
    xdoscript.write("xdotool key Return\n")
    xdoscript.write("sleep 5\n")

