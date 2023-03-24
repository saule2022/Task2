import glob
import pandas as pd

# Define the input directories
users_dir = 'Data/users'
clicks_dir = 'Data/clicks'

# Create an empty DataFrame to store the filtered clicks
filtered_clicks = pd.DataFrame(columns=['date', 'id', 'click_target'])

# Read the user files into a single DataFrame
users_df = pd.concat([pd.read_csv(file) for file in sorted(glob.glob(users_dir + "/part-*.csv"))])

# Filter the users from Lithuania
lt_users = users_df[users_df['country'] == 'LT']

# Read the clicks files into a single DataFrame
clicks_df = pd.concat([pd.read_csv(file) for file in sorted(glob.glob(clicks_dir + "/part-*.csv"))])

# Filter the clicks by user_id and country
lt_clicks = clicks_df[clicks_df['user_id'].isin(lt_users['id'])]

# # Append the filtered clicks to the DataFrame
filtered_clicks = filtered_clicks.append(lt_clicks, ignore_index=True)


# Write the filtered clicks to a CSV file
filtered_clicks.to_csv('Data/filtered_clicks2.csv', index=False)


