# school-surveillance
This is a set of python scripts that scrape BoardDocs data from schools in the top 30 districs which use BoardDocs as a platform. Each school district has a scraper file and a folder containing the scraped detailed meeting agendas.

Each scraper relies on the ability to identify the existing meeting IDs for all meetings that have occured in the past. The IDs are all currently loaded into each individual script, but to get the ID of a new school district you need to access the BoardDocs page and run the following command:

[...new Set(Array.from(document.querySelectorAll('.meeting'), el => el.id))]

Then the structure of the existing python scripts can be followed for any new school with a corresponding set of new IDs.
