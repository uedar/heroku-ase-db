git --git-dir=/tmp/heroku-ase-db/.git --work-tree=/tmp/heroku-ase-db pull origin master
cp /tmp/heroku-ase-db/data/atoms.json /tmp/db_snapshot/atoms_$(date "+%Y%m%d").json