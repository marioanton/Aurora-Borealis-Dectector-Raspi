# Aurora-Borealis-Detector-Raspi
This project meant to exist because of auroras hobby came to my life.
This is a manual for beginners, as i am on this science field. Feel free to correct me. Been trying to get the most accurate but according to hw used and knowledge

Neccesary items to get Aurora Detector Raspi based. 
- Raspberry PI (Model B+ the one i used) [https://www.modmypi.com/]
- Xloborg magnetometer [https://www.piborg.org/xloborg]
- VM with Xymon Monitor Server [http://xymon.sourceforge.net/xymon/help/install.html]
- Xymon Client installed in Raspberry [sudo apt-get install hobbit-client]
- Give PI user root sudo with NOPASSWORD to ALL commands.

Not going to talk about raspberrypi installation.

## Magnetometer installation/detection ##

Once we get the product at home and with the RaspBerryPi switched off, we proceed to assembly it to the GPIO. 
Since the Xloborg is a magnetomer specifically adapted, there is no need to adapt anything. Just plug it and bingo.
This is not rocket science.

Switch raspi ON.
In order to get the Xloborg magnetometer recognized by the raspi, we proceed with following commands.
```
  sudo mkdir ~/xloborg
  sudo cd ~/xloborg
  sudo wget http://www.piborg.org/downloads/xloborg/examples.zip
  sudo unzip examples.zip
  sudo chmod +x install.sh
  sudo ./install.sh
```

We wil be having created several folders/files.
go into and execute it
````
  sudo cd ~/xloborg
  sudo ./XLoBorg.py
````

You will be getting:(otherwise you have done something wrong)

![Working](https://www.piborg.org/images/XLoBorg/example-test.png)


From these values, we will be looking after mX,mY and mZ ones.
Now, we have installed the magnetometer

## Calibrating mangenotmeter ##

Basically this consists of 

 - getting values from three axis given
 - and on each axis based, get the min value and  the max one
 - having the difference for each one, plus to the normal value you get

Here is where patience takes place since i had neither a robot nor a automatic way to move the magentomeneter in every direction for a long period of time (5000 seconds)

I used the following script: 
```
https://github.com/marioamas/Aurora-Borealis-Dectector-Raspi/blob/master/calibration-script.py
````
The script is pretty simple. In addition to it, you will have to run this as well:

````
for i in {1..5000}; do ./ReadCompassRaw.py >> data.csv;sleep 1;done
````
At sametime  this script is being executed, be prepare to move the magnetometer in every direction, upside down included :P

The output would be something similar to (where first colum is X, second is Y and third is Z)
````
-00602, +00462, +02022
-00605, +00461, +02021
-00605, +00462, +02026
-00604, +00455, +02026
````

So, once we have gathered the data, we just take the max and the min using for instance, excel, python or whatever.
Having those values for each column, we wil be having something like this

```
X Diff = (maxX + minX)/2
Y Diff = (maxY + minY)/2
X Diff = (maxZ + minZ)/2
```
Note that these values will be needed afterwards.

To check if the magnetometer has been properly calibrated you can use 3D Plot functions from python libs.
I used this one:
````
https://github.com/marioamas/Aurora-Borealis-Dectector-Raspi/blob/master/plotter.py
````
i got something like this, not pretty accurate but close.

![plot](https://lh6.googleusercontent.com/Jhz0yvuhDhH7zMvppZkHNWCl86velXU6n1yZywYEkbge9Qqjjuz3q2D2DN6KAGBYBxcsg-ch5OcpogEJuFfMbrahwgpYa3we=w1416-h614)

## Collecting data and sending it to Xymon Server  ##

This script i built will do the job.
- Gathering data script
  ReadCompassRaw.py -> https://github.com/marioamas/Aurora-Borealis-Dectector-Raspi/blob/master/ReadCompassRaw.py
  Change BBDISPLAY accordingly within file. (not needed since it is taken from BBENV, but there it is anyway)

- Hobbit/Xymon Client configuration needed as well.
 on clientlaunch.cfg:
 ````
 [kp]
        ENVFILE $HOBBITCLIENTHOME/etc/hobbitclient.cfg
        CMD $HOBBITCLIENTHOME/ext/ReadCompassRaw.py
        LOGFILE $HOBBITCLIENTHOME/xymon-kp.log
        INTERVAL 2m
````
- Server config as well
on graphs.cfg
````
[kp]
           TITLE kp
           YAXIS kp
           DEF:kp=kp.rrd:kp:AVERAGE
           LINE2:kp#@COLOR@:kp
           GPRINT:kp:LAST:Current\: %5.2lf%s C
           GPRINT:kp:MAX:Max\: %5.2lf%s C
           GPRINT:kp:MIN:Min\: %5.2lf%s C
           GPRINT:kp:AVERAGE:Avg\: %5.2lf%s C\n
````
on xymonserver.cfg add:

````
kp=ncv  => to TEST2RRD var, without deleting any other
NCV_kp="kp:GAUGE" => as a new line

````


