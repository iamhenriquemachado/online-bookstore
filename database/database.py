import sqlite3

connection = sqlite3.connect('onlinestore.db')
cursor = connection.cursor()

cursor.execute('''INSERT INTO books (title, author, price, description, stockquantity) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 10.99, 'A story of the Jazz Age in the United States, centered around the mysterious Jay Gatsby.', 25),
('1984', 'George Orwell', 12.99, 'A dystopian novel exploring the dangers of totalitarianism and surveillance.', 40),
('To Kill a Mockingbird', 'Harper Lee', 9.99, 'A story of racial injustice in the Deep South during the 1930s, seen through the eyes of a young girl.', 15),
('Moby-Dick', 'Herman Melville', 14.99, 'The epic tale of Captain Ahab’s obsessive quest to hunt the white whale, Moby-Dick.', 10),
('Pride and Prejudice', 'Jane Austen', 11.99, 'A classic romance exploring themes of class, love, and social expectations in 19th-century England.', 30),
('The Catcher in the Rye', 'J.D. Salinger', 13.49, 'The story of Holden Caulfield, a disenchanted teenager struggling with the complexities of life and identity.', 20),
('The Hobbit', 'J.R.R. Tolkien', 8.99, 'The prelude to the Lord of the Rings series, following Bilbo Baggins on his adventure to reclaim a treasure.', 50),
('War and Peace', 'Leo Tolstoy', 19.99, 'A sweeping epic of Russian society during the Napoleonic Wars, blending history with fiction.', 5),
('Brave New World', 'Aldous Huxley', 15.49, 'A dystopian novel imagining a future where technology and social engineering create a society devoid of individuality.', 35),
('The Lord of the Rings: The Fellowship of the Ring', 'J.R.R. Tolkien', 16.99, 'The first part of the epic fantasy trilogy, following the journey of Frodo Baggins and his companions to destroy the One Ring.', 45);
''')

connection.commit()
connection.close()