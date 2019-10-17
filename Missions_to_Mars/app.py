from flask import Flask, render_template
import pymongo
import scrape_mars_mission

# Create an instance of Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars_mission'

client = pymongo.MongoClient(conn)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    scrape_mars_mission = client.db.marsmission.find_one()
    return render_template("index.html", scrape_mars_mission=scrape_mars_mission)

# Scraping info
@app.route("/scrape")
def scrape():
    coll = client.db.marsmission
    mars_info = scrape_mars_mission.scrape_mars_mission()
    coll.update({}, mars_info)
    return "Scraped!"

if __name__ == "__main__":
    app.run(debug=True)
