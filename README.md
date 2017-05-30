# **Codetouch Messenger**
This is a simple web application develpoed using python on the Django framework.

## Requirements
#### Docker
Follow the official documentations install instruction.
Visit [Docker Installation](https://docs.docker.com/engine/installation/linux/ubuntu/)
## Steps
```
$ git clone https://github.com/Amrsaeed/codetouch.git
$ cd codetouch
$ sudo docker build -t amrsaeed/codetouch .
$ sudo docker run -it -p 8000:8000 amrsaeed/codetouch

Browse to http://localhost:8000/

**Admin account**
username: admin
password: admin123qwe
```
### Notes
Messages display was somehow messed up when run from docker and I didn't have time to debug.
