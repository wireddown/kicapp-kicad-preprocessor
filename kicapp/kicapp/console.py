import click

@click.group()
def cli():
    pass

def run():
    cli()


if __name__ == '__main__':
    run()
