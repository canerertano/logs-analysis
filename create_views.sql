CREATE VIEW most_popular_articles AS
	SELECT a.title, count(l.id) AS num
	FROM log l, articles a
	WHERE l.path = ('/article/'::text || a.slug)
	 AND l.status = '200 OK'::text
	GROUP BY a.title
	ORDER BY (count(l.id)) DESC;

CREATE VIEW most_popular_authors AS
	SELECT b.name, sum(x.num) AS number
	FROM ( SELECT a_1.title, count(l.id) AS num
		FROM log l, articles a_1
		WHERE l.path = ('/article/'::text || a_1.slug)
		AND l.status = '200 OK'::text
		GROUP BY a_1.title
		ORDER BY (count(l.id)) DESC) x, articles a, authors b
	WHERE a.title = x.title AND a.author = b.id
	GROUP BY b.name
	ORDER BY (sum(x.num)) DESC;

CREATE VIEW days_with_most_errors AS
	SELECT x.time,
	round((x.count * 100)::numeric / y.count::double precision::numeric, 2) AS rate
	FROM
	(SELECT count(*) AS count, date(log.time) AS time
		FROM log
		WHERE log.status = '404 NOT FOUND'::text
		GROUP BY (date(log.time))) x,
	(SELECT count(*) AS count, date(log.time) AS time
		FROM log
		GROUP BY (date(log.time))) y
	WHERE x.time = y.time
	ORDER BY (round((x.count * 100)::numeric / y.count::double precision::numeric, 2)) DESC;