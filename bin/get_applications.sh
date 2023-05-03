
#!/usr/bin/env bash

python bin/prepare_data.py formatapplication \
    -au "https://docs.google.com/spreadsheets/d/1kPgPvIQYx7yzohA3IBjWhDnQ4KqX2kYQ_qsIL7w_TSg/export?format=csv&gid=1151339964" \
    -o "."