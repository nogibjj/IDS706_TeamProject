CREATE TABLE icu_beds (
    MMSA VARCHAR(255) NOT NULL,
    total_percent_at_risk DECIMAL(5, 2) NOT NULL,
    high_risk_per_icu_bed INT NOT NULL,
    high_risk_per_hospital INT NOT NULL,
    icu_beds INT NOT NULL,
    hospitals INT NOT NULL,
    total_at_risk INT NOT NULL,
    PRIMARY KEY (MMSA)
);
