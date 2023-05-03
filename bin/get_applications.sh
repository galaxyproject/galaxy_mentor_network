
#!/usr/bin/env bash

python bin/prepare_data.py formatapplication \
    -au "https://docs.google.com/spreadsheets/d/1OjKawAHCyBKVpvt4azg9zSpGM1cvWRcT8q8bZ9pFX4k/export?format=csv&gid=1977280793" \
    -o "."