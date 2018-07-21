-- 1. What query would you run to get the total revenue for March of 2012?
SELECT charged_datetime AS 'month', SUM(amount) AS revenue
FROM billing
WHERE charged_datetime BETWEEN '2012-3-1' AND '2012-3-31';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, sum(amount) AS revenue
FROM billing
WHERE client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT client_id, domain_name
FROM sites
WHERE client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT client_id, monthname(created_datetime), year(created_datetime)
FROM sites
WHERE client_id = 1;

SELECT client_id, monthname(created_datetime), year(created_datetime)
FROM sites
WHERE client_id = 20;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS website, COUNT(sites.created_datetime) AS leads_generated, date(sites.created_datetime) AS date
FROM sites
JOIN leads ON sites.site_id = leads.leads_id
WHERE created_datetime BETWEEN '2011-1-1' AND '2011-2-15'
GROUP BY sites.domain_name;

-- What query would you run to get a list of client names and the total # of leads
-- we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M') AS 'month'
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);

-- verify the above query results with the query below...
-- SELECT clients.first_name, clients.last_name, leads.*
-- FROM clients
	-- JOIN sites ON clients.id = sites.clients_id
    -- JOIN leads ON sites.id = leads.sites_id
-- WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
-- ORDER BY leads.registered_datetime;

-- What query would you run to get a list of client names and the total # of leads
-- we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011?
-- Order it by clients id
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

-- Come up with a second query that shows all the clients, the site name(s),
-- and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.domain_name;

-- Write a single query that retrieves total revenue collected from each client for each month of the year. Order by client id.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS monthly_revenue, DATE_FORMAT(billing.charged_datetime, '%M') AS 'month', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year'
FROM clients
	LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
ORDER BY clients.client_id;

-- Write a single query that retrieves all the sites that each client owns.
-- Group the results so that each row shows a new client. It will become clearer when you
-- add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS 'sites'
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;