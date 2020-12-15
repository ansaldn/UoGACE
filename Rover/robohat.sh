if [ ! -d ~/robohat ]; then
  mkdir ~/robohat
fi
cd ~/robohat
wget -q http://4tronix.co.uk/robohat/servod.xxx -O servod
wget -q http://4tronix.co.uk/robohat/robohat.py -O robohat.py
wget -q http://4tronix.co.uk/robohat/motorTest.py -O motorTest.py
wget -q http://4tronix.co.uk/robohat/motorTest2.py -O motorTest2.py
wget -q http://4tronix.co.uk/robohat/motorTestRaw.py -O motorTestRaw.py
wget -q http://4tronix.co.uk/robohat/irTest.py -O irTest.py
wget -q http://4tronix.co.uk/robohat/servo.py -O servo.py
wget -q http://4tronix.co.uk/robohat/servoTest.py -O servoTest.py
wget -q http://4tronix.co.uk/robohat/sonarTest.py -O sonarTest.py
chmod +x servod
