from flask import Flask, jsonify, request
from domain import Business, Coupon, Hours, Location
from queries import GET_ALL_QUERY, UPDATE_BUS_QUERY
from adapter import SqlAdapter

app = Flask(__name__)
conn_str = 'mysql+mysqlconnector://root:password@localhost:3306/DenverPassbook'
sql_adapter = SqlAdapter(conn_str)

@app.route('/api/business', methods=['POST'])
def update_biz():
    result = {}
    try:
        req = request.json
        bus = Business(
            business_id=req.get('business_id'),
            name=req.get('name'),
            desc=req.get('desc'),
            price_level=req.get('price_level')
        )
        bus.validate()

        bus = bus.serialize()
        sql_adapter.update(UPDATE_BUS_QUERY % bus)
        result['success'] = True
    except Exception as ex:
        print("Failed to update business object: %s" % ex)
        result['success'] = False
        result['error'] = str(ex)
    return jsonify(result)

@app.route('/api/business', methods=['GET'])
def get():
    result = None
    biz_dict = {}
    loc_dict = {}
    result = sql_adapter.fetchall(GET_ALL_QUERY)

    if result:
        for row in result:
            if row.id not in biz_dict.keys():
                # biz is not in dict yet
                biz_dict[row.id] = Business(
                    business_id=row.id,
                    name=row.name,
                    desc=row.description,
                    price_level=row.price_level
                )

            loc = Location(
                loc_id=row.loc_id,
                lat=row.lat,
                lon=row.lon,
                address=row.address,
                neighborhood=row.neighborhood,
                website=row.website,
                google_rating=row.google_rating,
                phone=row.phone
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
