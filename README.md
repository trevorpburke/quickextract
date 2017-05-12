## quickextract - a tool to quickly generate ad-hoc reports

by simply connecting to your database of choice you can be creating quick reports in about three lines of code. 

quickextract connects to dbs using the create_engine function in sqlalchemy.

Example:

    from quickextract import extract_tools
    conn = SQL_Extract('postgresql://username:password@host:port/database')
    conn.csv('select * from table', 'sample')
    # generates a CSV in the current working directory
