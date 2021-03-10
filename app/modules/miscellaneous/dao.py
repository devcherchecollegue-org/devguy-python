from sqlite3 import connect, Error


class DAO:
    def __init__(self, config):
        try:
            self.conn = connect(config.get('database', 'database'))
        except Error as e:
            print(e)
            raise EnvironmentError("Could not connect to database!")

    def __cursor(self):
        return self.conn.cursor()

    def insert_follow(self, user_id: int):
        """
        Add user to followed list

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """ 
        INSERT INTO coin_coin (user_id)
        VALUE (?)
        """

        self.__cursor().execute(query, user_id)

    def delete_follow(self, user_id: int):
        """

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """ 
            DELETE FROM coin_coin
            WHERE user_id = ?
            """

        self.__cursor().execute(query, user_id)
