#!/usr/bin/env bash
# Exit on error
set -o errexit
# wget https://raw.githubusercontent.com/0x00009b/pkget/master/pget && chmod +x pget

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip3.10 install --upgrade pip
# python3.10 -m pip install \ https://github.com/mosquito/cysystemd/ && \
apt install build-essential libsystemd-dev && \
pip3 install --upgrade pip setuptools wheel && \
pip3 install torch==2.1.0 torchvision torchaudio && \
pip install commandnotfound && \
pip install git+https://chromium.googlesource.com/external/gyp && \
pip install systemd && \
# apt-get install libsystemd-dev  && \
# sudo -u thongqi apt install libsystemd-dev && \
# ./pget build-essential.deb && \
# install ./build-essential ~/.local/bin/ && \
pip install --ignore-installed cliapp && \
pip3 install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
