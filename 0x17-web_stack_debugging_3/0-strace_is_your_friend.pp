# Fixes bad "phpp" extensions to "php" in "wp-settings.php".

exec {'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/ww/html/wp-settings.php;',
  path    => '/usr/local/bin/:/bin/'
}
# Puppet manifest to fix file permissions and ensure a module is enabled

# Ensure the file has the correct permissions
file { '/path/to/file':
  ensure  => 'file',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure the Apache module is enabled
apache::mod { 'rewrite':
  ensure => present,
}

# Ensure the Apache service is running and enabled
service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/path/to/file'],
}

# Alternatively, use exec to enable module if not using the puppetlabs/apache module
exec { 'enable_apache_module':
  command => '/usr/sbin/a2enmod rewrite',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/sbin/a2query -m rewrite | grep -q "enabled"',
  notify  => Service['apache2'],
}
