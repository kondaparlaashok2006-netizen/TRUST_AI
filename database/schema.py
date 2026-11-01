
CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS evaluation_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    model_name TEXT NOT NULL,
    model_version TEXT NOT NULL,
    test_id TEXT NOT NULL,
    category TEXT,
    score REAL DEFAULT 0,
    passed INTEGER DEFAULT 0,
    input_prompt TEXT,
    model_output TEXT,
    evidence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(run_id, test_id)
);
"""
