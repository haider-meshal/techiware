This is my first TODO module for odoo.

![Screenshot](TODO.png)

# Development from src (Run it locally: needs to setup pythons and dependencies)
----------------------
(1) cd odoo (root folder)
(2) Run DB server
   docker-compose -f ./dev-source/odoo-db/server.yaml up -d
   docker-compose -f ./dev-source/odoo-db/server.yaml stop
   docker-compose -f ./dev-source/odoo-db/server.yaml down

   # OPTIONAL
   docker-compose -f ./dev-source/odoo-db/client.yaml up -d
   docker-compose -f ./dev-source/odoo-db/client.yaml stop
   docker-compose -f ./dev-source/odoo-db/client.yaml down

(3) Run odoo from source code (This is odoo git clone)
./repo-15/odoo-bin -c ./dev-source/odoo.conf -i base

# Development without src (No python and dependencies needed)
-------------------------
docker-compose -f ./dev-no-source/docker-compose.yaml up -d
docker-compose -f ./dev-no-source/docker-compose.yaml stop
docker-compose -f ./dev-no-source/docker-compose.yaml down
