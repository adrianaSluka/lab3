CREATE VIEW TablesJoined
AS SELECT shape, duration_sec, event_id, country_name, longitude
FROM comment3 
JOIN event3
ON event_event_id=event_id
JOIN place3 
ON (latitude=place_latitude AND longitude=place_longitude)
JOIN location3
ON (city_name=location_city_name AND country_country_name=country_name);