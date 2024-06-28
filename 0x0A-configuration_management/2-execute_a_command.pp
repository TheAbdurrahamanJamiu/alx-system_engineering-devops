# execute a command with puppet

exec { 'pkill -f enditasap':
  path  => '/usr/bin/:/usr/local/bin/:/bin/',
}
