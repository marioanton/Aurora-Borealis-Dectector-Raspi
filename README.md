# Aurora-Borealis-Raspi
This project meant to exist because of auroras hobby came to my life.

Neccesary items to get Aurora Detector Raspi based. 
- Raspberry PI (Model B+ the one i used) [https://www.modmypi.com/]
- Xloborg magnetometer [https://www.piborg.org/xloborg]
- VM with Xymon Monitor Server [http://xymon.sourceforge.net/xymon/help/install.html]
- Xymon Client installed in Raspberry [sudo apt-get install hobbit-client]
- Patience

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

You will be getting:

![Working](https://www.piborg.org/images/XLoBorg/example-test.png)

