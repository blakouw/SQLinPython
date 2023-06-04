from unittest.mock import MagicMock

class CacheService:

    def __init__(self, session): # 1

        self.session = session # 2



    def get_status(self, number):

        self.session.execute('SELECT existing FROM numbers WHERE number=?', (number,))

        return self.session.fetchone()



    def save_status(self, number, existing):

        self.session.execute('INSERT INTO numbers VALUES (?, ?)', (number, existing))

        self.session.connection.commit()



    def generate_report(self):

        self.session.execute('SELECT COUNT(*) FROM numbers')

        count = self.session.fetchone()

        self.session.execute('SELECT COUNT(*) FROM numbers WHERE existing=1')

        count_existing = self.session.fetchone()

        return count_existing[0]/count[0]


def test_get_mock():

    session = MagicMock() # 1

    executor = MagicMock()

    session.execute = executor

    cache = CacheService(session) # 2

    cache.get_status('+3155512345')

    executor.assert_called_once_with('SELECT existing FROM numbers WHERE number=?', ('+3155512345',)) # 3
