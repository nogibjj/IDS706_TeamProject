"""Database query lib"""
import json
import MySQLdb


class DB:
    """DB utility class to connect and query"""
    def __init__(self):
        # get connected with the db
        self.connection = MySQLdb.connect(
            host="imdb.ciankffgrtkz.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="12349876",
            db="proj5",
        )
        # get the cursor of the connection
        self.cursor = self.connection.cursor()


    def query1(self, director_name):
        '''
        query1: return all movies directed by a specified director
        '''
        sql1 = 'SELECT title, year, director\
                FROM movie\
                WHERE director = "' + director_name + '"'
        self.cursor.execute(sql1)
        data = self.cursor.fetchall()

        result = []
        for row in data:
            movie = {}
            movie['title'] = row[0]
            movie['year'] = row[1]
            movie['director'] = row[2]
            result.append(movie)

        return json.dumps(result)


    def query2(self):
        '''
        query2: return all movies that have ratings higher than 9
        '''
        sql2 = 'SELECT title, year, rating\
                FROM movie\
                WHERE rating >= 9'
        self.cursor.execute(sql2)
        data = self.cursor.fetchall()

        result = []
        for row in data:
            movie = {}
            movie['title'] = row[0]
            movie['year'] = row[1]
            movie['rating'] = str(row[2])
            result.append(movie)

        return json.dumps(result)


    def query3(self):
        '''
        query3: return the top 10 longest movies
        '''
        sql3 = 'SELECT title, year, runtime\
                FROM movie\
                ORDER BY runtime DESC\
                LIMIT 10'       
        self.cursor.execute(sql3)
        data = self.cursor.fetchall()

        result = []
        for row in data:
            movie = {}
            movie['title'] = row[0]
            movie['year'] = row[1]
            movie['runtime'] = row[2]
            result.append(movie)

        return json.dumps(result)
