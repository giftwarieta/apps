from deta import Deta  # pip install deta
DETA_KEY = "<YOUR DETA KEY>"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")
def insert_period(period, incomes, expenses, comment):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
