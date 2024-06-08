# lamp_wordpress.pp - Puppet manifest to set up a LAMP stack and install WordPress

# Ensure Apache is installed and running
package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => Package['apache2'],
}

# Ensure MySQL server is installed and running
package { 'mysql-server':
  ensure => installed,
}

service { 'mysql':
  ensure     => running,
  enable     => true,
  subscribe  => Package['mysql-server'],
}

# Ensure PHP and necessary modules are installed
package { ['php', 'php-mysql', 'libapache2-mod-php']:
  ensure => installed,
  before => Service['apache2'],
}

# Create MySQL database and user for WordPress
exec { 'create_mysql_database':
  command => '/usr/bin/mysql -e "CREATE DATABASE IF NOT EXISTS wordpress;"',
  unless  => '/usr/bin/mysql -e "SHOW DATABASES LIKE \'wordpress\';" | grep wordpress',
  require => Package['mysql-server'],
}

exec { 'create_mysql_user':
  command => '/usr/bin/mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO \'wp_user\'@\'localhost\' IDENTIFIED BY \'wp_password\';"',
  unless  => '/usr/bin/mysql -e "SELECT User FROM mysql.user WHERE User = \'wp_user\';" | grep wp_user',
  require => Exec['create_mysql_database'],
}

# Download and install WordPress
exec { 'download_wordpress':
  command => '/usr/bin/wget https://wordpress.org/latest.tar.gz -O /tmp/wordpress.tar.gz',
  creates => '/tmp/wordpress.tar.gz',
  require => Package['apache2'],
}

exec { 'extract_wordpress':
  command => '/bin/tar -xzvf /tmp/wordpress.tar.gz -C /var/www/html',
  creates => '/var/www/html/wordpress',
  require => Exec['download_wordpress'],
}

# Set the correct permissions
file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
  require => Exec['extract_wordpress'],
}

# Configure Apache to serve WordPress site
file { '/etc/apache2/sites-available/wordpress.conf':
  ensure  => file,
  content => "
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/wordpress
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>",
  notify  => Service['apache2'],
}

exec { 'enable_wordpress_site':
  command => '/usr/sbin/a2ensite wordpress.conf',
  unless  => '/usr/sbin/a2query -s wordpress.conf',
  require => File['/etc/apache2/sites-available/wordpress.conf'],
  notify  => Service['apache2'],
}

exec { 'reload_apache':
  command => '/usr/sbin/service apache2 reload',
  refreshonly => true,
  subscribe => Exec['enable_wordpress_site'],
}

