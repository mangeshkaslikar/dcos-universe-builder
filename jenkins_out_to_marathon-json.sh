rm -f marathon.json
tee marathon.json &> /dev/null << EOF
{
  "id": "/test",
  "instances": 1,
  "portDefinitions": [],
  "container": {
    "type": "MESOS",
    "volumes": []
  },
  "cpus": 0.1,
  "mem": 128,
  "requirePorts": false,
  "networks": [],
  "healthChecks": [],
  "fetch": [],
  "constraints": [],
  "cmd": "echo 'hello' && sleep infinity"
}

EOF

cat marathon.json
