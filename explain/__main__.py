"""Program entry point!"""
import click
from explain.dump import dump


@click.command()
@click.argument('table')
@click.option('--host', '-h', help="Host of the postgres instance.")
@click.option('--port', '-p', default=5432,
              help="Port of the postgres instance.")
@click.option('--user', '-u', help="User of postgres instance.")
@click.option('--password', '-P', prompt=True, hide_input=True,
              envvar='PGPASSWORD',
              help="Password of the postgres instance.")
@click.option('--db', '-d', help="Database on the postgres instance.")
def explain(table, host, port, user, password, db):
    """Print the create table statement for a table."""
    print('')
    print(dump(table, host, port, user, password, db))

if __name__ == '__main__':
    explain()
