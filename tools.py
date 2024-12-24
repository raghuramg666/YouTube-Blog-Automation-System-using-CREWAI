from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific YouTube channel to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')

# Specify the topic you want to search for within the channel
search_topic = "data scientist"  # Example topic to search for

# Perform the search within the specified channel
results = yt_tool.run(search_topic)

# Print the results
print(dir(yt_tool)) 
