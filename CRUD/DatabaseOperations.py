import psycopg2



def WriteToDatabase(TwitterFeed):
    """
           Generates SpaCy Analysis and outputs the data into the format
           Parameters
           ----------
           self : DataFrame object
               upon itself

           data : string
               Twitter JSON feed
           """
    # Connect to an existing database
    conn = psycopg2.connect("dbname=postgres user=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO twitterlog (twitterjson) VALUES (%s)", [TwitterFeed])

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
