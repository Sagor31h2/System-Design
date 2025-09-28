
#  Chapter 1 – Reliable, Scalable, and Maintainable Applications
<details>
<summary>Click to expand </summary>
This chapter is the **foundation** of the book. It doesn’t tell you *how* to build databases yet but explains *what good systems should look like* and *what problems we need to solve*.

---

##  Data-Intensive vs. Compute-Intensive

* **Compute-intensive** → main bottleneck is CPU (e.g., scientific simulations, image rendering).
* **Data-intensive** → main bottleneck is **data** (volume, complexity, or speed of access).
* Examples:

  * Facebook timeline → billions of reads/writes.
  * YouTube → store & stream petabytes.
  * Uber → real-time location updates, high read/write ratio.

Core tools we use:

* **Databases** → store/retrieve.
* **Caches** → speed up.
* **Indexes** → efficient search.
* **Streams/Queues** → communication.
* **Batch & Stream Processing** → transform data.

---

##  The Three Pillars

### 1. Reliability

**Definition**: The system works correctly **even when things go wrong**.

* **What can go wrong?**

  1. **Hardware faults**

     * Disk crash, memory failure, power outage.
     * Solution → redundancy (replicas, RAID, failover clusters).
  2. **Software faults**

     * Bugs, memory leaks, race conditions.
     * Harder to handle than hardware faults.
     * Solution → isolation, testing, rolling restarts.
  3. **Human errors**

     * Config mistakes, wrong deployment, accidental delete.
     * Solution → better tooling, safe defaults, automation, good UX for ops.

* **Fault vs. Failure**

  * *Fault* = something broke.
  * *Failure* = user sees a problem.
  * Goal: **tolerate faults without user-facing failure.**

---

### 2. Scalability

**Definition**: A system’s ability to cope with **increased load**.

* **Load parameters** depend on the system:

  * Web server → requests per second.
  * DB → read/write ratio, queries/sec.
  * Streaming → events/sec.
  * Data warehouse → dataset size.

* **Performance metrics**:

  * **Throughput** → how much work per unit of time.
  * **Latency** → how long one request takes (often measured in percentiles, e.g., 95th/99th percentile latency).

* **Scaling methods**:

  1. **Vertical scaling (scale up)** → stronger machine.

     * Easy but limited.
  2. **Horizontal scaling (scale out)** → more machines, distributed system.

     * Harder, but scales further.

* **Workload patterns** matter:

  * Read-heavy vs. write-heavy.
  * Sequential vs. random access.
  * Batch (e.g., nightly reports) vs. real-time (e.g., chat app).

---

### 3. Maintainability

**Definition**: Systems should stay **useful and manageable** in the long run.

* **Why important?** Most software spends more time in **maintenance** than initial development.

* **Aspects:**

  1. **Operability** → easy for ops team to monitor, debug, upgrade.

     * Good dashboards, logs, alerts.
  2. **Simplicity** → avoid unnecessary complexity.

     * Simple APIs, modular design, consistent naming.
  3. **Evolvability (or agility)** → easy to adapt to new requirements.

     * Refactorable code, flexible data models, test coverage.

---

##  Big Takeaway

Building a good data-intensive app = balancing **3 goals**:

* Reliable (don’t break when something fails).
* Scalable (handle growth).
* Maintainable (easy to work with in the long term).

You always face **trade-offs** — e.g., more scalability might add complexity → harder maintainability.

This sets the stage for the rest of the book:

* Storage & retrieval.
* Encoding & evolution.
* Replication.
* Partitioning.
* Consistency.
* Batch vs. stream processing.
</details>

---

# Chapter 2 – Data Models and Query Languages

<details>

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
