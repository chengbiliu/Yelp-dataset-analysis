import sys
import json
import json_to_csv_converter
import pandas as pd
sys.path.append("C:\\Users\\golfbrother\\OneDrive - George Mason University\\Yelp project")

# json_to_csv_converter.read_and_write_file("checkin.txt","checkin.csv",["time",'business_id','type'])
# json_to_csv_converter.read_and_write_file("business.txt","business.csv",['business_id','name','neighborhood','address','city','state','postal_code','latitude','longitude','stars','review_count','is_open','attributes','categories','type'])
# json_to_csv_converter.read_and_write_file("review.txt","review.csv",["review_id",'user_id','business_id','stars','date','text','useful','type'])
# json_to_csv_converter.read_and_write_file("tip.txt","tip.csv",['business_id','user_id','date','text','likes','type'])
# json_to_csv_converter.read_and_write_file("user.txt","user.csv",["user_id",'name','review_count','yelping_since','friends','useful','funny','cool','fans','elite','average_stars','compliment_hot','compliment_more','compliment_profile','compliment_cute','compliment_list','compliment_note','compliment_plain','compliment_cool','compliment_funny','compliment_writer','compliment_photos','type'])

data=pd.read_csv('user.csv')
data['review_count'].unique()