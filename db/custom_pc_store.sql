DROP TABLE IF EXISTS components;
DROP TABLE IF EXISTS custom_pcs;

CREATE TABLE custom_pcs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    components VARCHAR(255) ARRAY DEFAULT '{}',
    total_price INT
);

CREATE TABLE components (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    custom_pc_id INT NOT NULL REFERENCES custom_pcs(id) ON DELETE CASCADE
);