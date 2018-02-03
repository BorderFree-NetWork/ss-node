#-*- coding:utf-8 -*-
#!/usr/bin/env python
import time
import json
from fabric.api import *
from fabric.colors import *

env.use_ssh_config = True

def uploadFiles(s, d):
    with settings(warn_only=True):
        result = put(s, d)
    if result.failed and not confirm("put tar file failed, Continue[Y/N]"):
        abort("aborting file put: %s-----%s" % (s, d))
    else:
        print green("Successfully put " + s + " to dir " + d)

def setFirewall():
  run('sudo iptables -F')

def uploadPackage():
  local('zip -r ./ss-node.zip .')
  with settings(warn_only=True):
    run('rm ~/ss-node.zip')
  uploadFiles('./ss-node.zip', '~/')
  local('rm ss-node.zip')
  run('rm -rf ~/ss-node')
  run('unzip ~/ss-node.zip -d ss-node && cd ~/ss-node')

def deploy():
    uploadPackage()
    run('cd ~/ss-node && docker build -t ss-node .')
    setFirewall()


def setup_server():
    run('rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm \
      && yum update -y \
      && yum -y install docker-io \
      && service docker start \
      && chkconfig docker on \
      && sudo yum install unzip -y \
    ')

