"""Defines all the functions related to the database"""
from app import db

def Two_origin_recommand(origin: str, dest: str) -> str:
    conn = db.connect()
    query = """SELECT airline.name AS Best, AVG(Delay) AS AVG_Delay
FROM airline JOIN (SELECT Airline, (AVG(ArrivalDelay)+AVG(DepartureDelay)) AS Delay
FROM flight
GROUP BY Airline) delay_cal ON airline.name = delay_cal.Airline
WHERE Origin = '{}' AND Destination = '{}'
GROUP BY airline.name
ORDER BY AVG_Delay
LIMIT 1;
""".format(origin, dest)
    result = conn.execute(query).fetchone()
    conn.close()

    if result:
        airline, delay = result
        return '{} {}'.format(airline, delay)
    else:
        return 'No results found'



def Two_city_delay(origin: str, dest: str) -> str:
    conn = db.connect()
    query = """SELECT flight.Airline, AVG(ArrivalDelay) + AVG(DepartureDelay) AS Average_delay
FROM flight JOIN airline ON (flight.Airline = airline.name)
WHERE airline.Origin = '{}' AND airline.Destination = '{}'
GROUP BY flight.Airline;""".format(origin, dest)
    results = conn.execute(query).fetchall()
    conn.close()

    if results:
        output = ""
        for result in results:
            airline, delay = result
            output += '{} {}\n'.format(airline, delay)
        return output.strip()
    else:
        return 'No results found'
    


def add_reviewdb(text: str, airname: str) -> int:
    conn = db.connect()
    query = """INSERT INTO review (Text, airline_name) VALUES ("{}", "{}");""".format(text, airname)
    conn.execute(query)
    query = """SELECT Review_ID FROM review WHERE (airline_name = "{}" AND Text = "{}");""".format(airname, text)
    id = conn.execute(query).fetchone()[0]
    conn.close()
    return id



def delete_reviewdb(review_id: int) -> None:
    conn = db.connect()
    query = """DELETE FROM review WHERE Review_ID = {};""".format(review_id)
    conn.execute(query)
    conn.close()



def update_reviewdb(review_id: int, text: str) -> None:
    conn = db.connect()
    query = """UPDATE review SET Text = "{}" WHERE Review_ID = {};""".format(text, review_id)
    conn.execute(query)
    conn.close()


def show_review(search: str) -> None:
    conn = db.connect()
    query = """SELECT * FROM review WHERE airline_name = "{}";""".format(search)
    conn.execute(query)
    conn.close()



def delay_calculator(airline: str, origin: str, dest: str) -> str:
    conn = db.connect()
    query = """SELECT AVG(ArrivalDelay) + AVG(DepartureDelay) AS Average_delay
FROM flight JOIN airline ON (flight.Airline = airline.name)
WHERE flight.Airline = '{}' AND airline.Origin = '{}' AND airline.Destination = '{}';""".format(airline, origin, dest)
    result = conn.execute(query).fetchone()
    conn.close()

    if result:
        average_delay = result[0]
        return 'Average delay: {}'.format(average_delay)
    else:
        return 'No results found'

def searchdb(Aline: str) -> str:
    conn = db.connect()
    query = """SELECT Text FROM review WHERE airline_name = "{}";""".format(Aline)
    results = conn.execute(query).fetchall()
    conn.close()

    if results:
        output = ""
        for result in results:
            output += '{}\n'.format(result)
        return output.split('\n')
    else:
        return 'No results found'
    

def get_best_airline_with_least_delay(origin, destination):
    conn = db.connect()
    query = """CALL GetBestAirlineWithLeastDelay("{}", "{}");""".format(origin, destination)
    result = conn.execute(query).fetchone()

    conn.close()

    return result[0], result[1]

