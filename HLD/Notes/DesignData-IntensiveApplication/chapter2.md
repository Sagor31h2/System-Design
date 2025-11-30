# Chapter 2 – Data Models and Query Languages

## Why Data Models Matter

* The data model decides how we *think about* and *work with* data.
* It’s the main interface between developers and the data.
* Different models encourage different ways of structuring applications.
* Example: If you choose a relational model, you think in terms of tables and joins. If you choose a document model, you think in terms of nested JSON-like structures.

---

## The Main Data Models

### 1. Relational Model (SQL)

* Data = tables (rows + columns).
* Query = SQL (Structured Query Language).
* Very mature, standardized, and widely used.
* Benefits:

  * Strong consistency guarantees.
  * Rich query language (joins, aggregations, filtering).
  * Good for structured, normalized data.
* Limitations:

  * Schema rigidity (though modern DBs allow some flexibility).
  * Not always natural for hierarchical or nested data.

---

### 2. Document Model (NoSQL, e.g., MongoDB, CouchDB)

* Data = documents (usually JSON, BSON, XML).
* Better fit for hierarchical/nested data.
* Example: A blog post with comments can be stored as a single document.
* Benefits:

  * More flexible schema (schema-less or schema-on-read).
  * Often maps more directly to application objects.
* Limitations:

  * Joins are weak or not supported → data may need to be duplicated.
  * Harder to enforce consistency across documents.

---

### 3. Graph Model (Neo4j, Titan, etc.)

* Data = nodes (entities) + edges (relationships).
* Good for highly interconnected data (social networks, recommendation systems, fraud detection).
* Query = declarative languages like Cypher, or traversal APIs (walk through graph).
* Benefits:

  * Relationships are first-class citizens.
  * Efficient traversal of complex connections.
* Limitations:

  * Not as widely adopted as relational/document models.
  * Performance can vary depending on graph size and query style.

---

## Query Languages

1. Declarative (SQL, Cypher, Datalog)

   * You specify *what* you want, not *how* to get it.
   * Database engine figures out the execution plan.
   * Example: `SELECT name FROM users WHERE age > 30`.
   * Advantage: Concise, optimizable, easier to maintain.

2. Imperative (low-level APIs, map-reduce, object traversal)

   * You specify *how* to get the data step by step.
   * Example: In map-reduce, you explicitly write map and reduce functions.
   * Advantage: More control, sometimes more flexible.
   * Disadvantage: More code, harder to optimize.

---

## Evolution of Data Models

* Early days → hierarchical (tree-like) and network models.
* 1970s → relational model became dominant.
* 2000s → rise of NoSQL due to web-scale needs.
* Today → polyglot persistence (use multiple models depending on the problem).

---

## The Big Picture of Chapter 2

* No single “best” model. Choice depends on use case.
* Relational is still strong, but document and graph models solve problems relational doesn’t handle as naturally.
* Query languages matter: declarative approaches are powerful because they let the database optimize queries for you.
* Modern systems often combine models (e.g., a relational core plus a document store for logs plus a graph engine for relationships).
</details>

---