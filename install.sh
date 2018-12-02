rm /usr/bin/tts
PWD=$(pwd)
chmod +x $PWD/code/tts.py
ln -s $PWD/code/tts.py /usr/bin/tts
