-- Database Migration Schema
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL
);

-- NOTE: Defect!
-- Foreign key references users(id) but lacks ON DELETE CASCADE!
-- Parent deletion in production leaves orphaned profile records.
CREATE TABLE user_profiles (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),
    bio TEXT
);
