Select CAST(sack AS INTEGER) AS sack_int, * FROM bills;

select sum(passing_yards), sum(sack), sum(pass_touchdown), sum(pass_attempt), sum(complete_pass)
from bills
where passer_player_name = 'J.Allen' and season_type = 'REG';



SELECT COUNT(*) AS pass_attempts
FROM bills
WHERE passer_player_name = 'J.Allen'
  AND season_type = 'REG'
  AND pass_attempt = 1
  AND play_description NOT LIKE '%spike%'
  AND play_description NOT LIKE '%throwaway%'
  AND play_description NOT LIKE '%penalty%'
  AND play_description NOT LIKE '%two-point%'
;