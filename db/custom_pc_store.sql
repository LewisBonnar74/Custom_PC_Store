DROP TABLE IF EXISTS custom_pcs;
DROP TABLE IF EXISTS psus;
DROP TABLE IF EXISTS motherboards;
DROP TABLE IF EXISTS rams;
DROP TABLE IF EXISTS cpus;
DROP TABLE IF EXISTS gpus;

CREATE TABLE gpus (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE cpus (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE rams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE motherboards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE psus (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE custom_pcs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    total_price INT,
    gpu_id INT NOT NULL REFERENCES gpus(id),
    cpu_id INT NOT NULL REFERENCES cpus(id),
    ram_id INT NOT NULL REFERENCES rams(id),
    motherboard_id INT NOT NULL REFERENCES motherboards(id),
    psu_id INT NOT NULL REFERENCES psus(id)
);