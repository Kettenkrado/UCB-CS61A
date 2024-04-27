-- use the command: python3 sqlite_shell.py --init disc12.sql

CREATE TABLE original AS
  SELECT 1 AS n, "It's" AS word UNION
  SELECT 2     , "The"      UNION
  SELECT 3     , "End";

CREATE TABLE code AS
  SELECT "Up" AS x, "Down" AS y UNION
  SELECT "Now"    , "Home" UNION
  SELECT "It's"   , "What" UNION
  SELECT "See"    , "Do" UNION
  SELECT "Can"    , "See" UNION
  SELECT "End"    , "Now" UNION
  SELECT "What"   , "You" UNION
  SELECT "The"    , "Happens" UNION
  SELECT "Love"   , "Scheme" UNION
  SELECT "Not"    , "Mess" UNION
  SELECT "Happens", "Go";

CREATE TABLE decode1 AS 
  SELECT n AS n, y AS word
    FROM original, code
    WHERE word = x;

SELECT * FROM decode1 ORDER BY n;

CREATE TABLE decode2 AS 
  SELECT n AS n, y AS word
    FROM decode1, code
    WHERE word = x;

SELECT * FROM decode2 ORDER BY n;