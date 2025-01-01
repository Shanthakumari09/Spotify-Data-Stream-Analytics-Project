import random
import pandas as pd
import indian_names
from user_utils import UserUtils

# 1. Create sample location mapping CSV file
location_mapping_path = "location_mapping.csv"
location_data = {
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad'],
    'state': ['Maharashtra', 'Delhi', 'Karnataka', 'Telangana']
}
pd.DataFrame(location_data).to_csv(location_mapping_path, index=False)

# 2. Generate user demographic data
n_users = 10
users_df = UserUtils.generate_users_data(location_mapping_path, n_users)
print("Generated User Data:")
print(users_df)

# 3. Generate dates between a given range
start_date = "01-01-2022"
end_date = "10-01-2022"
dates_df = UserUtils.generate_dates_df(start_date, end_date)
print("\nGenerated Dates Data:")
print(dates_df)

# 4. Create sample songs DataFrame
song_data = {
    'song_id': [1, 2, 3, 4, 5],
    'release_date': pd.to_datetime(['2021-01-01', '2021-05-01', '2021-09-01', '2021-12-01', '2022-01-01']),
    'album_name': ['Album1', 'Album2', 'Album3', 'Album4', 'Album5'],
    'song_title': ['Song1', 'Song2', 'Song3', 'Song4', 'Song5']
}
songs_df = pd.DataFrame(song_data)

# 5. Generate user-song interactions
interaction_date = '2022-01-10'
start_ts = 1641772800  # Start timestamp for '2022-01-10'
end_ts = 1641859199    # End timestamp for '2022-01-10'
total_users = len(users_df)
songs_per_day_per_user = 2
users_per_day = 2

events_df = UserUtils.generate_user_song_interactions(
    users_df, songs_df, interaction_date, start_ts, end_ts, total_users, 
    songs_per_day_per_user, users_per_day
)
print("\nGenerated User-Song Interaction Data:")
print(events_df)
