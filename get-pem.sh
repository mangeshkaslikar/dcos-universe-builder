#!/bin/bash

echo "Getting cert from host (make sure this is ONLY IP / hostname - not http://.. ): $1"
openssl s_client -showcerts -connect $1:443 </dev/null 2>/dev/null|openssl x509 -outform PEM > ./3.3.0-2.73.1/dcos.pem
