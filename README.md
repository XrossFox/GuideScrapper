GuideScrapper

For those times you just want to download a guide as PDF

Usage:
Replace URL and pages with the respective URL from the guide you want to scrap and its pages
It works with HTML guides, for those that dont, set pages to 0 (Now working)

It requires (install with pip): 
BeautifulSoap 4
pdfkit

Also requires wkhtmltopdf. Google it. Rememeber to add bin folder to path if using windows

DONE:
Delete temporal folder before exit.
To make it compatible with single paged, spaghetti guides.

ISSUES:
While scrapping HTML guides, it adds some commas and square brackets at the beggining/end, programmer too lazy to figure out where the mistake was done