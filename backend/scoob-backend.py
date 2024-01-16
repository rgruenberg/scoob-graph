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
    """

    records, _, _ = driver.execute_query(query, database_=database, routing_="r")
    
    counts = {record['category']: record['count'] for record in records}
    return jsonify(counts)

if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    try:
        app.run(port=port)
    finally:
        driver.close()
