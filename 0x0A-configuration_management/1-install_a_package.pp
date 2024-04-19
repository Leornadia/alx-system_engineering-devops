# This Puppet manifest installs Flask version 2.1.0 using Pip3

package { 'python3-pip':
  ensure => 'present',
}

exec { 'install-flask':
  command     => 'pip3 install flask==2.1.0',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => Package['python3-pip'],
}
