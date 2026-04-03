select 
is_ai_used, 
count(r.request_id) AS total_requests,
count(o.order_id) AS total_orders,
round(count(o.order_id) * 100.0 / count(r.request_id), 2) AS conversion_rate_pct
from requests r
left join orders o on r.request_id = o.request_id
group by is_ai_used;

select u.referral_source, device_type, round(count(o.order_id)/count(r.request_id)*100.0, 2)  as convertion_rate
from users u
left join requests r on u.user_id = r.user_id
left join orders o on r.request_id=o.request_id
group by referral_source, device_type;

select device_type,
sum(o.total_price)/count(distinct u.user_id) as avg_revenue_from_user,
count(distinct r.user_id) as users
from users u
left join requests r on u.user_id = r.user_id
left join orders o on r.request_id=o.request_id
group by device_type ;

select 
u.device_type,
count(distinct u.user_id) as total_users,
count(distinct r.request_id) as total_requests,
count(distinct a.activity_id) as total_interactions,
count(distinct o.order_id) as total_orders,
round(count(distinct o.order_id) * 100.0 / count(distinct r.request_id), 2) as conv_request_to_order_pct
from users u
left join requests r on u.user_id = r.user_id
left join activities a on r.request_id = a.request_id AND a.is_liked = 1
left join orders o on r.request_id = o.request_id
group by u.device_type;

select avg(timestampdiff(minute, r.request_date, o.order_date)) as avg_time_before_ordering from requests r
inner join orders o on r.request_id = o.request_id;
