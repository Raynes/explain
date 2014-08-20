"""Code for running pg_dump and extracting the bit of useful info we want."""
import re
from sh import pg_dump


def replace_table(s, table):
    """Replace the table in the create table statement
    with the one specified.

    """
    return re.sub(r'CREATE TABLE \w+', 'CREATE TABLE ' + table, s)


def extract_create(s, table):
    """Extract the create table statement from the string
    and change the table name to include the schema if
    needed.

    """
    for item in s.split('\n\n'):
        if item.startswith('CREATE TABLE'):
            return replace_table(item, table)


def dump(table, host, port, user, password, db):
    """Dump the create table statement for this table."""
    out = pg_dump(db, '--schema-only', t=table, h=host, U=user, p=port,
                  _env={'PGPASSWORD': password})
    return extract_create(out, table)
