


CREATE TABLE beerStyle (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	shortName VARCHAR,
	description VARCHAR,
	ibuMin INT,
	ibuMax DEC,
	abvMin DEC,
	abvMax DEC,
	srmMin DEC,
	srmMax DEC,
	ogMin DEC,
	ogMax DEC,
	fgMin DEC,
	fgMax DEC,
	createDate DATE,
	updateDate DATE
);


CREATE TABLE breweryLocations (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	brewery_type VARCHAR,
	street VARCHAR,
	city VARCHAR,
	state VARCHAR,
	postal_code VARCHAR,
	country VARCHAR,
	longitude DEC,
	latitude DEC,
	phone BIGINT,
	website_url VARCHAR,
	updated_at DATE
);


SELECT * FROM beerstyle order by id;
UPDATE beerstyle SET ibumin = 0
WHERE ibumin IS NULL;
UPDATE beerstyle SET ibumax = 0
WHERE ibumax IS NULL;
UPDATE beerstyle SET abvmin = 0
WHERE abvmin IS NULL;
UPDATE beerstyle SET abvmax = 0
WHERE abvmax IS NULL;
UPDATE beerstyle SET srmmin = 0
WHERE srmmin IS NULL;
UPDATE beerstyle SET srmmax = 0
WHERE srmmax IS NULL;
UPDATE beerstyle SET ogmin = 0
WHERE ogmin IS NULL;
UPDATE beerstyle SET ogmax = 0
WHERE ogmax IS NULL;
UPDATE beerstyle SET fgmin = 0
WHERE fgmin IS NULL;
UPDATE beerstyle SET fgmax = 0
WHERE fgmax IS NULL;
ALTER TABLE beerStyle
DROP COLUMN createdate;
ALTER TABLE beerStyle
DROP COLUMN updatedate;
DELETE FROM beerStyle
WHERE ID = 84;

SELECT 
	brewery_type, 
	latitude,
	longitude
FROM breweryLocations;
