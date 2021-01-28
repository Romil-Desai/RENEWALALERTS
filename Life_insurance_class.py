import datetime

mode = {
    "ANNUAL": 365,
    "HALF-YEARLY": 180,
    "QUARTERLY": 90,
    "MONTHLY": 30
}


class NewPolicy:
    def __init__(self, company: str, customer_name: str, email: str, contact_no: str, address: str, nominee: str,
                 policy_status: str, policy_name: str, policy_number: str, issue_date: datetime.date,
                 maturity_date: datetime.date,
                 premium_amount: int, sum_assured: int, policy_term: int, premium_paying_term: int,
                 payment_mode: str, first_year_commission_percent: int, renewal_commission_for_2_3_year_percent: int,
                 renewal_commission_for_4_5_year_percent: int, renewal_commission_for_6_year_onwards_percent: int,
                 gst_on_first_year_commission: int, gst_on_renewal_commission: int):
        self.company = company
        self.customer_name = customer_name
        self.email = email
        self.contact_no = contact_no
        self.address = address
        self.nominee = nominee
        self.policy_status = policy_status
        self.policy_name = policy_name
        self.policy_number = policy_number
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.premium_amount = premium_amount
        self.sum_assured = sum_assured
        self.policy_term = policy_term
        self.premium_paying_term = premium_paying_term
        self.payment_mode = payment_mode
        self.first_year_commission_percent = first_year_commission_percent
        self.renewal_commission_for_2_3_year_percent = renewal_commission_for_2_3_year_percent
        self.renewal_commission_for_4_5_year_percent = renewal_commission_for_4_5_year_percent
        self.renewal_commission_for_6_year_onwards_percent = renewal_commission_for_6_year_onwards_percent
        self.gst_on_first_year_commission = gst_on_first_year_commission
        self.gst_on_renewal_commission = gst_on_renewal_commission
        self.renewal_date = self.issue_date + datetime.timedelta(days=mode[self.payment_mode])
        self.first_year_commission = (self.first_year_commission_percent/ 100) * (self.premium_amount - (self.premium_amount *
                                                                                                  (
                                                                                                          self.gst_on_first_year_commission / 100)))
        self.renewal_commission_for_2_3_year = (self.renewal_commission_for_2_3_year_percent / 100) * (
                self.premium_amount - (self.premium_amount *
                                       (self.gst_on_renewal_commission / 100)))
        self.renewal_commission_for_4_5_year = (self.renewal_commission_for_4_5_year_percent / 100) * (
                self.premium_amount - (self.premium_amount *
                                       (self.gst_on_renewal_commission / 100)))
        self.renewal_commission_for_6_year_onwards = (self.renewal_commission_for_6_year_onwards_percent / 100) * (
                self.premium_amount - (self.premium_amount *
                                       (self.gst_on_renewal_commission / 100)))

        self.note=""

    # def update_renewal(self):
    #     if datetime.date.today > self.renewal_date and self.renewal_status:
    #         self.renewal_date = self.renewal_date + datetime.timedelta(days=mode[self.payment_mode])
    #         self.renewal_status = False
    #
    # def add_renewal_status(self, renewal_date: datetime.datetime):
    #     self.premium_paid.append(renewal_date)
    #     self.renewal_status = True
