import pymysql
from tabulate import tabulate

# Connect to MaxScale
db = pymysql.connect(
    host="10.0.0.66",
    port=4000,
    user="maxuser",
    passwd="maxpwd"
)

cursor = db.cursor()

