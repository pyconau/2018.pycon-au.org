require 'time'

desc 'create a new news post'
task :post, [:title]  do |t, args|
    
    title = args[:title]
    if title.nil?
      puts "News posts require a title"
      exit 1
    end

    slug = "#{Date.today}-#{title.downcase.gsub(/[^\w]+/, '-')}"

    file = File.join(File.dirname(__FILE__),'_posts',slug + '.md')

    if File.exists?(file)  
	puts "File already exists as #{file}."
	exit 1
    end

    File.open(file, "w") do |f|
        f << <<-EOS
---
layout: post
title: #{title}
---

        EOS
    end

    puts "Opening #{file}..."
    system ("#{ENV['EDITOR']} #{file}")
end
