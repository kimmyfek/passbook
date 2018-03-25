import uuid
from flask import Flask, jsonify
from domain import Business, Coupon, Hours, Location
from queries import GET_ALL_QUERY

from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/DenverPassbook', pool_recycle=3600)

@app.route('/')
def index():
    return "Hello"

@app.route('/api/business')
def get():
    result = None
    biz_dict = {}
    loc_dict = {}
    with engine.connect() as conn:
        result = conn.execute(GET_ALL_QUERY).fetchall()

    if result:
        for row in result:
            if row.id not in biz_dict.keys():
                # biz is not in dict yet
                biz_dict[row.id] = Business(
                    business_id=row.id,
                    name=row.name,
                    desc=row.description,
                    website=row.website,
                    google_rating=row.google_rating,
                    price_level=row.price_level
                )

            loc = Location(
                loc_id=row.loc_id,
                lat=row.lat,
                lon=row.lon,
                address=row.address,
                neighborhood=row.neighborhood
            )
            biz_dict[row.id].add_location(loc)

            # lets build a location dict for the hours
            # for easy lookup
            if row.loc_id not in loc_dict:
                loc_dict[row.loc_id] = []

            loc_dict[row.loc_id].append(Hours(
                weekday=row.weekday,
                open_time=row.open_time,
                close_time=row.close_time,
                hour_id=row.hour_id
            ))

            coup = Coupon(
                coupon_id=row.coupon_id,
                desc=row.coup_desc,
                restrictions=row.restrictions,
                coup_type=row.coup_type
            )

            biz_dict[row.id].add_coupon(coup)

        for k,v in biz_dict.items():
            for loc in v.locations:
                if loc.loc_id in loc_dict.keys():
                    loc.add_hours(loc_dict[loc.loc_id])


        biz_list = [b.serialize() for b in biz_dict.values()]
    return jsonify(biz_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777, debug=True)
