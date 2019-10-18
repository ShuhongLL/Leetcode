# Write your MySQL query statement below
SELECT  	s1.Score,
        	(SELECT COUNT(DISTINCT Score) FROM Scores as s2 WHERE s2.Score >= s1.Score) AS Rank
FROM    	Scores AS S1
ORDER BY 	Score DESC