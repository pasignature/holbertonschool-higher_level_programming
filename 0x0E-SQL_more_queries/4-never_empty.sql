-- creates new table if not exist and makes id default and non-null
CREATE TABLE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1, name VARCHAR(256));
