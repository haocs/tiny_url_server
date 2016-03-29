CREATE USER 'tiny_url'@'localhost'
IDENTIFIED BY 'tiny1234';

GRANT ALL PRIVILEGES ON *.* TO 'tiny_url'@'localhost';
FLUSH PRIVILEGES;
