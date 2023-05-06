#! /bin/bash
dropdb team8
createdb team8
psql -f CreateTables.sql team8

