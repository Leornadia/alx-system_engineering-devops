# 0-strace_is_your_friend.pp - Puppet manifest to fix WordPress file permission issue

# Ensure correct permissions for wp-config.php
file { '/var/www/html/wordpress/wp-config.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Exec['download_wordpress'],
}

# Ensure Apache is restarted to apply changes
service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => File['/var/www/html/wordpress/wp-config.php'],
}

