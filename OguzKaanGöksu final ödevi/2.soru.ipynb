import pandas as pd

data = {'age': ['genc', 'genc', 'orta_yasli', 'yasli', 'yasli', 'yasli', 'or-ta_yasli', 'genc', 'genc', 'yasli', 'genc', 'orta_yasli', 'orta_yasli', 'yas-li'],
        'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'me-dium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
        'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no'],
        'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excel-lent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],
        'buy_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}

df = pd.DataFrame(data)
print(df)

total_instances = len(df)
buy_computer_count = len(df[df['buy_computer'] == 'yes'])
age_probability = {'genc': len(df[df['age'] == 'genc']) / total_instances,
                   'orta_yasli': len(df[df['age'] == 'orta_yasli']) / total_instances,
                   'yasli': len(df[df['age'] == 'yasli']) / total_instances}

income_probability = {'low': len(df[df['income'] == 'low']) / total_instances,
                      'medium': len(df[df['income'] == 'medium']) / total_instances,
                      'high': len(df[df['income'] == 'high']) / total_instances}

student_probability = {'no': len(df[df['student'] == 'no']) / total_instances,
                       'yes': len(df[df['student'] == 'yes']) / total_instances}

credit_rating_probability = {'fair': len(df[df['credit_rating'] == 'fair']) / total_instances,
                             'excellent': len(df[df['credit_rating'] == 'excel-lent']) / total_instances}

buy_computer_probability = buy_computer_count / total_instances

x_age = 'genc'
x_income = 'medium'
x_student = 'yes'
x_credit_rating = 'fair'

x_probability = age_probability[x_age] * income_probability[x_income] * student_probability[x_student] * credit_rating_probability[x_credit_rating]

buy_computer_given_x = (buy_computer_probability * x_probability) / x_probability
not_buy_computer_given_x = ((1 - buy_computer_probability) * x_probability) / x_probability

print("Kişinin bilgisayar alıp alma olasılığı:", buy_computer_given_x)
print("Kişinin bilgisayar almama olasılığı:", not_buy_computer_given_x)
# Kişinin bilgisayar alıp alma olasılığı için tablo
buy_computer_table = df.groupby(['age', 'income', 'student', 'cre-dit_rating'])['buy_computer'].apply(lambda x: sum(x == 'yes') / len(x)).reset_index().rename(columns={'buy_computer': 'buy_computer_given_x'})
print("Kişinin bilgisayar alıp alma olasılığı:")
print(buy_computer_table)

# Kişinin bilgisayar almama olasılığı için tablo
not_buy_computer_table = df.groupby(['age', 'income', 'student', 'cre-dit_rating'])['buy_computer'].apply(lambda x: sum(x == 'no') / len(x)).reset_index().rename(columns={'buy_computer': 'not_buy_computer_given_x'})
print("\nKişinin bilgisayar almama olasılığı:")
print(not_buy_computer_table)
