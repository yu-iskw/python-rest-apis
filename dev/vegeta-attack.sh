#!/bin/bash
set -e

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd -P )"
echo $SCRIPT_DIR

NUM_CONNECTIONS_LIST="10000"
RATE_LIST="10 100 200 500"
DURATION="60s"
TARGETS_PATH="${SCRIPT_DIR}/resources/vegeta-targets.txt"
BODY_PATH="${SCRIPT_DIR}/resources/test-body.json"

echo "targets: ${TARGETS_PATH}"
echo "body: ${BODY_PATH}"

for NUM_CONNECTIONS in ${NUM_CONNECTIONS_LIST}
do
  for RATE in ${RATE_LIST}
  do
    echo "-------------------------------"
    echo "connections: ${NUM_CONNECTIONS}"
    echo "rate: ${RATE}"
    echo "duration: ${DURATION}"

    OUTPUT="connections-${NUM_CONNECTIONS}_rate-${RATE}_duration-${DURATION}.bin"
    vegeta attack \
      -rate=${RATE} \
      -duration=${DURATION} \
      -connections=${NUM_CONNECTIONS} \
      -body="${BODY_PATH}" \
      -targets="${TARGETS_PATH}" \
      -output="${OUTPUT}"
  done
done
