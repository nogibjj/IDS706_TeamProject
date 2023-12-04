CREATE TABLE icu_beds (
    MMSA VARCHAR(255) NOT NULL,
    total_percent_at_risk DECIMAL(5, 2),  -- Nullable, as it might have NA values
    high_risk_per_icu_bed DECIMAL(10, 2),  -- DECIMAL to accommodate NA as NULL
    high_risk_per_hospital DECIMAL(10, 2),  -- DECIMAL to accommodate NA as NULL
    icu_beds INT,  -- Nullable, as it might have NA values
    hospitals INT,  -- Nullable, as it might have NA values
    total_at_risk DECIMAL(12, 2),  -- DECIMAL to accommodate large numbers with decimal places
    PRIMARY KEY (MMSA)
);
