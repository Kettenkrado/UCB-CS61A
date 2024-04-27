CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;

-- Q1: Open Early
select name from pizzas where open < 13 order by name;

-- Q2: Study Session
create table study as select name as name, max(14 - open, 0) as duration 
  from pizzas order by duration DESC;

-- Q3: Late Night Snack
create table snack as select pizzas.name || " closes at " || pizzas.close as status
  from pizzas, meals where meals.meal = "snack" and pizzas.close >= meals.time;

-- Q4: Double Pizza
-- Two meals at the same place
CREATE TABLE double AS
  SELECT a.meal AS first, b.meal AS second, name
  FROM meals AS a, meals AS b, pizzas
  WHERE b.time - a.time > 6
  AND pizzas.open <= a.time
  AND pizzas.close >= b.time;