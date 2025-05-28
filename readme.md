# criar ambiente windows
python -m venv .venv

# ativar ambiente - windows
.venv\Scripts\activate

# ativar ambiente - linux
source .venv/bin/activate

# exportar libs do projeto
pipreqs . --ignore .venv --force

# instalar libs do projeto
pip install -r requirements.txt