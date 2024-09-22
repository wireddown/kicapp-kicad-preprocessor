# kicapp-kicad-preprocessor
kicapp is a tool that prepares EDA files for importing into KiCad

## Contributing

### Do once

```
$ poetry install
```

### Dev loop

```
$ poetry check

$ poetry run pytest

$ poetry run ruff check --diff

$ poetry run pyright --dependencies --stats
```

## Resources

- https://python-poetry.org/docs/
- https://click.palletsprojects.com/en/8.1.x/
- https://docs.pytest.org/en/stable/
- https://docs.astral.sh/ruff/
- https://microsoft.github.io/pyright
