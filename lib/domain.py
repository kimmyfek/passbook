class BaseObject(object):
    def __init__(self):
        pass

    def serialize(self):
        return self.__dict__

class Business(BaseObject):
    def __init__(self, **kwargs):
        self.business_id = kwargs.get('business_id')
        self.name = kwargs.get('name')
        self.phone = kwargs.get('phone')
        self.desc = kwargs.get('desc')
        self.website = kwargs.get('website')

        self.locations = []
        self.coupons = []

    def add_location(self, location):
        self.locations.append(location)

    def add_locations(self, locations):
        self.locations = locations

    def add_coupons(self, coupons):
        self.coupons = coupons

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

class Location(BaseObject):
    def __init__(self, **kwargs):
        self.lat = kwargs.get('lat')
        self.lon = kwargs.get('lon')
        self.address = kwargs.get('address')
        self.neighborhood = kwargs.get('neighborhood')

        self.hours = []

    def add_hours(self, hours):
        self.hours = hours

    def serialize(self):
        if self.hours:
            self.hours = [h.serialize() for h in self.hours]
        return self.__dict__

class Coupon(BaseObject):
    def __init__(self, **kwargs):
        self.coupon_id = kwargs.get('coupon_id')
        self.desc = kwargs.get('desc')
        self.restrictions = kwargs.get('restrictions')
