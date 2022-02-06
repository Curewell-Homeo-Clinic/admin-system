#!/bin/bash

## Constants
RED="\033[0;31m"
GREEN="\033[0;32m"
Blue="\033[0;34m"
NC="\033[0m"

INFO="\033[0;34m[INFO]\033[0m"
CHECK="${GREEN}✔${NC}"
ERROR="\033[0;31m[ERROR]\033[0m"

function check_if_heroku_installed {
	heroku_path="$(command -v heroku)"
	if [[ $heroku_path == "/usr/bin/heroku" ]]
	then
		echo -e "$INFO heroku cli is installed. $CHECK"
	else
		echo -e "$ERROR heroku cli isn't installed."
		exit 1
	fi
}

function check_auth_user {
	if [[ $(heroku auth:whoami) == "curewellhomeoclinic101@gmail.com" ]]
	then
		echo -e "$INFO heroku auth user logged in. $CHECK"
	else
		echo -e "$ERROR heroku - not auth user."
		exit 1
	fi
}

function check_build_file {
	file="$(pwd)/Dockerfile"
	if test -f "$file"; then
		echo -e "$INFO Dockerfile found. $CHECK"
	else
		echo -e "$ERROR Dockerfile doesn't exist"
		exit 1
	fi
}

function checks {
	check_if_heroku_installed
	# check_auth_user
	check_build_file
}

function deploy () {
	checks
	app_name=""
	
	if [[ $1 == "dev" ]]
	then
		app_name="curewell-dev"
	else
		app_name="curewell"
	fi

	read -p "Deploying to '$app_name', proceed [y/n]: " consent

	if [[ $consent == "y" || $consent == "Y" ]]
	then
		heroku container:push web -a $app_name
		heroku container:release web -a $app_name
	else
		echo -e "$INFO Cancelling deploy to $app_name."
		exit 0
	fi
}

branch_name=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)

if [[ $branch_name ]]
then
	if [[ $branch_name == "master" ]]
	then
		deploy $branch_name
	else
		deploy $branch_name
	fi
else
  echo -e "$ERROR Unnamed Branch or not a git repository"
  exit 1
fi