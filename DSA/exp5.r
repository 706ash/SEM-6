library(sqldf)
data(iris)

sqldf("
  SELECT * 
  FROM iris 
  WHERE Species = 'versicolor' 
    AND [Sepal.Width] > (
      SELECT AVG([Sepal.Width]) 
      FROM iris 
      WHERE Species = 'versicolor'
    )
")

sqldf("
  SELECT AVG([Sepal.Width]) AS avg_sepal_width
  FROM iris 
  WHERE Species = 'versicolor' 
    AND [Petal.Length] < 5
")

library(glue)
iris <- sqldf(glue("
  SELECT
    [Sepal.Length],
    [Sepal.Width],
    [Petal.Length],
    CASE 
      WHEN Species = 'versicolor' THEN 14 
      ELSE [Petal.Width] 
    END AS [Petal.Width],
    Species
  FROM iris
"))


sqldf("Select * from iris")
