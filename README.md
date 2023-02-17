Used in the `update-1lib1ref` Toolforge tool ([link](https://toolsadmin.wikimedia.org/tools/id/update-1lib1ref)).

# Setup instructions

* Add a client_secret.json per the [gspread instructions](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project).
* `chmod +x update_1lib1ref.sh`
* Follow the [Toolforge Kubernetes instructions](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Python#Kubernetes_python_jobs) to bootstrap the venv.


* Update `spreadsheet_key` in update_1lib1ref.py with the key for this year's spreadsheet
* Update `dates` with the relevant date range
* Update the list of hashtags (`hashtags`)

Run the job with 
> toolforge-jobs run 1lib1ref --command 1Lib1Ref/update_1lib1ref.sh --image tf-python39

or schedule it for hourly runs with

> toolforge-jobs run 1lib1ref --command 1Lib1Ref/update_1lib1ref.sh --image tf-python39 --schedule "10 * * * *"

# Subsequent instructions
To get the script running for the latest campaign:
* SSH in to Toolforge ([instructions](https://wikitech.wikimedia.org/wiki/Help:Toolforge)) and `become update-1lib1ref`
* Edit `$HOME/1Lib1Ref/update_1lib1ref.py`
** Replace the value of `spreadsheet_key` on line 9 with the key from this campaign's spreadsheet URL
** Update `dates` on line 11 with the relevant campaign start and end dates
** On line 26 update the list of hashtags to track
* Check `toolforge-jobs list` to confirm that the job is still scheduled.
