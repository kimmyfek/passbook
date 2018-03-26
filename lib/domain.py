class BaseObject(object):
    def __init__(self):
        pass

    def serialize(self):
        return self.__dict__

class Business(BaseObject):
    def __init__(self, **kwargs):
        self.business_id = kwargs.get('business_id')
        self.name = kwargs.get('name')
        self.desc = kwargs.get('desc')
        self.price_level = kwargs.get('price_level')
        self.shutdown = False

        self.location_ids = []
        self.locations = []

        self.coupon_ids = []
        self.coupons = []

    def validate(self):
        if self.business_id is None or self.name is None \
        or self.desc is None or self.price_level is None:
            raise Exception("Required business fields: business_id, name, price_level, desc")

    def add_location(self, location):
        if location.loc_id not in self.location_ids:
            self.locations.append(location)
            self.location_ids.append(location.loc_id)
        shutdown_locs = [l.loc_id for l in self.locations if l.perm_closed]
        if len(shutdown_locs) == len(self.locations):
            self.shutdown = True
        else:
            self.shutdown = False


    def add_coupon(self, coupon):
        if coupon.coupon_id not in self.coupon_ids:
            self.coupons.append(coupon)
            self.coupon_ids.append(coupon.coupon_id)

    def serialize(self):
        if self.locations:
            self.locations = [l.serialize() for l in self.locations]
        if self.coupons:
            self.coupons = [c.serialize() for c in self.coupons]
        return self.__dict__

class Hours(BaseObject):
    def __init__(self, **kwargs):
        self.weekday = kwargs.get('weekday')
        self.open_time = kwargs.get('open_time')
        self.close_time = kwargs.get('close_time')
        self.hour_id = kwargs.get('hour_id')

class Location(BaseObject):
    def __init__(self, **kwargs):
        self.loc_id = kwargs.get('loc_id')
        self.lat = kwargs.get('lat')
        self.lon = kwargs.get('lon')
        self.address = kwargs.get('address')
        self.neighborhood = kwargs.get('neighborhood')
        self.website = kwargs.get('website')
        self.google_rating = kwargs.get('google_rating')
        self.phone = kwargs.get('phone')
        self.active = kwargs.get('active', True)
        self.perm_closed = kwargs.get('perm_closed', False)

        self.hours = []

    def validate(self):
        if self.address is None or self.neighborhood is None \
        or self.active is None or self.phone is None or self.website is None:
            raise Exception("Required location fields: address, neighborhood, active, phone, website")

    def add_hours(self, hours):
        hour_ids = []
        for h in hours:
            if h.hour_id not in hour_ids:
                hour_ids.append(h.hour_id)
                self.hours.append(h)

    def serialize(self):
        if self.hours:
            self.hours = [h.serialize() for h in self.hours]
        return self.__dict__

class Coupon(BaseObject):
    def __init__(self, **kwargs):
        self.coupon_id = kwargs.get('coupon_id')
        self.desc = kwargs.get('desc')
        self.restrictions = kwargs.get('restrictions')
        self.coup_type = kwargs.get('coup_type')
