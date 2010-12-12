path = File.expand_path "../", __FILE__
require 'sinatra'

require "#{path}/config/env"


get "/" do
  haml :index
end

post "/open" do
  @message = "Opened!"
  @out = `python #{path}/lib/phidgets.py`
  haml :index
end