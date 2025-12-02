-- Campaign Analytics Database Schema
-- SQLite database script for creating campaigns table and inserting sample data

-- Create campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0,
    cost REAL NOT NULL DEFAULT 0.0,
    impressions INTEGER NOT NULL DEFAULT 0
);

-- Insert 10 sample campaigns
INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale 2024', 'Active', 15234, 3421.50, 125000),
('Black Friday Campaign', 'Active', 28456, 6789.25, 245000),
('Holiday Special', 'Paused', 8923, 2100.75, 98000),
('New Product Launch', 'Active', 12345, 4567.80, 156000),
('Spring Collection', 'Active', 18765, 5234.90, 198000),
('Back to School', 'Paused', 6543, 1890.40, 72000),
('Winter Clearance', 'Active', 22134, 6123.60, 234000),
('Valentine''s Day', 'Paused', 9876, 2345.20, 89000),
('Tech Innovation Week', 'Active', 15678, 4456.30, 167000),
('End of Year Sale', 'Active', 31245, 7890.10, 289000);

