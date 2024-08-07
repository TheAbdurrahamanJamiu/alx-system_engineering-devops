# automating configuration with puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/deafult',
  after  => 'listen do default_server;'
  line   => 'rewrite ^/redirect_me https://www.youtube.com/@thealchemist permanent;',
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => package['nginx']
}
