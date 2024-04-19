# This Puppet manifest installs Flask version 2.1.0 using Pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
