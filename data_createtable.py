import pymysql

db, cur = None,None

db = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='telco_churn',charset='utf8')
cur = db.cursor()

my_table = "CREATE TABLE IF NOT EXISTS the_telco_churn(ID INT AUTO_INCREMENT PRIMARY KEY, COLLEGE VARCHAR(4), INCOME INT, OVERAGE INT, LEFTOVER INT, HOUSE INT, HANDSET_PRICE INT, OVER_15MINS_CALLS_PER_MONTH INT, AVERAGE_CALL_DURATION INT, REPORTED_SATISFACTION VARCHAR(10), REPORTED_USAGE_LEVEL VARCHAR(10), CONSIDERING_CHANGE_OF_PLAN VARCHAR(10), LEAVECHECK VARCHAR(8))"

cur.execute(my_table)

db.commit()

db.close()