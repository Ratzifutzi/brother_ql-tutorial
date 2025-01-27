**DISCLAIMER:** I was not able to do this via USB. My script uses a ethernet cable and I will explain you how to do that too.

# Brother QL Python label printer
Making this program was quite frustrating and if you want to use it yourself, you'll probably have to do some adjustments by yourself.

# Prerequisites
You'll need some python libraries, for one library, you'll need to downgrade a library since there are some deprecated methods used. I will probably modify the brother_ql library and fix the issues so you guys won't have to do that in the future. As of 27.01.2025 you have to do it the way described below. **I've ran into the issue that brother_ql doesn't add the required command line commands to PATH on Windows. If you run Windows, please run the install command as administrator**.


First install the main library:
```
brother_ql==0.9.4
```
After installation, downgrade pillow:
```
pip uninstall Pillow
```
after uninstall, install the downgraded version:
```
pip install Pillow==9.5.0
```

<br>

After the installation, try running the brother_ql command
```
brother_ql
```
If you get an error, try restarting your PC. If you still get the error, you'll have to figure out yourself. This is probably because the command is not added to PATH.

# Next steps
1. Check if your device is supported. Sub Versions like the QL-820NWB**c** is the same as QL-820NWB<br>QL-500, QL-550, QL-560, QL-570, QL-580N, QL-650TD, QL-700, QL-710W, QL-720NW, QL-800, QL-810W, QL-820NWB, QL-1050, QL-1060N
2. Turn off your printer BEFORE connecting any Ethernet cable. After connecting your ethernet cable with your printer and your PC, you may start your printer again.
3. Install ethernet drivers for your printer
Go to brothers web page and download the driver installer for your printer. When you install, you'll be able to select what you want to install. You'll have to select the Wired Network Connection. [View this picture for reference](images/driver.png). Continue with the Set Up.
4. Now we'll have to get the device IP adress. To get it, press the following buttons on your printer, if you have a Display. If you don't, you'll have to figure out yourself, but it's possible. I've done the following steps on a QL-820NWBc
	1. Press "Menu"
	2. Go to "Information"
	3. Go to "Print Configuration"
	4. Select "All". This will print around 30cm of tape.
	5. On the print, look for \<IP Settings\>, the line below that should say "IP Adress". Write down that number

# Update the program
1. Change "printer_model" to your printer. Make sure to write down the major version of it \-\> if you have a "QL-820NWB***c***", remove the "C" and use "QL-820NWB" in the variable
2. Change "printer_connection" with the IP Adress you've wrote down earlier. It should look like something like this: "tcp://0.0.0.0".
3. Change "label_type" with the current labels you have in your printer. Run `brother_ql info labels` for a full list including ideal pixel dimensions OR view the screenshot I've made [here](images/labels.png).

# Run the script
After all that trouble, you should now be able to print out labels. Just run the script \:)
<br>
If you still run into issues, contact me either on
Discord: `ratzifutzi`
Mail: `joshua@hyper-tech.ch`
<br>
It would be nice if you contact me, so I can help other people figure this annoying thing out for themselves \:) I hope this tutorial was at least a bit helpful and I wish you a wonderful day.