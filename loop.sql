DECLARE
    rowss INT NOT NULL DEFAULT 4;
    TYPE countries_array IS VARRAY(4) OF country3.country_name%TYPE;
    countries_names countries_array := countries_array();
    TYPE cities_array IS VARRAY(4) OF location3.city_name%TYPE;
    cities_names cities_array :=cities_array();
BEGIN
    countries_names := countries_array('USA', 'Australia', 'UK', 'Canada');
    cities_names := cities_array('New York', 'Melbourne', 'London', 'Toronto');
    FOR i IN 1..rowss LOOP
        INSERT INTO country3
        VALUES (countries_names(i));
        INSERT INTO location3
        VALUES (cities_names(i), countries_names(i));
    END LOOP;
END;