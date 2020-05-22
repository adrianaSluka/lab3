-- Generated by Oracle SQL Developer Data Modeler 18.3.0.268.1156
--   at:        2020-05-18 22:16:21 EEST
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



CREATE TABLE comment3 (
    comment_id       INTEGER,
    comment_text     VARCHAR2(1000),
    duration_sec     INTEGER,
    datetime         TIMESTAMP,
    shape            VARCHAR2(15),
    event_event_id   INTEGER NOT NULL
);

ALTER TABLE comment3 ADD CONSTRAINT comment3_pk PRIMARY KEY ( comment_id );

CREATE TABLE country3 (
    country_name   VARCHAR2(20) NOT NULL
);

ALTER TABLE country3 ADD CONSTRAINT country3_pk PRIMARY KEY ( country_name );

CREATE TABLE event3 (
    event_id          INTEGER NOT NULL,
    place_longitude   FLOAT(126) NOT NULL,
    place_latitude    FLOAT(126) NOT NULL
);

ALTER TABLE event3 ADD CONSTRAINT event3_pk PRIMARY KEY ( event_id );

CREATE TABLE location3 (
    city_name              VARCHAR2(100),
    country_country_name   VARCHAR2(20) NOT NULL
);

ALTER TABLE location3 ADD CONSTRAINT location3_pk PRIMARY KEY ( city_name,
                                                               country_country_name );

CREATE TABLE place3 (
    latitude             FLOAT(126) NOT NULL UNIQUE,
    longitude            FLOAT(126) NOT NULL UNIQUE,
    location_city_name   VARCHAR2(100) NOT NULL,
    country_name         VARCHAR2(20) NOT NULL
);

ALTER TABLE place3 ADD CONSTRAINT place3_pk PRIMARY KEY ( latitude,longitude );

ALTER TABLE comment3
    ADD CONSTRAINT comment3_event3_fk FOREIGN KEY ( event_event_id )
        REFERENCES event3 ( event_id );

ALTER TABLE event3
    ADD CONSTRAINT event3_place3_fk FOREIGN KEY ( place_longitude,
                                                place_latitude )
        REFERENCES place3 ( longitude,
                            latitude );

ALTER TABLE location3
    ADD CONSTRAINT location3_country3_fk FOREIGN KEY ( country_country_name )
        REFERENCES country3 ( country_name );

ALTER TABLE place3
    ADD CONSTRAINT place3_location3_fk FOREIGN KEY ( location_city_name,
                                                   country_name )
        REFERENCES location3 ( city_name,
                               country_country_name );


