#!/bin/bash
docker-compose -f docker/compose/test.yml run achados unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
