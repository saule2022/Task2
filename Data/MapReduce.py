import pandas as pd
import glob

# Read all the files from the "data/clicks" folder and concatenate them into
# a single DataFrame using pandas library.
clicks_dir = 'Data/clicks'
clicks_df = pd.concat([pd.read_csv(file) for file in sorted(glob.glob(clicks_dir + "/part-*.csv"))])

# Use map and lambda to create a new column in the DataFrame with a value of 1 for each row,
# which will allow us to count the number of clicks for each date using the pandas groupby function.
clicks_df['click_count'] = clicks_df['user_id'].map(lambda x: 1)

# Group the clicks by date and count how many clicks there were for
#  each date using pandas groupby and sum functions.
total_clicks_df = clicks_df.groupby("date").agg({"click_count": "sum"}).reset_index()
total_clicks_df.columns = ["date", "count"]
# filtered_clicks2 = pd.DataFrame(columns=['date', 'count'])

# Write the "total_clicks_df" DataFrame to a new file called "data/total_clicks.csv".
total_clicks_df.to_csv("Data/total_clicks.csv", index=False)

# print(total_clicks_df)
print(clicks_df)
