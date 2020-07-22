--lists all cities where state id is the same in cities' state id
SELECT cities.id, cities.name, states.name FROM states, cities WHERE cities.state_id = states.id ORDER BY cities.id ASC;
