# Chapter 3 – Storage and Retrieval

## The Big Idea

* When you `INSERT` or `SELECT` in a database, a lot happens under the hood.
* This chapter explains how databases **write to disk, organize data, and use indexes**.
* The focus is on two main storage engines: **log-structured** and **page-oriented**.

---

## Logs – The Foundation

* A **log** is the simplest storage: an append-only sequence of records.
* Fast to write (sequential disk I/O).
* Problem: Finding specific data requires scanning the whole log.
* Solution: Add **indexes**.

---

## Indexes

* An index helps you find data without scanning everything.
* Indexes = extra data structures that speed up lookups but add cost to writes.

### 1. Hash Indexes

* Simple: keep an in-memory hash map (key → position in file).
* Fast lookups.
* Problems: memory-heavy, not good for range queries.
* Used in **Bitcask (Riak)**.

### 2. SSTables and LSM-Trees

* **SSTable** = Sorted String Table (immutable, sorted key-value files).
* New writes go into memory first (memtable), then flushed to disk.
* Merging sorted files = efficient compaction.
* **LSM-tree (Log-Structured Merge Tree)** = combination of memtable + SSTables + compaction.
* Used in **LevelDB, RocksDB, Cassandra, HBase**.
* Strength: high write throughput.
* Weakness: reads may need to check multiple SSTables → solved with **Bloom filters**.

### 3. B-Trees

* Traditional indexing structure in relational databases.
* Data stored in sorted pages (blocks), each page pointing to others.
* Balanced tree → O(log n) lookups.
* Pages can be updated in place.
* Used in **MySQL (InnoDB), PostgreSQL, Oracle, SQL Server**.
* Strength: great for range queries and transactions.
* Weakness: writes involve random I/O, slower than LSM for heavy writes.

---

## Comparing B-Trees and LSM-Trees

* **B-Trees** → stable, good for reads, widely used.
* **LSM-Trees** → better for heavy writes, but compaction can cause write amplification.
* Trade-off depends on workload.

---

## Other Index Structures

* **Secondary indexes**: allow lookups by fields other than primary key.
* **Clustered index**: rows stored in order of index (good for range queries).
* **Covering index**: index contains enough data to answer query without touching main table.
* **Full-text search indexes**: inverted index (map words → documents).

---

## In-Memory Databases

* Some systems keep everything in memory (Redis, Memcached).
* Faster, but need durability strategies (snapshot to disk, write-ahead log).
* Trade-off: speed vs. persistence.

---

## OLTP vs. OLAP Storage

* **OLTP (Online Transaction Processing)** → many small, simple queries (banking, e-commerce). Needs fast writes and indexes.
* **OLAP (Online Analytical Processing)** → fewer, complex queries over large datasets (reporting, analytics). Needs columnar storage and efficient scans.
* Example: Data warehouses (Redshift, Snowflake, ClickHouse) use **column-oriented storage**.

---

## Takeaways

* All storage engines are variations on a few core ideas: append-only logs, sorted files, B-Trees.
* LSM-Trees and B-Trees are the two dominant families.
* Index choice = trade-off between read performance, write performance, and storage space.
* OLTP systems optimize for lots of small read/write transactions.
* OLAP systems optimize for large scans and aggregations.

</details>

---
