mkdir json 
mkdir pdf
if [ -s config.py ]
then 
	echo "config.py deve contenere un token valido"
	cat config.py
else
	echo "creator un config.py vuoto, aggiungere il token discord"
	echo "TOKEN=\"\"" > config.py
fi
python3.10 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
patch ./venv/lib/python3.10/site-packages/pypdf/_writer.py pypdf.patch 
deactivate
