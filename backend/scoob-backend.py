#!/usr/bin/env python
import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from neo4j import GraphDatabase, basic_auth

app = Flask(__name__)

CORS(app)

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "password")
neo4j_version = os.getenv("NEO4J_VERSION", "5")
database = os.getenv("NEO4J_DATABASE", "neo4j")

port = int(os.getenv("PORT", 8080))

driver = GraphDatabase.driver(url, auth=basic_auth(username, password))

@app.route("/totals")
def get_totals():
    query = """
    MATCH (n:investigator) RETURN 'investigators' AS category, COUNT(n) AS count
    UNION ALL
    MATCH (v:villain) RETURN 'villains' AS category, COUNT(v) AS count
    UNION ALL
    MATCH (s:suspect) RETURN 'suspects' AS category, COUNT(s) AS count
    UNION ALL
    MATCH (c:collaborator) RETURN 'collaborator' AS category, COUNT(c) AS count
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'count': record['count'], 'category': record['category']} for record in records]
    return jsonify(counts)

@app.route("/caught")
def get_caught_totals():
    query = """
    MATCH (i:investigator)<-[:CAUGHT_BY]-(v:villain)
    WITH i, COUNT(*) AS catchersCount
    RETURN i.name, catchersCount
    ORDER BY catchersCount DESC
    LIMIT 5
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'name': record['i.name'], 'catchersCount': record['catchersCount']} for record in records]
    return jsonify(counts)

@app.route("/unmasked")
def get_unmasked_totals():
    query = """
    MATCH (i:investigator)<-[:UNMASKED_BY]-(v:villain)
    WITH i, COUNT(*) AS unmaskerCount
    RETURN i.name, unmaskerCount
    ORDER BY unmaskerCount DESC
    LIMIT 5
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'name': record['i.name'], 'unmaskerCount': record['unmaskerCount']} for record in records]
    return jsonify(counts)

@app.route("/catchphrase")
def get_trope_totals():
    query = """
    MATCH (i:investigator)
    WHERE ANY(phrase IN keys(i) 
        WHERE phrase ENDS WITH '_count' 
        AND i[phrase] IS NOT NULL)
    WITH i, REDUCE(s = 0, phrase IN keys(i) | s + CASE 
        WHEN phrase ENDS WITH '_count' 
        THEN i[phrase] ELSE 0 END) AS totalCatchphrases
    UNWIND keys(i) AS phrase
    WITH i, phrase, totalCatchphrases, i[phrase] AS count
    WHERE phrase ENDS WITH '_count' 
        AND count IS NOT NULL
    RETURN i.name AS investigatorName, phrase AS catchphrase, count AS catchphraseCount
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'name': record['investigatorName'], 'phrase': record['catchphrase'], 'tropeCount': record['catchphraseCount']} for record in records]
    return jsonify(counts)

@app.route("/tropeCaught")
def get_scatter_totals():
    query = """
    MATCH (i:investigator)<-[CAUGHT_BY]-()
    WITH i, COUNT(CAUGHT_BY) AS caughtCount
    WHERE ANY(phrase IN keys(i) WHERE phrase ENDS WITH '_count' AND i[phrase] IS NOT NULL)
    WITH i, caughtCount, REDUCE(s = 0, phrase IN keys(i) | s + CASE WHEN phrase ENDS WITH '_count' THEN i[phrase] ELSE 0 END) AS totalTropeCount
    RETURN i.name AS investigatorName, caughtCount, totalTropeCount
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'name': record['investigatorName'], 'caught': record['caughtCount'], 'tropeCount': record['totalTropeCount']} for record in records]
    return jsonify(counts)

@app.route("/villainType")
def get_villain_type_totals():
    query = """
    MATCH (v:villain)
    RETURN v.type, COUNT(v) AS count
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'type': record['v.type'], 'typeCount': record['count']} for record in records]
    return jsonify(counts)

@app.route("/motives")
def get_motive_totals():
    query = """
    MATCH (v:villain)
    WHERE (v.motive IS NOT NULL)
    RETURN v.motive, COUNT(v) AS count
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'motive': record['v.motive'], 'motiveCount': record['count']} for record in records]
    return jsonify(counts)

@app.route("/realness")
def get_realness_totals():
    query = """
    MATCH (v:villain)
    WHERE (v.realness IS NOT NULL)
    RETURN v.realness, COUNT(v) AS count
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'realness': record['v.realness'], 'realCount': record['count']} for record in records]
    return jsonify(counts)

@app.route("/status")
def get_status_totals():
    query = """
    MATCH (s:suspect)
    WHERE (s.status IS NOT NULL)
    RETURN s.status, COUNT(s) AS count
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = [{'status': record['s.status'], 'statusCount': record['count']} for record in records]
    return jsonify(counts)

if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    try:
        app.run(port=port)
    finally:
        driver.close()
