mkdir json 
mkdir pdf
python3.10 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
patch ./venv/lib/python3.10/site-packages/pypdf/_writer.py pypdf.patch 
deactivate
