# FVSAutomator

## What is this?

The Forest Vegetation Simulator tool released by the US Forest Service seems to not be designed for any automated input - rather, on its own, you must enter in each input manually. This two-part script solution addresses this automation gap and allows you to run the FVS simulation on hundreds of input files at once with a few keystrokes. 

This is written to work with the Ontario variant of the FVS tool. Other FVS versions may have slightly different inputs. 

## How do I use it?

### System prerequisites

* OS: Linux
* Packages: `wine`, `xdotool`, `python` (Debian-based systems should just require `sudo apt install wine xdotool python`. All major Linux distributions should have these three packages available through the package manager, otherwise build from source. Python should already be installed on your system.)

This automation tool is written to be run in Linux only - I'll happily accept a pull request with a tool like AutoHotKey for Windows, or an equivalent tool in MacOS. 

### Organizing the data

Your inputs (minus they .key file) must all be in a folder titled `in` and you must have an empty folder titled `out` where the output files will be generated. All inputs should have a file extension of `.tre`. The keyword file is named `carbon.key`, and should be in the root of the repository. 

### Generating the xdotool script

The python script in this repository is designed to create the shell script that executes all the xdotool commands. To run, fire up a terminal in the root of this repository and run `python gen_xdotool.py`. This will generate a file named `xdo.sh` containing the xdotool commands.

### Running xdo.sh

To run xdo.sh, simply run `bash xdo.sh` and sit back. Since this is automating typing in the terminal, it is crucial that you leave this terminal active and not select another window while it is running, otherwise the xdotool automation will start typing in the new window you have activated. It will also probably not like it if your computer goes to a lock screen partway through running, but I have not tested that.  For these reasons alone, I would highly recommend either running this tool on a secondary machine, or in a virtual machine so that you can let it run and do other stuff while it completes, especially if you have a large number of inputs you need to run. 

Due to it requiring xdotools, it cannot be run on a headless machine. 
