import click

__version__ = "0.1.1"


@click.command("guten-tag")
def version():
    click.echo("guten tag")


@click.command("version")
def version():
    click.echo(__version__)


@click.command("hello")
def hello():
    click.echo("hello, world!")


if __name__ == "__main__":
    hello()
