/* JOINS SQL RANDOM EXAMPLES*/
/*
1.
*/
select B.name,B.email,A.district
FROM (
select address_id,district from address
where district = 'California') A
INNER JOIN 
(select concat(first_name,' ',last_name)as name,email,address_id from customer) B
ON A.address_id = B.address_id
/*
2.
*/
select concat(A.first_name,' ',A.last_name)as actor_name, C.title 
from actor A
INNER JOIN 
film_actor B
ON A.actor_id = B.actor_id
INNER JOIN 
film C
ON B.film_id = C.film_id
where first_name = 'Nick' and last_name = 'Wahlberg'