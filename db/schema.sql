PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS animals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag_no TEXT UNIQUE NOT NULL,
  name TEXT,
  breed TEXT NOT NULL,
  sex TEXT NOT NULL CHECK (sex IN ('F', 'M')),
  dob DATE,
  lactation_no INTEGER DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'Active',
  purchase_price REAL DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS milk_yield (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_id INTEGER NOT NULL,
  entry_date DATE NOT NULL,
  session TEXT NOT NULL CHECK (session IN ('Morning','Evening')),
  liters REAL NOT NULL CHECK (liters >= 0),
  FOREIGN KEY(animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS health_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_id INTEGER NOT NULL,
  visit_date DATE NOT NULL,
  condition TEXT NOT NULL,
  treatment TEXT,
  vet_name TEXT,
  cost REAL DEFAULT 0,
  FOREIGN KEY(animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS vaccinations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_id INTEGER NOT NULL,
  vaccine_name TEXT NOT NULL,
  vaccination_date DATE NOT NULL,
  next_due_date DATE,
  cost REAL DEFAULT 0,
  FOREIGN KEY(animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS breeding_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_id INTEGER NOT NULL,
  service_date DATE NOT NULL,
  sire_name TEXT,
  method TEXT,
  pregnancy_check_date DATE,
  result TEXT,
  expected_calving_date DATE,
  FOREIGN KEY(animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS feed_logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  log_date DATE NOT NULL,
  feed_type TEXT NOT NULL,
  quantity_kg REAL NOT NULL,
  cost REAL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS expenses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  expense_date DATE NOT NULL,
  category TEXT NOT NULL,
  description TEXT,
  amount REAL NOT NULL CHECK (amount >= 0)
);

CREATE TABLE IF NOT EXISTS milk_sales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sale_date DATE NOT NULL,
  liters REAL NOT NULL CHECK (liters >= 0),
  rate_per_liter REAL NOT NULL CHECK (rate_per_liter >= 0)
);
