import sqlite3

# Step 1: Connect to the SQLite database (or create one)
connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

# Step 2: Create the Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    conditions TEXT
);
""")

# Step 3: Insert sample data
cursor.executemany("""
INSERT INTO Patients (patient_id, patient_name, conditions) 
VALUES (?, ?, ?)
ON CONFLICT(patient_id) DO NOTHING;
""", [
    (1, 'Daniel', 'YFEV COUGH'),
    (2, 'Alice', ''),
    (3, 'Bob', 'DIAB100 MYOP'),
    (4, 'George', 'ACNE DIAB100'),
    (5, 'Alain', 'DIAB201')
])

# Step 4: Query patients with conditions starting with 'DIAB1'
cursor.execute("""
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE '%DIAB1%';
""")

# Step 5: Fetch and print the results
results = cursor.fetchall()
print("Patients with Type I Diabetes:")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Conditions: {row[2]}")

# Step 6: Close the connection
connection.commit()
connection.close()
