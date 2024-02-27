#!/usr/bin/env ruby

puts ARGV[0].scan(/^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]+)\.([a-z]{2,})$/).join

