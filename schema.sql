CREATE TABLE movie (
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    director VARCHAR(255) NOT NULL,
    actors VARCHAR(255) NOT NULL,
    rating DECIMAL(10, 2) NOT NULL,
    runtime INT NOT NULL,
    censor VARCHAR(255) NULL,
    gross VARCHAR(255) NULL,
    genre_main VARCHAR(255) NOT NULL,
    genre_side VARCHAR(255) NOT NULL,
    PRIMARY KEY (title)
);