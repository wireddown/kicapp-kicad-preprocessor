# kicapp-kicad-preprocessor
kicapp is a tool that prepares EDA files for importing into KiCad

## Contributing

### Do once

```
$ pipx install poetry
$ pipx inject poetry poethepoet
$ poetry install
$ poetry check
```

### Dev loop

```
$ poetry run kicapp [OPTIONS] COMMAND [ARGS]

$ poetry poe test

$ poetry poe lint
```

## Resources

- https://pipx.pypa.io/stable/
- https://python-poetry.org/docs/
- https://poethepoet.natn.io/index.html
- https://click.palletsprojects.com/en/8.1.x/
- https://docs.pytest.org/en/stable/
- https://docs.astral.sh/ruff/
- https://microsoft.github.io/pyright
