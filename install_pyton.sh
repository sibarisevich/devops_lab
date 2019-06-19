#!/usr/bin/bash

if ! [ -d /home/vagrant/.pyenv/versions/2.7.6 ]; then
 pyenv install 2.7.6
fi

if if ! [ -d /home/vagrant/.pyenv/versions/3.7.0 ]; then
pyenv install 3.7.0
fi

if ! [ -d /home/vagrant/.pyenv/versions/2.7.6/envs/v2.7 ]; then
 pyenv virtualenv 2.7.6 v2.7
fi

if ! [ -d /home/vagrant/.pyenv/versions/3.7.0/envs/v3.7 ]; then	
 pyenv virtualenv 3.7.0 v3.7
fi

echo saccess
