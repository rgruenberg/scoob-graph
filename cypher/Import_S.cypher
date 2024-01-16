CREATE (node:suspect
{ 	
	name: 'Jameson Hyde White',
	nickname: '',
	profession: ['professor', 'archaeologist'],
	appearances: 1,
	status: 'alive'
});
MATCH 	(s:suspect {name: 'Jameson Hyde White'}),
	(v: villain {alias: 'Black Knight'})
CREATE 	(s)-[:SUSPECT_FOR]->(v),
	(s)-[:VICTIM_OF]->(v);

CREATE (node:suspect
{ 	
	name: 'Mr. Wickles',
	nickname: '',
	profession: ['museum curator'],
	appearances: 1,
	status: 'incarcerated'
});
MATCH 	(s:suspect {name: 'Mr. Wickles'}),
	(v: villain {alias: 'Black Knight'})
CREATE 	(s)-[:SUSPECT_FOR]->(v),
	(s)-[:IS]->(v);

CREATE (node:suspect
{ 	
	name: 'Ebenezer Shark',
	nickname: '',
	profession: ['beach hermit'],
	appearances: 1,
	status: 'alive'
});
MATCH 	(s:suspect {name: 'Ebenezer Shark'}),
	(v: villain {alias: 'Ghost of Captain Cutler'})
CREATE 	(s)-[:SUSPECT_FOR]->(v);

CREATE (node:suspect
{ 	
	name: 'Captain Cutler',
	nickname: '',
	profession: ['sailor'],
	appearances: 1,
	status: 'incarcerated'
});
MATCH 	(s:suspect {name: 'Captain Cutler'}),
	(v: villain {alias: 'Ghost of Captain Cutler'})
CREATE 	(s)-[:IS]->(v);

CREATE (node:suspect
{ 	
	name: 'Mrs. Cutler',
	nickname: 'Widow Cutler',
	profession: ['lighthouse keeper, witch'],
	appearances: 1,
	status: 'incarcerated'
});
MATCH 	(s:suspect {name: 'Mrs. Cutler'}),
	(s2:suspect {name: 'Captain Cutler'}),
	(v: villain {alias: 'Ghost of Captain Cutler'})
CREATE 	(s)-[:SUSPECT_FOR]->(v),
	(s)-[:IN_LEAGUE_WITH]->(v),
	(s)-[:WIFE_OF]->(s2);

CREATE (node:suspect
{ 	
	name: 'Bluestone the Great',
	nickname: '',
	profession: ['magician'],
	appearances: 1,
	status: 'incarcerated'
});
MATCH 	(s:suspect {name: 'Bluestone the Great'}),
	(v: villain {alias: 'Phantom'})
CREATE 	(s)-[:IS]->(v);

CREATE (node:suspect
{ 	
	name: 'Big Ben',
	nickname: '',
	profession: ['guest ranch operator'],
	appearances: 1,
	status: 'alive'
});
MATCH 	(s:suspect {name: 'Big Beg'}),
	(v: villain {alias: 'Miner Forty-Niner'})
CREATE 	(s)-[:SUSPECT_FOR]->(v);

CREATE (node:suspect
{ 	
	name: 'Hank',
	nickname: '',
	profession: ['ranch caretaker'],
	appearances: 1,
	status: 'incarcerated'
});
MATCH 	(s:suspect {name: 'Hank'}),
	(v: villain {alias: 'Miner Forty-Niner'})
CREATE 	(s)-[:SUSPECT_FOR]->(v),
	(s)-[:IS]->(v);