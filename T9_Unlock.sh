#!/bin/bash
echo -n "Enter your IMEI: "
read -r IMEI
echo -n "${IMEI}simlock" | sha1sum | cut -c1-8
