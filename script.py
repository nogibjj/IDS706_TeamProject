import pandas as pd
import MySQLdb
import os

def get_connection():
    """Returns a connection to the database"""
    connection = MySQLdb.connect(
        host="imdb.ciankffgrtkz.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd=os.environ["PROJ5_DB_PASS"],
        db="proj5",
    )
    return connection

def save_data(connection, title, year, director, actors, rating, runtime, censor, gross, genre_main, genre_side):
    cursor = connection.cursor()
    str = (
        "INSERT INTO movie VALUES ('"
        + title
        + "',"
        + year
        + ",'"
        + director
        + "','"
        + actors
        + "',"
        + rating
        + ","
        + runtime
        + ",'"
        + censor
        + "','"
        + gross
        + "','"
        + genre_main
        + "','"
        + genre_side
        + "');"
    )
    #print(str)
    cursor.execute(str)
    connection.commit()


def save_all_data():
    """Saves the csv data to the database"""
    df = pd.read_csv("./movie.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        try:
            save_data(
                connection,
                row["Movie_Title"],
                str(row["Year"]),
                row["Director"],
                row["Actors"],
                str(row["Rating"]),
                str(row["Runtime(Mins)"]),
                row["Censor"],
                row["Total_Gross"],
                row["main_genre"],
                row["side_genre"],
            )
        except Exception as e:
            continue

    connection.close()

if __name__ == "__main__":
    save_all_data()