from Life_insurance_class import NewPolicy, mode
import sqlite3
import datetime
import pandas as pd

conn = sqlite3.connect("LIFEINSURANCE.sqlite")
conn.execute(
    "CREATE TABLE IF NOT EXISTS LIFEINSURANCE (COMPANY TEXT, CUSTOMER_NAME TEXT, EMAIL TEXT, CONTACT_NO TEXT, "
    "ADDRESS TEXT, NOMINEE TEXT, "       +
    "POLICY_STATUS TEXT, POLICY_NAME TEXT, POLICY_NUMBER TEXT, ISSUE_DATE TEXT,MATURITY_DATE TEXT,PREMIUM_AMOUNT "
    "INTEGER, SUM_ASSURED INTEGER, "
    "POLICY_TERM INTEGER, PREMIUM_PAYING_TERM INTEGER,PAYMENT_MODE INTEGER, FIRST_YEAR_COMMISSION_PERCENT INTEGER, "
    "RENEWAL_COMMISSION_FOR_2_3_YEAR_PERCENT INTEGER,RENEWAL_COMMISSION_FOR_4_5_YEAR_PERCENT INTEGER, "
    "RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS_PERCENT INTEGER,GST_ON_FIRST_YEAR_COMMISSION INTEGER, "
    "GST_ON_RENEWAL_COMMISSION INTEGER, "
    "RENEWAL_DATE TEXT,"
    "FIRST_YEAR_COMMISSION INTEGER,"
    "RENEWAL_COMMISSION_FOR_2_3_YEAR INTEGER,"
    "RENEWAL_COMMISSION_FOR_4_5_YEAR INTEGER,"
    "RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS INTEGER,"
    "NOTE TEXT)")


def create_an_entry_in_the_database(policy_info: dict):
    policy_to_be_added = NewPolicy(str(policy_info["COMPANY"]), policy_info["CUSTOMER_NAME"], policy_info["EMAIL"],
                                   policy_info["CONTACT_NO"], policy_info["ADDRESS"], policy_info["NOMINEE"],
                                   policy_info["POLICY_STATUS"], policy_info["POLICY_NAME"],
                                   policy_info["POLICY_NUMBER"],
                                   policy_info["ISSUE_DATE"],
                                   policy_info["MATURITY_DATE"],
                                   policy_info["PREMIUM_AMOUNT"],
                                   policy_info["SUM_ASSURED"], policy_info["POLICY_TERM"],
                                   policy_info["PREMIUM_PAYING_TERM"],
                                   policy_info["PAYMENT_MODE"], policy_info["FIRST_YEAR_COMMISSION_PERCENT"],
                                   policy_info["RENEWAL_COMMISSION_FOR_2_3_YEAR_PERCENT"],
                                   policy_info["RENEWAL_COMMISSION_FOR_4_5_YEAR_PERCENT"],
                                   policy_info["RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS_PERCENT"],
                                   policy_info["GST_ON_FIRST_YEAR_COMMISSION"],
                                   policy_info["GST_ON_RENEWAL_COMMISSION"]
                                   )
    conn=sqlite3.connect("LIFEINSURANCE.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT  INTO LIFEINSURANCE (COMPANY , CUSTOMER_NAME , EMAIL , CONTACT_NO , "
                   "ADDRESS , NOMINEE , "
                   "POLICY_STATUS , POLICY_NAME , POLICY_NUMBER , ISSUE_DATE ,MATURITY_DATE ,PREMIUM_AMOUNT "
                   ", SUM_ASSURED , "
                   "POLICY_TERM , PREMIUM_PAYING_TERM ,PAYMENT_MODE , FIRST_YEAR_COMMISSION_PERCENT , "
                   "RENEWAL_COMMISSION_FOR_2_3_YEAR_PERCENT ,RENEWAL_COMMISSION_FOR_4_5_YEAR_PERCENT , "
                   "RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS_PERCENT ,GST_ON_FIRST_YEAR_COMMISSION , "
                   "GST_ON_RENEWAL_COMMISSION , "
                   "RENEWAL_DATE ,"
                   "FIRST_YEAR_COMMISSION ,"
                   "RENEWAL_COMMISSION_FOR_2_3_YEAR ,"
                   "RENEWAL_COMMISSION_FOR_4_5_YEAR ,"
                   "RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS ,"
                   "NOTE ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (policy_to_be_added.company,
                    policy_to_be_added.customer_name,
                    policy_to_be_added.email,
                    str(policy_to_be_added.contact_no),
                    policy_to_be_added.address,
                    policy_to_be_added.nominee,
                    policy_to_be_added.policy_status,
                    policy_to_be_added.policy_name,
                    str(policy_to_be_added.policy_number),
                    str(policy_to_be_added.issue_date),
                    str(policy_to_be_added.maturity_date),
                    int(policy_to_be_added.premium_amount),
                    int(policy_to_be_added.sum_assured),
                    int(policy_to_be_added.policy_term),
                    int(policy_to_be_added.premium_paying_term),
                    str(policy_to_be_added.payment_mode),
                    int(policy_to_be_added.first_year_commission_percent),
                    int(policy_to_be_added.renewal_commission_for_2_3_year_percent),
                    int(policy_to_be_added.renewal_commission_for_4_5_year_percent),
                    int(policy_to_be_added.renewal_commission_for_6_year_onwards_percent),
                    int(policy_to_be_added.gst_on_first_year_commission),
                    int(policy_to_be_added.gst_on_renewal_commission),
                    str(policy_to_be_added.renewal_date), int(policy_to_be_added.first_year_commission),
                    int(policy_to_be_added.renewal_commission_for_2_3_year),
                    int(policy_to_be_added.renewal_commission_for_4_5_year),
                    int(policy_to_be_added.renewal_commission_for_6_year_onwards), str(policy_to_be_added.note)))
    cursor.connection.commit()
    cursor.close()


def insert_to_database(path:str):
    frame = pd.read_excel(path)
    print(frame.index)
    print(dict(frame.iloc[0]))

    for j in frame.index:
        dictionary = dict(frame.iloc[j])
        create_an_entry_in_the_database(dictionary)



conn.commit()
conn.close()
