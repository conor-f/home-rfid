CREATE TABLE cards (
  card_id TEXT NOT NULL UNIQUE PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  action_ids
);
CREATE TABLE actions (
  action_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  module TEXT NOT NULL,
  extra
);
CREATE TABLE state (
  is_configuring
);
