#!/usr/bin/env bash


config_dir="$HOME/.sgu"
config_file="config"

repo_url=$(git config --get remote.origin.url)
if [ -z "$repo_url" ]; then
	echo "No remote origin set for this repository."
	exit 1
fi

domain_regex=".*@([a-z\.]+):.*"
if [[ $repo_url =~ $domain_regex ]]; then
	domain="${BASH_REMATCH[1]}"
	if [ -z "$domain" ]; then
		echo "No domain found in remote origin."
		exit 1
	fi
	
	mkdir -p $config_dir
	touch "$config_dir/$config_file"

	target_section="[${domain[0]}]"
	found_section=false
	while IFS= read -r line
	do
		if [[ $found_section == true && "$line" != "[${domain[0]}]" ]]; then
			
		fi
	done < "$config_dir/$config_file"
	git config user.email ""
	git config user.rname ""
else
	echo "Remote origin URL did not match expect."
	exit 1
fi

