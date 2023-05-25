#!/bin/bs
is_master_machine=%s
nginx_conf="config/nginx.conf"
apt-get update
apt-get install redis-server

if [ $is_master_machine ] ; then
  echo 'this is a master machine.'
  service nginx reload -c $nginx_conf
  fi
