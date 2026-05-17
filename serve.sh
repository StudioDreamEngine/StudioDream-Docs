if [[ "$VIRTUAL_ENV" == "" ]] then
  source ./.venv/bin/activate
fi

python autogen/generate.py
mkdocs serve