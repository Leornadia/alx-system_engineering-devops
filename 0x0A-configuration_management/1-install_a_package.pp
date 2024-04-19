class install_flask {
  package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip',
  }
}

