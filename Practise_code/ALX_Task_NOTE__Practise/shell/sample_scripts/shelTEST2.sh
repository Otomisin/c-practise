while true
do 
	echo "To God be the glory"
	sleep 2
	trap 'echo "I am invincible!!!"' SIGTERM
done