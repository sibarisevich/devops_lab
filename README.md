#Overview

'systemmonitor' app can create snapshots of the state of the system each n minutes('n' - may be setted-up) App output next data: ● Overall CPU load ● Overall memory usage ● Overall virtual memory usage ● IO information ● Network information


#The app's parameters

For confifure system monitor use /monitor/config.ini
● type - type of report format. Can be json or txt.
● time - how often will doing snapshons. Specify in minutes.
● count - how many snapshots will be taken by the application. For infinitely choose 0.

#HowToInstall

for installetion module insert: pip install /path/to/wheel/file


#HowToUse

For start upplication jast incert command: python monitor
