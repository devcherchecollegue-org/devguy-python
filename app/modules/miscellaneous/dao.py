from sqlite3 import connect, Error


class DAO:
    def __init__(self, config):
        try:
            self.conn = connect(config.get('database', 'name'))
        except Error as e:
            print(e)
            raise EnvironmentError("Could not connect to database!") from e

    def __cursor(self):
        return self.conn.cursor()

    def __commit(self):
        return self.conn.commit()

    def get(self, user_id: int):
        """
        Add user to followed list

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
        SELECT * FROM coin_coin WHERE user_id = :uid
        """
        return self.__cursor().execute(query, {'uid': user_id}).fetchone()

    def insert_follow(self, user_id: int):
        """
        Add user to followed list

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
        INSERT INTO coin_coin (user_id)
        VALUES (:uid)
        """
        self.__cursor().execute(query, {'uid': user_id})
        self.__commit()

    def delete_follow(self, user_id: int):
        """
        Forgot followed user

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
            DELETE FROM coin_coin
            WHERE user_id = ?
            """

        self.__cursor().execute(query, [user_id])
        self.__commit()
