# explain

This is a super duper simple tool for printing the create table statement for a
table in a postgres (or redshift) database.

It's different from pg_dump with --schema-only option in that it:

1) Only prints out the create table statement.
2) If you pg_dump a table in a schema, the create table statement doesn't
include the schema in the name -- not a big issue, but it's just inconvenient
most of the time.

## Usage

First of all install the sucker:

```
pip install explain
```

Then use it like this:

```
$ explain -h mydb.com -u admin -d thedb foo.bar
Password:

CREATE TABLE foo.bar (
    ...
);
```
