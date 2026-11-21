from pytrends.request import TrendReq
import json

pytrends = TrendReq()

trends = pytrends.trending_searches(pn="united_states")

topics = trends[0].head(2).tolist()

with open("trends.json", "w") as f:
    json.dump(topics, f)
