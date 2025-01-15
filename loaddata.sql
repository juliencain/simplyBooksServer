CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "Author" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "email" varchar(50),
  "first_name" varchar(30),
  "last_name" varchar(30),
  "image" varchar,
  "favorite" BOOLEAN,
  "uid" varchar(30)
);

CREATE TABLE "Book" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "author_id" INTEGER,
  "title" varchar(50),
  "image" varchar,
  "price" DECIMAL(9,2),
  "sale" BOOLEAN,
  "uid" varchar(30),
  "description" varchar(280),
  FOREIGN KEY ("author_id") REFERENCES "Author"("id") ON DELETE CASCADE
);

INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.'),
(2, 'The Rum Diary', 'https://example.com/images/rum_diary.jpg', 12.00, 0, 'book-uid-002', 'Hunter S. Thompson\'s semi-autobiographical novel about a journalist\'s adventures in Puerto Rico.'),
(3, 'On the Road', 'https://example.com/images/on_the_road.jpg', 16.50, 1, 'book-uid-003', 'Jack Kerouac\'s seminal novel about the Beat Generation and the quest for freedom in post-war America.'),
(4, 'Dune', 'https://example.com/images/dune.jpg', 20.00, 0, 'book-uid-004', 'Frank Herbert\'s epic science fiction novel that explores politics, religion, and ecology on the desert planet of Arrakis.'),
(5, 'Harry Potter and the Sorcerer\'s Stone', 'https://example.com/images/harry_potter.jpg', 18.99, 1, 'book-uid-005', 'J.K. Rowling\'s magical first book in the Harry Potter series, where a young boy discovers he is a wizard.');

SELECT * FROM "Book";

INSERT INTO "Author" ("email", "first_name", "last_name", "image", "favorite", "uid")
VALUES
('hunter.thompson@example.com', 'Hunter', 'Thompson', 'https://example.com/images/hunter_thompson.jpg', 1, 'author-uid-001'),
('jack.kerouac@example.com', 'Jack', 'Kerouac', 'https://example.com/images/jack_kerouac.jpg', 1, 'author-uid-002'),
('frank.herbert@example.com', 'Frank', 'Herbert', 'https://example.com/images/frank_herbert.jpg', 0, 'author-uid-003'),
('jk.rowling@example.com', 'J.K.', 'Rowling', 'https://example.com/images/jk_rowling.jpg', 1, 'author-uid-004');


INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.'),
(1, 'The Rum Diary', 'https://example.com/images/rum_diary.jpg', 12.00, 0, 'book-uid-002', 'Hunter S. Thompson\'s semi-autobiographical novel about a journalist\'s adventures in Puerto Rico.'),
(2, 'On the Road', 'https://example.com/images/on_the_road.jpg', 16.50, 1, 'book-uid-003', 'Jack Kerouac\'s seminal novel about the Beat Generation and the quest for freedom in post-war America.'),
(3, 'Dune', 'https://example.com/images/dune.jpg', 20.00, 0, 'book-uid-004', 'Frank Herbert\'s epic science fiction novel that explores politics, religion, and ecology on the desert planet of Arrakis.'),
(4, 'Harry Potter and the Sorcerer\'s Stone', 'https://example.com/images/harry_potter.jpg', 18.99, 1, 'book-uid-005', 'J.K. Rowling\'s magical first book in the Harry Potter series, where a young boy discovers he is a wizard.');


INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.'),
(2, 'The Rum Diary', 'https://example.com/images/rum_diary.jpg', 12.00, 0, 'book-uid-002', 'Hunter S. Thompson\'s semi-autobiographical novel about a journalist\'s adventures in Puerto Rico.'),
(3, 'On the Road', 'https://example.com/images/on_the_road.jpg', 16.50, 1, 'book-uid-003', 'Jack Kerouac\'s seminal novel about the Beat Generation and the quest for freedom in post-war America.'),
(4, 'Dune', 'https://example.com/images/dune.jpg', 20.00, 0, 'book-uid-004', 'Frank Herbert\'s epic science fiction novel that explores politics, religion, and ecology on the desert planet of Arrakis.'),
(5, 'Harry Potter and the Sorcerer\'s Stone', 'https://example.com/images/harry_potter.jpg', 18.99, 1, 'book-uid-005', 'J.K. Rowling\'s magical first book in the Harry Potter series, where a young boy discovers he is a wizard.');


INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.');

INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.');

PRAGMA table_info("Book");

PRAGMA foreign_keys = ON;

PRAGMA foreign_keys;


INSERT INTO "Book" ("author_id", "title", "image", "price", "sale", "uid", "description")
VALUES
(1, 'Fear and Loathing in Las Vegas', 'https://example.com/images/fear_and_loathing.jpg', 14.99, 1, 'book-uid-001', 'Hunter S. Thompson\'s iconic book that explores the counterculture of the 1960s through a wild, drug-fueled road trip.');

