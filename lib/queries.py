GET_ALL_QUERY = """
SELECT
b.id
, b.name
, l.phone
, b.description
, l.website
, l.google_rating
, b.price_level
, l.id as loc_id
, l.lat
, l.lon
, l.address
, l.neighborhood
, l.active
, l.perm_closed
, h.id as hour_id
, h.weekday
, h.open_time
, h.close_time
, c.id as coupon_id
, c.description as coup_desc
, c.restrictions
, c.coup_type
FROM Businesses b
LEFT OUTER JOIN Locations l on l.bus_id = b.id
LEFT OUTER JOIN Hours h on h.location_id = l.id
LEFT OUTER JOIN Coupons c on b.id = c.bus_id
ORDER BY b.name, l.neighborhood, l.address
"""

UPDATE_BUS_QUERY = """
UPDATE Businesses SET description = '%(desc)s', price_level = '%(price_level)s'
WHERE id = %(business_id)s
"""

UPDATE_LOC_QUERY = """
UPDATE Locations SET address = '%(address)s', neighborhood = '%(neighborhood)s'
phone = '%(phone)s', active = '%(active)s', website = '%(website)s'
WHERE id = %(loc_id)s
"""
