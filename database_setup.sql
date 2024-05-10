CREATE TABLE task_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    task_type TEXT NOT NULL,
    task_data TEXT NOT NULL,
    result TEXT NOT NULL,
    processed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
