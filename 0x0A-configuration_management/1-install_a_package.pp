#creating a file /tmp using puppet

file { 'my_file':
    path    => '/tmp/school',
    mode    => '1230',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I can do hard things',
}
