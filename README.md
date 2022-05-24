Used in the `update-1lib1ref` Toolforge tool.

# Usage instructions

* Add a client_secret.json per the [gspread instructions](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project).
* Update `spreadsheet_key` in update_1lib1ref.py with the key for this year's spreadsheet
* Update `dates` with the relevant date range
* Update the list of hashtags (`hashtags`)

Run the job with 
> toolforge-jobs run mytool --command update_1lib1ref.sh --image tf-python39

or schedule it for hourly runs with

> toolforge-jobs run mytool --command update_1lib1ref.sh --image tf-python39