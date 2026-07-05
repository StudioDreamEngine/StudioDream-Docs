if [[ "$VIRTUAL_ENV" == "" ]] then
  source ./.venv/bin/activate
fi

python3.12 autogen/generate.py
mkdocs serve
