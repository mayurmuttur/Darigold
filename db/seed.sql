INSERT OR IGNORE INTO animals (tag_no, name, breed, sex, dob, lactation_no, status, purchase_price)
VALUES
('DG-001', 'Gauri', 'HF Cross', 'F', '2021-02-10', 2, 'Active', 65000),
('DG-002', 'Nandini', 'Jersey Cross', 'F', '2020-08-14', 3, 'Active', 70000),
('DG-003', 'Bheem', 'Sahiwal', 'M', '2022-01-05', 0, 'Active', 40000);

INSERT INTO milk_yield (animal_id, entry_date, session, liters)
SELECT id, '2026-04-29', 'Morning', 9.2 FROM animals WHERE tag_no = 'DG-001'
UNION ALL
SELECT id, '2026-04-29', 'Evening', 7.6 FROM animals WHERE tag_no = 'DG-001'
UNION ALL
SELECT id, '2026-04-29', 'Morning', 8.1 FROM animals WHERE tag_no = 'DG-002';

INSERT INTO milk_sales (sale_date, liters, rate_per_liter) VALUES
('2026-04-29', 240, 48),
('2026-04-30', 252, 49);

INSERT INTO expenses (expense_date, category, description, amount) VALUES
('2026-04-30', 'Labor', 'Milking labor', 2500),
('2026-04-30', 'Utilities', 'Electricity', 1800);
