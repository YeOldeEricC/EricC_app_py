git pull;
for (( ; ; )) # infinite loop
do
	echo "Git commit message:";
	read message; # type your message here on prompt
	echo " ";
	echo "Are you sure you want to send this? (y/n)";
	read yn; # confirm or redo vya y/n
	# if sure or not
	if [[ "${yn}" == "y" ]]
	then
		echo " ";
		echo "Pushing to GitHub with message:";
		echo "${message}";
		echo " ";
		git add .;
		git commit -m "${message}";
		git push;
		git pull;
		break;
	fi
done
echo " ";
echo "-- DONE --";
echo " ";