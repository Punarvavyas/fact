# fact
i.	 Virtual box was installed in my windows system. In that Ubuntu 16 was installed. The zookeeper and mesos was installed with the help of the online documentation available. 
The following commands where used during the installation process:
• sudo apt-key adv –keyserver hkp://keyserver.ubuntu.com:80 –recv E56151BF 
• DISTRO=$(lsb_release -is | tr ‘[:upper:]’ ‘[:lower:]’)
 • CODENAME=$(lsb_release -cs) 
• echo “deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main” | sudo tee /etc/apt/sources.list.d/mesosphere.list 
• sudo apt-get -y update 
• sudo apt-get -y install mesos marathon
ii.	 Marathon was installed and configured using the                  below commands. Then two python scripts were run inside the container. The log file can be found in the  submitted folder 
• curl -O http://downloads.mesosphere.com/marathon/v1.5.1/marathon-1.5.1.tgz
• tar xzf marathon-1.5.1.tgz

iii.	The github repository was created containing the two programs of factorial and Fibonacci for user1 and user2. THe code can be found in the repository.
