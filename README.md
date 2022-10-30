## BMSYNC

Black Mamba Sync, a prototype (rsync/NFS)-like client-server file sharing system. UDP for service discovery and TCP for bulk-data transfer [Stevens et al., 2004].

Basically the user-data communication happens over TCP once discovery is completed over UDP.

### Reproduce this environment:


Be sure to be in the root of the project repository directory:

```
git clone thisproj
cd ./thisproj/
```

Create Python virtual environment (virtualenv, venv), upgrade the package manager pip, install the new Python distribution, Wheels, and install dependencies listed on ```requirements.txt```.

```
python3.10 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install wheel  #Not a typo
pip install -r ./requirements.txt

```

Run the shellscript to start the application. It will start the script and ask if the instance of the program wants to act as server or client.

```
sh ./runit.sh
```
