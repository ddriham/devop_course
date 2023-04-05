!# /usr/bin python3

f = open(r"c:\users\david\song.txt", "r")

#file contant:
# Tudo Bom;Static and Ben El Tavori;5:13;
# I Gotta Feeling;The Black Eyed Peas;4:05;
# Instrumental;Unknown;4:15;
# Paradise;Coldplay;4:23;
# Where is the love?;The Black Eyed Peas;4:13;

with f:
    fr = f.read()
    split = fr.split("\n")
    cnt = 0
    num_string = []
    artists_dict = {}
    longest_song_length = 0
    longest_song_name = ""
    
    for i in split:
        cnt += 1
        num_string.append(i.split(";"))
        song_name, artist, length = i.split(";")[0:3]
        if int(length.split(":")[0]) * 60 + int(length.split(":")[1]) > longest_song_length:
            longest_song_length = int(length.split(":")[0]) * 60 + int(length.split(":")[1])
            longest_song_name = song_name
        if artist in artists_dict:
            artists_dict[artist] += 1
        else:
            artists_dict[artist] = 1

    num_songs = cnt
    artist_most_appearances = max(artists_dict, key=artists_dict.get)
    result_tuple = (longest_song_name, num_songs, artist_most_appearances)

print(result_tuple)
