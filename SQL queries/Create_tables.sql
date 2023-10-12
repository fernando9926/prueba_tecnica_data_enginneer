CREATE TABLE charges (
    id VARCHAR(50) PRIMARY KEY NOT NULL,
    company_id VARCHAR(50) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME,
    FOREIGN KEY (company_id) REFERENCES companies (company_id)
);
