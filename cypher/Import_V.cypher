CREATE (node:villain
{ 	
	alias: 'Black Knight',
	type: 'ghost',
	realness: 'fake',
	location: 'County Museum',
	motive: 'money',
	appearances: 1
});
MATCH 	(i:investigator {name: 'Scoobert Doobert Doo'}),
	(v: villain {alias: 'Black Knight'})
CREATE 	(v)-[:CAUGHT_BY]->(i),
	(v)-[:UNMASKED_BY]->(i);

CREATE (node:villain
{ 	
	alias: 'Ghost of Captain Cutler',
	type: 'ghost',
	realness: 'fake',
	location: 'Rock Point Beach',
	motive: 'money',
	appearances: 1
}); 
MATCH 	(i:investigator {name: 'Scoobert Doobert Doo'}),
	(i2:investigator {name: 'Fred Jones'}),
	(v: villain {alias: 'Ghost of Captain Cutler'})
CREATE 	(v)-[:CAUGHT_BY]->(i),
	(v)-[:UNMASKED_BY]->(i2);

CREATE (node:villain
{ 	
	alias: 'Phantom',
	type: 'ghost',
	realness: 'fake',
	location: 'Haunted Isle',
	motive: 'money',
	appearances: 1
}); 
MATCH 	(i:investigator {name: 'Scoobert Doobert Doo'}),
	(i2:investigator {name: 'Fred Jones'}),
	(v: villain {alias: 'Phantom'})
CREATE 	(v)-[:CAUGHT_BY]->(i),
	(v)-[:UNMASKED_BY]->(i2);

CREATE (node:villain
{ 	
	alias: 'Miner Forty-Niner',
	type: 'ghost',
	realness: 'fake',
	location: 'Gold City',
	motive: 'money',
	appearances: 1
}); 
MATCH 	(i:investigator {name: 'Scoobert Doobert Doo'}),
	(i2:investigator {name: 'Fred Jones'}),
	(v: villain {alias: 'Miner Forty-Niner'})
CREATE 	(v)-[:CAUGHT_BY]->(i),
	(v)-[:UNMASKED_BY]->(i2);