import uuid
from flask import Flask, jsonify
from domain import Business, Coupon, Hours, Location
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/api/business')
def get():
    biz_list = load_fake_data()
    biz_list = [b.serialize() for b in biz_list]
    return jsonify(biz_list)

def load_fake_data():
    biz_list = []
    biz = Business(
        business_id=uuid.uuid4(),
        name="Leo's Bone Grill",
        phone="123-245-6789",
        desc="The place leo likes to eat at.  Only open Monday, Tuesday and Sundays!",
        website="woofwoofwoof.com"
    )

    loc = Location(
        lat=0,
        lon=0,
        address="123 Leo Dr",
        neighborhood="Wooftown"
    )

    hours = []
    hours.append(Hours(
        weekday="M",
        open_time="5:00",
        close_time="23:00"
    ))
    hours.append(Hours(
        weekday="T",
        open_time="5:00",
        close_time="23:00"
    ))
    hours.append(Hours(
        weekday="Su",
        open_time="12:00",
        close_time="17:00"
    ))

    loc.add_hours(hours)

    coups = []
    coups.append(Coupon(
        coupon_id=uuid.uuid4(),
        desc="Buy 1 Drink Get 1 Free",
        restrictions="Does not include Colas"
    ))
    coups.append(Coupon(
        coupon_id=uuid.uuid4(),
        desc="Buy 1 Meal Get 1 Free",
        restrictions="$5 MAX"
    ))

    biz.add_location(loc)
    biz.add_coupons(coups)
    biz_list.append(biz)

    return biz_list

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777, debug=True)
