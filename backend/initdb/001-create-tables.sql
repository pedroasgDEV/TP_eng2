CREATE TABLE IF NOT EXISTS users (
    regis_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    passwrd VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS admins (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    passwrd VARCHAR(255) NOT NULL,
    derp VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS subjets (
    subjet_code VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    professor VARCHAR(255) NOT NULL,
    derp VARCHAR(255) NOT NULL,
    summary TEXT
);

CREATE TABLE IF NOT EXISTS user_subjects (
    user_id VARCHAR(255),
    subject_code VARCHAR(255),
    PRIMARY KEY (user_id, subject_code),
    FOREIGN KEY (user_id) REFERENCES users(regis_id),
    FOREIGN KEY (subject_code) REFERENCES subjects(subjet_code)
);

CREATE TABLE IF NOT EXISTS admin_subjects (
    admin_id VARCHAR(255),
    subject_code VARCHAR(255),
    PRIMARY KEY (admin_id, subject_code),
    FOREIGN KEY (admin_id) REFERENCES admins(id),
    FOREIGN KEY (subject_code) REFERENCES subjects(subjet_code)
);