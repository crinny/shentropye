import click

from shentropye.providers import Cyberspace, Necrodesign


@click.command()
def main():
    """
    Простая CLI утилита для получения актуальных кодов шентропье
    """
    cyberspace, necrodesign = Cyberspace(), Necrodesign()
    for code in cyberspace.get_codes():
        click.echo(code)
    for code in necrodesign.get_codes():
        click.echo(code)


if __name__ == "__main__":
    main()
